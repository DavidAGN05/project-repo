import pytest

from bank import value

def test_starting_h():
    assert value("hi") == "$20"

def test_hello():
    assert value("hello") == "$0"

def test_no_greeting():
    assert value() == "$100"

def test_bad_greeting():
    assert value("goodbye") == "$100"

def test_non_string():
    assert value(1) == "$100"