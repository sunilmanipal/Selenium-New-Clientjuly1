import pytest

class TestDemo:
    @pytest.mark.third
    def test_case1(self):
        print("C")

    @pytest.mark.fourth
    def test_case2(self):
        print("D")

    @pytest.mark.second
    def test_case3(self):
        print("B")

    @pytest.mark.first
    def test_case4(self):
        print("A")