# -*- coding: utf-8 -*-
import pytest

import common.validators as validate
from common.validators.utils import ValidationFailure


@pytest.mark.parametrize(('value',), [
    ('2bc1c94f-0deb-43e9-92a1-4775189ec9f8',),
])
def test_returns_true_on_valid_mac_address(value):
    assert validate.uuid(value)


@pytest.mark.parametrize(('value',), [
    ('2bc1c94f-deb-43e9-92a1-4775189ec9f8',),
    ('2bc1c94f-0deb-43e9-92a1-4775189ec9f',),
    ('gbc1c94f-0deb-43e9-92a1-4775189ec9f8',),
    ('2bc1c94f 0deb-43e9-92a1-4775189ec9f8',),
])
def test_returns_failed_validation_on_invalid_mac_address(value):
    assert isinstance(validate.uuid(value), ValidationFailure)

