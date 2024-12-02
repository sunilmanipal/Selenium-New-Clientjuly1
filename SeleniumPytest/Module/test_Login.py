import pytest

@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_Login1(self):
        print("This is login")
        assert True == True


    def test_Login2(self):
        print("This is login2")
        assert True == True