import pytest



class TestApplication:
    # Setup is a decorator or fixture
    # this executes before every method runs
    @pytest.fixture() #Decorators
    def setup(self):
        print("i want to launch the browser")
        print("I want to open the app")
        yield
        print("This is to clean or close the browser") # which executes after each method is executed

    def test_Login(self,setup):
        print("This is the login page")

    def test_Links(self,setup):
        print("All the links are working fine")

    def test_Logout(self,setup):
        print("Logout successfull")