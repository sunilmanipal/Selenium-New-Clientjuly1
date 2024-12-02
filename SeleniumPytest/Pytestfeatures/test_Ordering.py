import pytest

class TestDemo:
    @pytest.mark.run(order=3)
    def test_case1(self):
        print("C")

    @pytest.mark.run(order=4)
    def test_case2(self):
        print("D")

    @pytest.mark.run(order=2)
    def test_case3(self):
        print("B")

    @pytest.mark.run(order=1)
    def test_case4(self):
        print("A")