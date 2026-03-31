import pytest


@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[AUTOUSE] fixture is running")


@pytest.fixture(scope="session")
def settings():
    print("[SESSION] fixture is running]")


@pytest.fixture(scope="class")
def user():
    print("[CLASS] fixture is running")


@pytest.fixture
def browser():
    print("[FUNCTION] fixture is running")


class TestUserFlow:
    def test_user(self, settings, user, browser):
        ...

    def test_user_browser(self, settings, user, browser):
        ...