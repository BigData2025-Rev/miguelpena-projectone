import pytest
from implementation.input_validation import InputValidation
from implementation.enum_classes.validation_type import ValidationType
from custom_exceptions.invalid_number_input import InvalidNumberInput
from custom_exceptions.invalid_menu_selection import InvalidMenuSelection
from custom_exceptions.invalid_string_input import InvalidStringInput

input_validation: InputValidation | None = None

def test_validate_number_alpha_input():
    """
        Must throw an exception when user provides an alphabetical input.
    """
    with pytest.raises(InvalidNumberInput):
        input_validation = InputValidation('g', ValidationType.IsANumber)
        result = input_validation.is_valid()
    # assert result == False

def test_validate_number_negative_input():
    """
        Must throw an exception if number is not a positive number, since something like 
        100 - (-100) will result in bad behaviour in a banking/budgeting app.
    """
    with pytest.raises(InvalidNumberInput):
        input_validation = InputValidation('-23', ValidationType.IsANumber)
        result = input_validation.is_valid()

def test_validate_number_negative_float_input():
    """
        Must throw an exception if number is not a positive number, since something like 
        100 - (-100) will result in bad behaviour in a banking/budgeting app.
    """
    with pytest.raises(InvalidNumberInput):
        input_validation = InputValidation('-2.123', ValidationType.IsANumber)
        result = input_validation.is_valid()

def test_validate_number_integer_input():
    """
        If the number entry is positive and is a float or integer, then make sure validation is true.
    """
    input_validation = InputValidation('23', ValidationType.IsANumber)
    result = input_validation.is_valid()
    assert result == True

def test_validate_number_float_input():
    """
        If the number entry is positive and is a float or integer, then make sure validation is true.
    """
    input_validation = InputValidation('23.50', ValidationType.IsANumber)
    result = input_validation.is_valid()
    assert result == True

def test_validate_menuoption_invalid_number_input():
    """
        Must raise the InvalidMenuSelection exception if user inputs anything other than a valid character from a string
    """
    with pytest.raises(InvalidMenuSelection):
        input_validation = InputValidation('123', ValidationType.IsAMenuOption, valid_options = 'abc')
        result = input_validation.is_valid()
    # assert result == False

def test_validate_menuoption_invalid_string_input():
    """
        Must raise the InvalidMenuSelection exception if user inputs anything other than a valid character from a string
    """
    with pytest.raises(InvalidMenuSelection):
        input_validation = InputValidation('Hello World!', ValidationType.IsAMenuOption, valid_options = 'abc')
        result = input_validation.is_valid()
    # assert result == False

def test_validate_menuoption_lower_input():
    """
        Must be able to detect valid upper and lowercase inputs.
    """
    input_validation = InputValidation('a', ValidationType.IsAMenuOption, valid_options = 'abc')
    result = input_validation.is_valid()
    assert result == True

def test_validate_menuoption_upper_input():
    """
        Must be able to detect valid upper and lowercase inputs.
    """
    input_validation = InputValidation('A', ValidationType.IsAMenuOption, valid_options = 'abc')
    result = input_validation.is_valid()
    assert result == True

def test_validate_string_too_short_input():
    """
        Must raise the InvalidStringInput when user fails to meet one or more criteria for strings like username, password, or category names.
    """
    with pytest.raises(InvalidStringInput):
        input_validation = InputValidation('He', ValidationType.IsValidString, reject_short = True, can_contain_numbers = False)
        result = input_validation.is_valid()

def test_validate_string_contains_numbers_input():
    """
        Must raise the InvalidStringInput when user fails to meet one or more criteria for strings like username, password, or category names.
    """
    with pytest.raises(InvalidStringInput):
        input_validation = InputValidation('123345', ValidationType.IsValidString, reject_short = True, can_contain_numbers = False)
        result = input_validation.is_valid()

def test_validate_string_valid_input():
    """
        Must return true if all conditions are met.
    """
    input_validation = InputValidation('Hamburger', ValidationType.IsValidString, reject_short = True, can_contain_numbers = False)
    result = input_validation.is_valid()
    assert result == True

def test_validate_string_username_input():
    """
        Must return true if all conditions are met.
    """
    input_validation = InputValidation('Hamburger223', ValidationType.IsValidString, reject_short = True, can_contain_numbers = True)
    result = input_validation.is_valid()
    assert result == True

def test_validate_string_missing_booleans():
    """
        Must raise InvalidStringInput if booleans aren't included.
    """
    with pytest.raises(InvalidStringInput):
        input_validation = InputValidation('Master123', ValidationType.IsValidString)
        result = input_validation.is_valid()

