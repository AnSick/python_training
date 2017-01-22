# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="Kim2", middle_name="Woo", last_name="Bin", nickname="bigbangtheory13",
                               title="leading software engineer",
                               company="SBS Entertainment", address="Songnam-gu, 145-12, Okchomdang, Seoul",
                               home_number="713 823-52-32",
                               mobile_number="010-352-51-32", email="sunnykimwoobit@gmail.co.kr",
                               website="kimwoobin.co.kr", notes="Handsome and sweet",
                               work_number="512 09 56", fax="3321", email2="dagaga", email3="agsagsag",
                               day_of_birth="1", month_of_birth="1", birth_year="1994",
                               day_of_anniversary="1", month_of_anniversary="1", anniversary_year="4131",
                               address2="hjfkhaskfjsaf", phone2="jsfahsfjksaf",
                               photo="C:\\Workspace\\Python\\python_training\\hola.png"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="", middle_name="", last_name="", nickname="", title="",
                               company="", address="", home_number="",
                               mobile_number="", email="", website="", notes="",
                               work_number="", fax="", email2="", email3="", day_of_birth="3",
                               month_of_birth="2", birth_year="",
                               day_of_anniversary="3", month_of_anniversary="2", anniversary_year="",
                               address2="", phone2="",
                               photo="C:\\Workspace\\Python\\python_training\\hola.png"))
    app.session.logout()
