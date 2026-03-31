from playwright.sync_api import sync_playwright, Page, expect
import pytest


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(chromium_page: Page):

        # Go to login page
        chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        # Find email input and fill it out
        email_input = chromium_page.get_by_test_id("registration-form-email-input").locator("input")
        email_input.fill("email@example.com")

        # Find username input and fill it out
        username_input = chromium_page.get_by_test_id("registration-form-username-input").locator("input")
        username_input.fill("username1")

        # Find password input and fill it out
        password_input = chromium_page.get_by_test_id("registration-form-password-input").locator("input")
        password_input.fill("password1")

        # Find Register button and click on it
        registration_button = chromium_page.get_by_test_id("registration-page-registration-button")
        registration_button.click()

        dashboard_title = chromium_page.get_by_test_id("dashboard-toolbar-title-text")
        expect(dashboard_title).to_be_visible()

    #     # After login we store localStorage data into "browser-state.json" file
    #     context.storage_state(path="browser-state.json")
    #
    # # Create new session
    # # Create context which uses "browser-state.json" data to authenticate
    # # Goes directly to dashboard page
    # with sync_playwright() as playwright:
    #     browser = playwright.chromium.launch(headless=False)
    #     context = browser.new_context(storage_state="browser-state.json")
    #     page = context.new_page()
    #
    #     page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
    #
    #     page.wait_for_timeout(3000)
