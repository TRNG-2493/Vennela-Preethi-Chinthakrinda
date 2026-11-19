import pytest
@pytest.fixture()
# annotate the method or decorator
def credentials():
    return {"username" : "standard_user", "password": "secret_sauce_1"}

# credentials is custom fixture
@pytest.fixture
def logged_in_page(page, credentials):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", credentials["username"])
    page.fill("#password", credentials["password"])
    page.click("#login-button")
    
    return page

# it is a hook playwright calls
def pytest_sessionstart(session):
    print("pytest calls this once as the session starts")
    
def pytest_sessionfinish(session):
    print("pytest calls this once as the session ends")