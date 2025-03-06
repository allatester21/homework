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
@pytest.mark.parametrize("input_str, expected", [
    ("Hello!", "l"),
    ("SkyPro programm", "P"),
    ("world43", "d"),
])
def test_contains_positive(input_str, expected):
    assert string_utils.contains(input_str, expected)


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("Test result", "a"),
    ("137 day", "2"),
    ("  ", "L"),
])
def test_contains_negative(input_str, expected):
    string_utils.contains(input_str, expected)


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("Hello!", "l"),
    ("SkyPro Programm", "P"),
    ("world date", "d"),
])
def test_delete_symvol_positive(input_str, expected):
    assert string_utils.delete_symbol(input_str, expected)


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("Hello mam!", "f"),
    ("37652the", "1"),
    (" wor ld", ""),
])
def test_delete_symvol_negative(input_str, expected):
    assert string_utils.delete_symbol(input_str, expected)
