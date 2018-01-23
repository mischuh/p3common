# -*- coding: utf-8 -*-
import pytest

import common.validators as validate
from common.validators.utils import ValidationFailure


@pytest.mark.parametrize(('value', 'instance_type'), [
    ('string', str),
    (123, int),
    ({'key': 'value'}, dict),
    ([1, 2, 3, 4], list),
    ((1, 2, 3, 4), tuple),
])
def test_returns_true_on_valid_instance_type(value, instance_type):
    assert validate.is_instance(value, instance_type)


@pytest.mark.parametrize(('value', 'instance_type'), [
    ('string', int),
    (123, list),
    ({'key': 'value'}, int),
    ([1, 2, 3, 4], tuple),
    ((1, 2, 3, 4), dict),
    (None, None)
])
def test_returns_failed_validation_on_invalid_instance_type(value, instance_type):
    res = validate.is_instance(value, instance_type)
    assert not res
    assert isinstance(res, ValidationFailure)


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
    res = validate.is_function(value)
    assert not res
    assert isinstance(res, ValidationFailure)

