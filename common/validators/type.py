from common.validators.utils import Validator, not_none


@Validator
def is_instance_of(value, instance_type):
    """
    Checks if value is instance of specific type
    :param value:
    :param instance_type:
    :return: True, if value is instance of type,
             otherwise :class:`~validators.utils.ValidationException`
    """
    return not_none(value) and isinstance(value, instance_type)


@Validator
def is_function(value):
    """
    Checks if value is a callable object
    :param value:
    :return: True, if value is a callable objecr,
             otherwise :class:`~validators.utils.ValidationException`
    """
    return not_none(value) and callable(value)
