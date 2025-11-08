import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   Hello!", "Hello!"),
    (" 164", "164"),
    ("  ", ""),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("Test", "Test"),
    ("12 april", "12 april"),
    ("", ""),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol_str, expected", [
    ("Hello!", "l", True),
    ("SkyPro programm", "P", True),
    ("world43", "d", True),
])
def test_contains_positive(input_str, symbol_str, expected):
    assert string_utils.contains(input_str, symbol_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol_str, expected", [
    ("Test result", "a", False),
    ("137 day", "2", False),
    ("  ", "L", False),
])
def test_contains_negative(input_str, symbol_str, expected):
    assert string_utils.contains(input_str, symbol_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol_str, expected", [
    ("Hello!", "l", "Heo!"),
    ("SkyPro Programm", "P", "Skyro rogramm"),
    ("world date", "d", "worl ate"),
])
def test_delete_symbol_positive(input_str, symbol_str, expected):
    assert string_utils.delete_symbol(input_str, symbol_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol_str, expected", [
    ("Hello mam!", "f", "Hello mam!"),
    ("37652the", "1", "37652the"),
    (" wor ld", "", " wor ld"),
])
def test_delete_symbol_negative(input_str, symbol_str, expected):
    assert string_utils.delete_symbol(input_str, symbol_str) == expected
