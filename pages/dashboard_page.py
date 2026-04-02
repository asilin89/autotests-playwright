from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.dashboard_title = page.get_by_test_id("dashboard-toolbar-title-text")

        self.students_widget_title = page.get_by_test_id("students-widget-title-text")
        self.students_widget = page.get_by_test_id("students-bar-chart")

        self.activities_widget_title = page.get_by_test_id("activities-widget-title-text")
        self.activities_widget = page.get_by_test_id("activities-line-chart")

        self.courses_widget_title = page.get_by_test_id("courses-widget-title-text")
        self.courses_widget = page.get_by_test_id("courses-pie-chart")

        self.scores_widget_title = page.get_by_test_id("scores-widget-title-text")
        self.scores_widget = page.get_by_test_id("scores-scatter-chart")


    def check_dashboard_title_visible(self):
        expect(self.dashboard_title).to_be_visible()
        expect(self.dashboard_title).to_have_text("Dashboard")


    def check_student_widget_visible(self):
        expect(self.students_widget_title).to_be_visible()
        expect(self.students_widget_title).to_have_text("Students")
        expect(self.students_widget).to_be_visible()


    def check_activities_widget_visible(self):
        expect(self.activities_widget_title).to_be_visible()
        expect(self.activities_widget_title).to_have_text("Activities")
        expect(self.activities_widget).to_be_visible()


    def check_courses_widget_visible(self):
        expect(self.courses_widget_title).to_be_visible()
        expect(self.courses_widget_title).to_have_text("Courses")
        expect(self.courses_widget).to_be_visible()


    def check_scores_widget_visible(self):
        expect(self.scores_widget_title).to_be_visible()
        expect(self.scores_widget_title).to_have_text("Scores")
        expect(self.scores_widget).to_be_visible()

