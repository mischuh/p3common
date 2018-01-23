import pytest

from common.collections import get_value_from_dictionary, group_by, merge_dicts, safe_list_get, chunk_list
from common.validators.utils import ValidationException


def test_group_by():
    input = ["a1", "a2", "b1", "c1", "c2"]
    res = group_by(lambda x: x[0], input)

    assert "a" in res and "b" in res and "c" in res
    assert len(res["a"]) == 2
    assert len(res["b"]) == 1
    assert len(res["c"]) == 2


def test_failed_group_by():
    with pytest.raises(ValidationException):
        group_by(lambda x: x[0], {'1': 'asdf', '2': 'asfdasf'})


def test_get_value_from_dictionary():
    d = {'a': 'a', 'b': {'b1': 'b1', 'b2': {'c1': 'c1'}}}
    dut = get_value_from_dictionary

    res = dut(d, 'a')
    assert res == 'a'

    res = dut(d, 'b.b1')
    assert res == 'b1'

    res = dut(d, 'b.b2.c1')
    assert res == 'c1'

    res = dut(d, 'b.b2')
    assert isinstance(res, dict)

    res = dut(d, 'b.b3', 'gibtesnicht')
    assert res == 'gibtesnicht'

    res = dut(d, 'b|b2|c1', sep='|')
    assert res == 'c1'


def test_merge_dicts():
    d1 = {'a': 1, 'b': 2}
    d2 = {'b': 99, 'c': 3}

    res = merge_dicts(d1, d2)

    assert 'a' in res and 'b' in res and 'c' in res
    assert res['a'] == 1
    assert res['b'] == 99
    assert res['c'] == 3


def test_safe_list_get():
    l = ['a', 'b', 'c']

    assert safe_list_get(l, 0) == 'a'
    assert safe_list_get(l, 1) == 'b'
    assert safe_list_get(l, 2) == 'c'
    assert safe_list_get(l, 3) is None
    assert safe_list_get(l, 3, 'd') == 'd'


def test_chunk_list():
    assert chunk_list([], 65) == []
    assert chunk_list(['a'], 64) == [['a']]
    assert chunk_list(['a', 'b', 'c'], 1) == [['a'], ['b'], ['c']]
    assert chunk_list(['a', 'b', 'c'], 2) == [['a', 'b'], ['c']]
    assert chunk_list(['a', 'b', 'c'], 3) == [['a', 'b', 'c']]
