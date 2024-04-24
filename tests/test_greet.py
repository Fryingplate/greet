# test_greet.py

import builtins
from unittest import mock
from greet import greet

def test_greet():
    with mock.patch('builtins.input', return_value='John'):
        greeting = greet()
        assert greeting == "Hello, John!", "Greeting didn't match expected output"
