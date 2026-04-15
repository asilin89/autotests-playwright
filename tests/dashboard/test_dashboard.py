from pages.dashboard.dashboard_page import DashboardPage
import pytest
import allure
from tools.allure.tags import AllureTags
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory

@pytest.mark.dashboard
@pytest.mark.regression
@allure.tag(AllureTags.DASHBOARD, AllureTags.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.DASHBOARD)
@allure.story(AllureStory.DASHBOARD)
class TestDashboard:
    @allure.title('Check dashboard page is displaying')
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#dashboard")
        dashboard_page_with_state.navbar.check_visible("username1")
        dashboard_page_with_state.check_dashboard_title_visible()
        dashboard_page_with_state.check_scores_widget_visible()
        dashboard_page_with_state.check_student_widget_visible()
        dashboard_page_with_state.check_courses_widget_visible()
        dashboard_page_with_state.check_activities_widget_visible()
