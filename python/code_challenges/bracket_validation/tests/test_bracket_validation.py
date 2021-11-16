from bracket_validation import __version__
from bracket_validation.bracket_validation import validate_brackets


def test_version():
    assert __version__ == '0.1.0'


def test_brackets_1():
    actual = validate_brackets('[[()]]')
    excepted = True
    assert actual == excepted

def test_brackets_10():
    actual = validate_brackets('{[()]}')

    excepted = True
    assert actual == excepted

def test_brackets_2():
    actual = validate_brackets('[[(')
    excepted = False
    assert actual == excepted

def test_brackets_3():
    actual = validate_brackets('{')
    excepted = False
    assert actual == excepted

def test_brackets_4():
    actual = validate_brackets('{')
    excepted = False
    assert actual == excepted

def test_brackets_5():
    actual = validate_brackets('{')
    excepted = False
    assert actual == excepted

def test_brackets_6():
    actual = validate_brackets('{[[]]}')
    excepted = True
    assert actual == excepted
