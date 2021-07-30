import pytest


@pytest.yield_fixture()  # make sure you pass that function name in other function
def setup():
    print("Once before every method")
    yield  # statements before yield are generated before tests and statements after yield are generated after tests
    print("Once after every method")

def testMethod1(setup):
    print("Test method 1")

def testMethod2(setup):
    print("Test method 2")
