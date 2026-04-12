import random

import pytest

PLATFORM = "Windows"

# reruns 3 times with 2 sec delay
@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_reruns(page):
    assert random.choice([True, False])


@pytest.mark.flaky(reruns=3, reruns_delay=2)
class TestReruns:
    def test_rerun_1(self, page):
        assert random.choice([True, False])

    def test_rerun_2(self, page):
        assert random.choice([True, False])


@pytest.mark.flaky(reruns=3, reruns_delay=2, condition=PLATFORM == "Windows")
@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_rerun_condition(self, page):
    assert random.choice([True, False])