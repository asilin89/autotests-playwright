from playwright.sync_api import Page, expect
import pytest
import allure
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.tags import AllureTags
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity


@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTags.REGRESSION, AllureTags.REGISTRATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
class TestRegistration:
    @allure.title('User registration with email, username and password')
    @allure.severity(Severity.CRITICAL)
    def test_successful_registration(self, dashboard_page: DashboardPage, register_page: RegistrationPage):
        register_page.visit(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
        )
        register_page.registration_form.fill(
            email="email@example.com",
            username="username1",
            password="password1"
        )
        register_page.click_registration_button()

        # The code line blow needs to be implemented
        # dashboard_page.dashboard_toolbar_view.check_visible()

                # dashboard_title = chromium_page.get_by_test_id("dashboard-toolbar-title-text")
                # expect(dashboard_title).to_be_visible()


