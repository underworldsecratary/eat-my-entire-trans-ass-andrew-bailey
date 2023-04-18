# Tool for submitting data to the Missouri Attorney Generalk Transgender Center Concerns Form

Url: https://ago.mo.gov/file-a-complaint/transgender-center-concerns

If you want to be a helpful citizen and submit some data to Andrew Bailey, install requirements.txt and run fu_andrew.py. It's faster than going to https://ago.mo.gov/file-a-complaint/transgender-center-concerns and submitting manually and this way we can make sure the website really gets some use.

The `time.sleep()` is set conservatively, but play with it maybe there's no rate limiting.

## Installation guide

First install python and pip:[https://www.python.org/downloads/](https://www.python.org/downloads/)

[https://packaging.python.org/en/latest/tutorials/installing-packages/](https://packaging.python.org/en/latest/tutorials/installing-packages/)

You will be using the command py for windows python3 for MacOS and Linux

install dependencies

    python3 -m pip install certifi charset-normalizer Faker idna python-dateutil requests six urllib3 pandas

in a folder download `defendTrans.py` and `moAddressData.csv`.  make sure they are in the same folder

(The updated version gives user output, so you can see it is working correctly)

now run it by entering:

    python3 defendTrans.py

Using the later version you should see something like:

    $ python3 defendTrans.py
    Response submitted for
    Kent, Joann
    63242 Jessica Manors
    HOLLIDAY, MO, 65258
    snyderjeffrey@hotmail.com 747.133.8330
    Suffer third environmental course. Suddenly development organization read language stock ........
