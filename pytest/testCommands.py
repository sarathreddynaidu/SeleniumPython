# Run all tests in a module/file

    # pytest -v -s test_Login.py
    # pytest -v -s test_Signup.py

# Run all tests from all modules in a path

    # pytest -v -s C:\seleniumpython\mypack\

# Run specific test method from a module

    # pytest -v -s test_Login.py::test_loginByEmail

# -s -> to print statements
# -v -> verbose