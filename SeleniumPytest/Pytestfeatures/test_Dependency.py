import pytest

class TestDemo:
    # if my first method is succefull then it will execute the second
    @pytest.mark.dependency()
    def test_Login(self):
        assert True

    @pytest.mark.dependency(depends=['TestDemo::test_Login'])
    def test_HomePage(self):
        assert True

    @pytest.mark.dependency(depends=['TestDemo::test_HomePage'])
    def test_SelectProduct(self):
        assert False

    @pytest.mark.dependency(depends=['TestDemo::test_SelectProduct'])
    def test_Logout(self):
        assert True