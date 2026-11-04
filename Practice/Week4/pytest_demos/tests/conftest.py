import pytest
@pytest.fixture(scope="session")
def app_config():
    return {"currency": "USD", "tax_rate": 0.1}