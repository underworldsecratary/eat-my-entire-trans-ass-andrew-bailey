import requests
import json
import sys
import time
from faker import Faker
import csv
import random
import pandas as pd

fake = Faker()
url = "https://ago.mo.gov/file-a-complaint/transgender-center-concerns?sf_cntrl_id=ctl00$MainContent$C001"

#counts lines in datafile
with open('moAddressData.csv', 'rt') as f:
    for i, _ in enumerate(f):
        pass
num_lines = i+1
print(num_lines)

while True:
    random_row = random.sample(range(num_lines), num_lines-1)
    df = pd.read_csv('moAddressData.csv', skiprows=random_row, header=None)
    print(df)

    data = {"TextFieldController_4": fake.first_name(),
            "TextFieldController_5": fake.last_name(),
            "TextFieldController_1": fake.street_address(),
            "TextFieldController_2": df.at[0, 2],
            "DropdownListFieldController": "MO",
            "TextFieldController_6": int(df.at[0, 0]),
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

    print("Response submitted for \n{0}, {1} \n{2} \n{3}, {4}, {5} \n{6} {7} \n{8}".format( data["TextFieldController_5"],
                                                    data["TextFieldController_4"], data["TextFieldController_1"], data["TextFieldController_2"],
                                                    data["DropdownListFieldController"], data["TextFieldController_6"], data["TextFieldController_0"],
                                                    data["TextFieldController_3"], data["ParagraphTextFieldController"] ))

    time.sleep(0.01)
