import pytest
@pytest.fixture(scope="class")
def setup():
    print("open the browser and the application")
    yield
    print("Closing the broswer and app")