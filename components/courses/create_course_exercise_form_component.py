from components.base_component import BaseComponent
from playwright.sync_api import expect, Page

from elements.button import Button
from elements.text import Text
from elements.input import Input


class CreateCourseExerciseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.delete_exercise_button = Button(
            page, "create-course-exercise-{index}-box-toolbar-delete-exercise-button", "Delete Exercise")

        self.subtitle = Text(
            page, "create-course-exercise-{index}-box-toolbar-subtitle-text", "Exercise Subtitle"
        )

        self.title_input = Input(
            page, "create-course-exercise-form-title-{index}-input", "Title"
        )


    def click_delete_button(self, index: int):
        self.delete_exercise_button.click(nth=index)


    def check_visible(self, index: int, title: str, description: str):
        self.subtitle.check_visible(nth=index)
        self.subtitle.check_have_text(f"#{index + 1} Exercise", nth=index)

        self.title_input.check_visible(nth=index)

        description_input = self.page.get_by_test_id(
            f"create-course-exercise-form-description-{index}-input"
        )

        #expect(title_input).to_have_value(title)

        expect(description_input).to_be_visible()
        expect(description_input).to_have_value(description)


    def fill_create_exercise_form(self, index: int, title: str, description: str):
        title_input = self.page.get_by_test_id(f"create-course-exercise-form-title-{index}-input")
        description_input = self.page.get_by_test_id(f"create-course-exercise-form-description-{index}-input")

        title_input.fill(title)
        expect(title_input).to_have_value(title)

        description_input.fill(description)
        expect(description_input).to_have_value(description)