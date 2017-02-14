import json
import os

from fixture.orm import ORMFixture
from model.group import Group

config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "target.json")
with open(config_file) as f:
    configuration = json.load(f)

db = ORMFixture(
    host=configuration['db']['host'],
    name=configuration['db']['name'],
    user=configuration['db']['user'],
    password=configuration['db']['password']
)

l = db.get_contacts_in_group(Group(id='30'))
for item in l:
    print(item)
print(len(l))
