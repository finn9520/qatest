#Getting Started

If you have not installed python3 or pipenv, you can do so by following the directions at the following links:

- Python: https://www.python.org/downloads/
- Pipenv: https://pypi.org/project/pipenv/

Follow the instructions below to execute the test suite

1) Verify that you are in the root directory of the project
2) Run `pipenv install` to install all packages needed for the tests
3) Use the command `pipenv shell` to start the virtual env
4) Execute all tests simply by running `pytest`.  This will collect all tests that start with the word "test" in the directory
5) Using the command `pytest -k "<string>"` will find any test case file that partially matches the value in `<string>` and run only that subset.  For example `pytest -k "smoke" will run any test that has the word "smoke" in the name
6) Pytest will output the Pass/Fail results of all tests run
# qatest
