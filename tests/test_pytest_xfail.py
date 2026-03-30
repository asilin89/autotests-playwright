import pytest


@pytest.mark.xfail(reason="test fails due to knows bug")
def test_with_bug():
    assert 1 == 2 # Test will be completed with XFAIL status


@pytest.mark.xfail(reason="bug fixed but xfail marker is still applied")
def test_without_bug():
    assert 2 + 2 == 4 # Test will be completed with XPASS status