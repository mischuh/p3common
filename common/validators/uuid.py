import re

from .utils import Validator

pattern = re.compile(r'^[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}$')


@Validator
def uuid(value):
    """
    Checks whether or not given value is a valid UUID.
    Examples::
        >>> uuid('2bc1c94f-0deb-43e9-92a1-4775189ec9f8')
        True
        >>> uuid('2bc1c94f 0deb-43e9-92a1-4775189ec9f8')
        ValidationException(func=uuid, ...)
    :param value: UUID string to validate
    :return: True, if value is valid UUID,
             otherwise :class:`~validators.utils.ValidationException`
    """
    return pattern.match(value)
