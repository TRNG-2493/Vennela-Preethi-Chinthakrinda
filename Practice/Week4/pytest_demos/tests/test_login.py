import csv
from pathlib import Path
import pytest
from auth import login

DATA_FILE = Path(__file__).parent/"data"/"login_data.csv"
# before wr test cases we need to wr what we are testing

# 2 steps in data driven testing
# 1. loading the data to test
# 2. testing 
# if we have to load multiple files - use fixtures

# loading the data row by row
def load_cases():
    with open(DATA_FILE) as f:
        reader = csv.DictReader(f) # reacs the csv and converts to dict
        return [
            (row["username"], row["password"], row["expected"])
            for row in reader
        ]
# test the login method

@pytest.mark.parametrize("username,password,expected", load_cases())
def test_login(username,password,expected):
    
    assert login(username,password) == (expected=="True") # without true it is failing "why?"
    