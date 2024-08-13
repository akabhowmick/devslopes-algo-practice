from ReverseString import reverse_string


def test_reverse_empty_string():
    assert reverse_string("") == ""


def test_reverse_string_palindrome():
    input_string = "racecar"
    expected_output = "racecar"
    assert reverse_string(input_string) == expected_output


def test_reverse_odd_length_string():
    input_string = "hello"
    expected_output = "olleh"
    assert reverse_string(input_string) == expected_output

def test_reverse_string_mixed_case():
    input_string = "Hello WOrLd"
    expected_output = "dlroW olleH"
    assert reverse_string(input_string) == expected_output
def test_reverse_uppercase_string():
    input_string = "HELLO"
    expected_output = "OLLEH"
    assert reverse_string(input_string) == expected_output

def test_reverse_string_special_characters():
    input_string = "!@#$%^&*()_+-="
    expected_output = "=+-_*(^&%$#@!"
    assert reverse_string(input_string) == expected_output
    
def test_reverse_string_mixed_characters():
    input_string = "!@#$%^&*()_+-=1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    expected_output = "zyxwvutsrqponmlkjihgfedcba9876543210_+-=*(&^%$#@! "
    assert reverse_string(input_string) == expected_output