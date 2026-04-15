from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
import pytest
import allure
from tools.allure.tags import AllureTags
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTags.COURSES, AllureTags.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
class TestCourses:
    @allure.title('Create course')
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

        create_course_page.check_visible_create_course_title()
        create_course_page.check_disabled_create_course_button()
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.check_visible_create_course_form(
            title="", max_score="0", min_score="0", description="", estimated_time=""
        )

        create_course_page.check_visible_exercises_title()
        create_course_page.check_visible_create_exercise_button()
        create_course_page.check_visible_exercises_empty_view()

        create_course_page.image_upload_widget.upload_preview_image("./testdata/files/image.png")
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.fill_create_course_form(
            title="Tiger", max_score="100", min_score="5", description="Tiger Trade", estimated_time="1 week"
        )
        create_course_page.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0, title="Tiger", max_score="100", min_score="5", estimated_time="1 week"
        )

    @allure.title('Check displaying of empty courses list')
    @allure.severity(Severity.NORMAL)
    def test_empty_course_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/")

        courses_list_page.navbar.check_visible('username1')
        courses_list_page.sidebar.check_visible()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()


