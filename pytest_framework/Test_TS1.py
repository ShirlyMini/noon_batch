import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_tc1(setup_module):
    print("this is tc1")

@pytest.mark.regression
def test_tc2():
    print("this is tc2")

@pytest.mark.sanity
def test_tc3():
    print("this is tc3")