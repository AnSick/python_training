import pytest
from fixture.application import Application
import json
import os.path
import importlib

fixture = None
target = None


@pytest.fixture
def app(request):
    global fixture
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as f:
            target = json.load(f)
    browser = request.config.getoption("--browser")
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, baseUrl=target['baseUrl'])
    fixture.session.ensure_login(username=target['username'], password=target['password'])
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action = "store", default = "firefox")
    parser.addoption("--target", action = "store", default = "target.json")


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids = [str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata