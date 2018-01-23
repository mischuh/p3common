
from .utils import Validator, not_none


@Validator
def str_not_empty(value):
    """
    Checks whether or not given value is not empty.
    Examples::
        >>> str_not_empty('test')
        True
        >>> str_not_empty(None)
        ValidationFailure(func=str_not_empty, ...)
    :param value: string to validate
    :return: True, if str is not empty, otherwise :class:`~validators.utils.ValidationFailure`
    """
    return not_none(value) and value != ''


@Validator
def is_str(value):
    """
    Checks if value is instance of str.
    Examples::
        >>> is_str('test')
        True
        >>> is_str(123)
        ValidationFailure(func=is_str, ...)
    :param value: string to check
    :return: True, if is instance, otherwise :class:`~validators.utils.ValidationFailure`
    """
    return str_not_empty(value) and isinstance(value, str)


@Validator
def str_is_equal(value, comparator):
    """
    Checks if value is equal to comparator.
    Examples::
        >>> str_is_equal('test', 'test')
        True
        >>> str_is_equal('test', 'bla')
        ValidationFailure(func=str_is_equal, ...)
    :param value: string to validate
    :param comparator: string to compare to
    :return: True, if strings are equal, otherwise :class:`~validators.utils.ValidationFailure`
    """
    return is_str(value) and is_str(comparator) and value == comparator
