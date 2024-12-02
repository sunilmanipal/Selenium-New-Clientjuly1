import pytest


class TestFeatures:
    def test_case1(self):
        print("testcase1")

    @pytest.mark.skip
    def test_case2(self):
        print("testcase2")

    def test_case3(self):
        print("testcase3")