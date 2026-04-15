from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.input import Input
import allure


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.get_by_test_id("login-form-email-input").locator("input")
        self.password_input = page.get_by_test_id("login-form-password-input").locator("input")


    @allure.step('Fill login form')
    def fill(self, email: str, password: str):
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)


    @allure.step('Check login form is visible')
    def check_visible(self, email: str, password: str):
        expect(self.email_input).to_be_visible()
        expect(self.email_input).to_have_value(email)

        expect(self.password_input).to_be_visible()
        expect(self.password_input).to_have_value(password)