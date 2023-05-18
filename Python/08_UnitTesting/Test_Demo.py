# test cases for pytest

import pytest
from Demo import convert_to_int, add, dict_keys

def test_convert_to_int():
    result = convert_to_int('2,351')
    assert result == 2351

def test_add():
    result = add(2,3)
    assert result == 5

def test_dict_keys():
    result = dict_keys({'a': 1, 'b': 2}) 
    expected = dict_keys['a', 'b']
    assert result == expected

def test_dict_keys_invalid():
    result = dict_keys[1,2,3,4]
    expected = 'Invalid Input'
    return result == expected