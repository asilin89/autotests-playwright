import pytest

from pages.authentication.login_page import LoginPage


@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize(
        "email, password",
        [
            ("user.name@gmail.com", "password"),
            ("user.name@gmail.com", " "),
            (" ", "password")
        ]
)
def test_wrong_email_or_password_auth(login_page: LoginPage, email: str, password: str):

        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#auth/login")
        login_page.fill_login_form(email, password)
        login_page.click_login_button()
        login_page.check_visible_wrong_email_or_password_alert()



        # chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#auth/login")
        #
        # # email_input =page.locator('//div[@data-testid ="login-form-email-input"]//div//input')
        # email_input = chromium_page.get_by_test_id("login-form-email-input").locator("input")
        # email_input.fill('user.name@mail.com')
        #
        # # password_input = page.locator('//div[@data-testid ="login-form-password-input"]//div//input')
        # password_input = chromium_page.get_by_test_id("login-form-password-input").locator("input")
        # password_input.fill('password')
        #
        # # login_btn = page.locator('//button[@data-testid = "login-page-login-button"]')
        # login_btn = chromium_page.get_by_test_id("login-page-login-button")
        # login_btn.click()
        #
        # # error_msg = page.locator('//div[@data-testid = "login-page-wrong-email-or-password-alert"]')
        # error_msg = chromium_page.get_by_test_id("login-page-wrong-email-or-password-alert")
        # expect(error_msg).to_be_visible()
        # expect(error_msg).to_have_text("Wrong email or password")