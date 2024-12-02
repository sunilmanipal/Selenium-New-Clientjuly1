import pytest

@pytest.mark.usefixtures("setup")
class TestLinks:

    def test_Links(self):
        print("This is links")
        assert True == True