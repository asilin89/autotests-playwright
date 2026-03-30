from playwright.sync_api import sync_playwright


def test_successful_registration():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)

        # Creating browser context (it's like Client() set up in httpx). Can be used to store auth data (tokens, etc.)
        context = browser.new_context()
        page = context.new_page()

        # Go to login page
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        # Find email input and fill it out
        email_input = page.get_by_test_id("registration-form-email-input").locator("input")
        email_input.fill("email@example.com")

        # Find username input and fill it out
        username_input = page.get_by_test_id("registration-form-username-input").locator("input")
        username_input.fill("username1")

        # Find password input and fill it out
        password_input = page.get_by_test_id("registration-form-password-input").locator("input")
        password_input.fill("password1")

        # Find Register button and click on it
        registration_button = page.get_by_test_id("registration-page-registration-button")
        registration_button.click()

        # After login we store localStorage data into "browser-state.json" file
        context.storage_state(path="browser-state.json")

    # Create new session
    # Create context which uses "browser-state.json" data to authenticate
    # Goes directly to dashboard page
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")

        page.wait_for_timeout(3000)
