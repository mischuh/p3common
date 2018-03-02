# -*- coding: utf-8 -*-
import pytest

import common.validators as validate
from common.validators.utils import ValidationException


def test_fail_hard():
    with pytest.raises(ValidationException):
        validate.not_none(None)


def test_fail_not_hard():
    assert not validate.not_none(None, fail=False)
