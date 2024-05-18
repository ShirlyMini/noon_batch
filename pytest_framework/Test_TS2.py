import pytest

class Test_TS2:
    @pytest.mark.regression
    def test_tc1(self, setup, setup_class, setup_module):
        print(setup)
        print("this is tc1")

    @pytest.mark.xfail
    @pytest.mark.regression
    # @pytest.mark.skip
    # @pytest.mark.skipif(5>4, reason="skipped the testcase bcoz condition is true")
    def test_tc2(self, setup):
        print("this is tc2")
        assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_tc3(self, setup):
        print("this is tc3")