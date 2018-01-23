from common.validators.utils import Validator, not_none
from common.validators.type import is_instance


@Validator
def list_not_empty(a_list):
    """
    Checks if a list is empty
    :param a_list: a list
    :return: True, if list is not empty, otherwise :class:`~validators.utils.ValidationFailure`
    """
    return not_none(a_list) and len(a_list) > 0


@Validator
def is_in_list(value, the_list):
    """
    Checks if a value is in given list
    Examples::
        >>> is_in_list('test', [1, 2, 'test'])
        True
        >>> is_in_list(None, [])
        ValidationFailure(func=is_in_list, ...)
    :param value: value to check
    :param the_list: list of elems
    :return: True, if value is instance of type, otherwise :class:`~validators.utils.ValidationFailure`
    """
    return not_none(value) and is_instance(the_list, list) and value in the_list


@Validator
def is_in_dict_keys(value, the_dict):
    """
    Checks if valie is in dictkeys
    Examples::
        >>> is_in_dict_keys('test', {'1': val1, 'test': val2})
        True
        >>> is_in_dict_keys(None, {'1': val1, 'test': val2})
        ValidationFailure(func=is_in_dict_keys, ...)
    :param value: value to check
    :param the_dict: dictionary to test on
    :return: True, if value is in dict keys, otherwise :class:`~validators.utils.ValidationFailure`
    """
    return is_instance(the_dict, dict) and is_in_list(value, list(the_dict.keys()))
