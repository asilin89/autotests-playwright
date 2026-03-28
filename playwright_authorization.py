from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page =  browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#auth/login")

    #email_input =page.locator('//div[@data-testid ="login-form-email-input"]//div//input')
    email_input = page.get_by_test_id("login-form-email-input").locator("input")
    email_input.fill('user.name@mail.com')

    #password_input = page.locator('//div[@data-testid ="login-form-password-input"]//div//input')
    password_input = page.get_by_test_id("login-form-password-input").locator("input")
    password_input.fill('password')

    #login_btn = page.locator('//button[@data-testid = "login-page-login-button"]')
    login_btn = page.get_by_test_id("login-page-login-button")
    login_btn.click()

    #error_msg = page.locator('//div[@data-testid = "login-page-wrong-email-or-password-alert"]')
    error_msg = page.get_by_test_id("login-page-wrong-email-or-password-alert")
    expect(error_msg).to_be_visible()
    expect(error_msg).to_have_text("Wrong email or password")


    #page.wait_for_timeout(3000) # do not use in real project