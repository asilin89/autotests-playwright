import pytest
from _pytest.fixtures import SubRequest


# one param case
@pytest.mark.parametrize('number', [1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0


# 2 params case
@pytest.mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 9)])
def test_several_nums(number: int, expected: int):
    assert number ** 2 == expected


# Pairwise case(when we need to multiply one param on another one)
@pytest.mark.parametrize('os', ['mac', 'linux', 'windows'])
@pytest.mark.parametrize('browser', ['chromium', 'webkit', 'firefox'])
def test_multiplication_os_browser(os: str, browser: str):
    assert len(os + browser) > 0


# Fixture parametrization
@pytest.fixture(params=['chromium', 'webkit', 'firefox'])
def browser(request: SubRequest):
    return request.param


# Takes params from browser fixture and run test for each of them ('chromium', 'webkit', 'firefox')
def test_open_browser(browser: str):
    print("Running test on browser:", browser)


@pytest.mark.parametrize('user', ['Alice', 'Zara'])
class TestOperations:
    @pytest.mark.parametrize('account', ['Credit Card', 'Debit Card'])
    def test_user_with_operations(self, user: str, account: str):
        print("User with operations: ", user)

    def test_user_without_operations(self, user: str):
        print("User without operations: ", user)



users = {
    '+3750000000222': 'User with funds on banking account',
    '+48009999888': 'User without funds on banking account',
    '+13139888444': 'User with transactions on banking account'
}

@pytest.mark.parametrize(
    'phone_number',
    users.keys(),
    ids=lambda phone_number: f'{phone_number}: {users[phone_number]}'
    # ['+3750000000222', '+48009999888', '+13139888444'],
    # ids=[
    #     'User with funds on banking account',
    #     'User without funds on banking account',
    #     'User with transactions on banking account'
    # ]
)
def test_identifiers(phone_number: str):
    ...