import pytest

class Test_TS3:
    @pytest.mark.parametrize("a", [1,2,3,4])# data driven testing
    def test_tc1(self,setup, a):
        print("this is tc1 from TS3", a)

    @pytest.mark.parametrize("a,b,c", [(1,2,3),(10,20,30),(100,200,300)])# data driven testing
    def test_tc2(self,setup, a,b,c):
        print("this is tc2 from TS3", a,b,c)

#pytest -v -s -k "Test" -n=2 --html=./logs.html --capture=tee-sys
