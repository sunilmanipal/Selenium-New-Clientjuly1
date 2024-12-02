import pytest

@pytest.mark.usefixtures("setup")
class TestLogot:

    def test_Logout(self):
        print("This is logout")
        assert True == True