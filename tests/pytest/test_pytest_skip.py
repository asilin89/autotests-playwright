import pytest


OS = 'Linux'
SYS_VERSION = 'v1.2.0'

@pytest.mark.skip(reason="Feature in development.")
def test_feature_in_dev():
    ...


@pytest.mark.skipif(
    SYS_VERSION == 'v1.3.0',
    reason="Test cannot be run on version 1.2.0."
)
def test_system_version_valid():
    ...


@pytest.mark.skipif(
    SYS_VERSION == 'v1.2.0',
    reason="Test cannot be run on version 1.2.0."
)
def test_system_version_invalid():
    ...
