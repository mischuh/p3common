# -*- coding: utf-8 -*-
import pytest

import common.validators as validate
from common.validators.utils import ValidationException


@pytest.mark.parametrize(('value', 'instance_type'), [
    ('string', str),
    (123, int),
    ({'key': 'value'}, dict),
    ([1, 2, 3, 4], list),
    ((1, 2, 3, 4), tuple),
])
def test_returns_true_on_valid_instance_type(value, instance_type):
    assert validate.is_instance_of(value, instance_type)


@pytest.mark.parametrize(('value', 'instance_type'), [
    ('string', int),
    (123, list),
    ({'key': 'value'}, int),
    ([1, 2, 3, 4], tuple),
    ((1, 2, 3, 4), dict),
    (None, None)
])
def test_returns_failed_validation_on_invalid_instance_type(value, instance_type):
    with pytest.raises(ValidationException):
        validate.is_instance_of(value, instance_type)


@pytest.mark.parametrize('value', [
    print,
    eval
])
def test_returns_true_on_valid_function(value):
    assert validate.is_function(value)


@pytest.mark.parametrize('value', [
    'hallo',
    None
])
def test_returns_true_on_invalid_function(value):
    with pytest.raises(ValidationException):
        validate.is_function(value)
