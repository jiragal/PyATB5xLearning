import pytest


@pytest.mark.regression
def test_method3():
    print("test1")
    assert 1+1 == 2

@pytest.mark.smoke
def test_method4():
    print('test2')
    assert 1-1 == 2


