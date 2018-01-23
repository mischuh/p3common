# -*- coding: utf-8 -*-
import pytest

import common.validators as validate
from common.validators.utils import ValidationException


@pytest.mark.parametrize('value', [
    'hallo',
])
def test_returns_true_on_not_emtpy_str(value):
    assert validate.str_not_empty(value)


@pytest.mark.parametrize('value', [
    None,
    '',
])
def test_returns_failed_on_not_empty_str(value):
    with pytest.raises(ValidationException):
        validate.str_not_empty(value)


@pytest.mark.parametrize('value', [
    'hallo',
])
def test_returns_true_is_str(value):
    assert validate.is_str(value)


@pytest.mark.parametrize('value', [
    None,
    123,
])
def test_returns_failed_on_not_is_str(value):
    with pytest.raises(ValidationException):
        validate.is_str(value)


@pytest.mark.parametrize(('value', 'comparator'), [
    ('hallo', 'hallo'),
])
def test_returns_true_on_equal_str(value, comparator):
    assert validate.str_is_equal(value, comparator)


@pytest.mark.parametrize(('value', 'comparator'), [
    ('hello', 'hallo'),
    ('hello', None),
    (None, 'hallo'),
    (None, None),
])
def test_returns_failed_on_equal_str(value, comparator):
    with pytest.raises(ValidationException):
        validate.str_is_equal(value, comparator)
