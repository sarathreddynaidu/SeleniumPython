import pytest


@pytest.fixture()  # once before every method, make sure you pass that function name in other function
def setup():
    print("Once before every method")

def testMethod1(setup):
    print("Test method 1")

def testMethod2(setup):
    print("Test method 2")
