import pytest

class Test_1:

    def test_2(self):
        a=12
        b=10
        c=a*b
        if c==120:
            print("Passed")
            assert True
        else:
            print("Failed")
            assert False