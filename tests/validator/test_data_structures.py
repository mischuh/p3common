# -*- coding: utf-8 -*-
import pytest

import common.validators as validate
from common.validators.utils import ValidationException


@pytest.fixture(scope="function")
def the_list():
    yield [
        'hallo', 'hello', 'test', [1, 2, 3]
    ]


@pytest.fixture(scope="function")
def the_dict():
    yield {
        'hello': 'asdf',
        'hallo': 1234,
        'test': None
    }


def test_returns_true_on_list_is_not_empty(the_list):
    assert validate.list_not_empty(the_list)


def test_returns_failed_on_list_is_not_empty():
    with pytest.raises(ValidationException):
        validate.list_not_empty([])


@pytest.mark.parametrize('value', [
    None,
    123,
])
def test_returns_failed_on_elem_is_in_list(value, the_list):
    with pytest.raises(ValidationException):
        validate.is_in_list(value, the_list)


@pytest.mark.parametrize('value', [
    'hallo',
    'hello',
    'test',
    [1, 2, 3]
])
def test_returns_true_on_elem_is_in_list(value, the_list):
    assert validate.is_in_list(value, the_list)


@pytest.mark.parametrize('value', [
    None,
    123,
])
def test_returns_failed_on_elem_is_in_list(value, the_list):
    with pytest.raises(ValidationException):
        validate.is_in_list(value, the_list)


@pytest.mark.parametrize('value', [
    'hallo',
    'hello',
    'test'
])
def test_returns_true_on_elem_is_in_dict(value, the_dict):
    assert validate.is_in_dict_keys(value, the_dict)


@pytest.mark.parametrize('value', [
    None,
    123,
])
def test_returns_failed_on_elem_is_in_dict(value, the_dict):
    with pytest.raises(ValidationException):
        validate.is_in_dict_keys(value, the_dict)
