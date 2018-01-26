from common.base import singleton


def test_singleton_simple():
    @singleton
    class ASingleton:
        pass

    a = ASingleton()
    b = ASingleton()

    assert a.__class__.__name__ == 'ASingleton'
    assert a is b


def test_singleton_with_args():
    @singleton
    class BSingleton:
        def __init__(self, x):
            self.x = x

    @singleton
    class ASingleton:
        pass

    a = ASingleton()

    b = BSingleton(11)
    # BSingleton is already instantiated and x is set to 11, no more initialization
    c = BSingleton(22)

    assert b is c
    assert b.x == 11
    assert c.x == 11
    assert b.x == c.x
    assert a is not b

    b.x = 22
    assert c.x == 22
