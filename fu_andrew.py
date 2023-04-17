import requests
import json
import time

from faker import Faker

fake = Faker()


url = "https://ago.mo.gov/file-a-complaint/transgender-center-concerns?sf_cntrl_id=ctl00$MainContent$C001"

for i in range(0, 10000):
    data = {"TextFieldController_4": fake.first_name(),
        "TextFieldController_5": fake.last_name(),
        "TextFieldController_1": fake.street_address(),
        "TextFieldController_2": fake.city(),
        "DropdownListFieldController": fake.state_abbr(),
        "TextFieldController_6": fake.postcode(),
        "TextFieldController_0": fake.free_email(),
        "TextFieldController_0": fake.phone_number(),
        "ParagraphTextFieldController": fake.paragraph(10)}

    data_json = json.dumps(data)
    headers = {"Content-type": "application/json",
            "user-agent": fake.user_agent(),
            "cookie": ""}

    requests.post(url, data=data_json, headers=headers)
    time.sleep(1)
    