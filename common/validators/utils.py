"""
https://github.com/kvesteri/validators/blob/master/validators/utils.py
"""

import functools
import inspect
import itertools
from collections import OrderedDict


class ValidationException(Exception):
    def __init__(self, func, args):
        self.func = func
        self.__dict__.update(args)

    def __repr__(self):
        return u'ValidationException(func={func}, args={args})'.format(
            func=self.func.__name__,
            args=dict(
                [(k, v) for (k, v) in self.__dict__.items() if k != 'func']
            )
        )

    def __str__(self):
        return repr(self)

    def __bool__(self):
        return False

    def __nonzero__(self):
        return False


class Validator(object):
    """
    A decorator that makes given function a validator.
    Whenever the given function is called and returns ``False`` value
    this decorator returns :class:`ValidationException` object.
    Example::
        >>> @Validator
        ... def even(value):
        ...     return not (value % 2)
        >>> even(4)
        True
        >>> even(5)
        ValidationException(func=even, args={'value': 5})
    """
    def __init__(self, func):
        """
        :param func: function to decorate
        """
        self.func = func
        functools.update_wrapper(self, func)

    def __func_args_as_dict(self, func, args, kwargs):
        """
        Return given function's positional and key value
        arguments as an ordered dictionary
        """
        arg_names = list(
            OrderedDict.fromkeys(
                itertools.chain(
                    inspect.getfullargspec(func)[0],
                    kwargs.keys()
                )
            )
        )
        return OrderedDict(
            list(zip(arg_names, args)) +
            list(kwargs.items())
        )

    def __call__(self, *args, **kwargs):
        """
        :param args: positional function arguments
        :param kwargs: key value function arguments
        """
        fail_hard = kwargs.pop('fail', True)
        value = self.func(*args, **kwargs)
        if not value and fail_hard:
            raise ValidationException(
                self.func, self.__func_args_as_dict(self.func, args, kwargs)
            )
        return value


@Validator
def not_none(value):
    """
    Checks if value is not None
    :param value: any given value
    :return: True, if value is not None,
    """
    return value is not None
