from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import EmailStr, FilePath, HttpUrl, DirectoryPath, BaseModel
from enum import Enum
from typing import Self


class Browser(str, Enum):
    WEBKIT = 'webkit'
    CHROMIUM = 'chromium'
    FIREFOX = 'firefox'


class TestUser(BaseModel):
    email: EmailStr
    username: str
    password: str


class TestData(BaseModel):
    image_png_file: FilePath


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter=".",
    )

    app_url: HttpUrl
    headless: bool
    browsers: list[Browser]
    test_user: TestUser
    test_data: TestData
    video_dir: DirectoryPath
    tracing_dir: DirectoryPath
    browser_state_file: FilePath


    @classmethod
    def initialize(cls) -> Self:
        """
        This function creates following folders in case they don't exist
        :return:
        """
        videos_dir = DirectoryPath("./videos")
        tracing_dir = DirectoryPath("./tracing")
        browser_state_file = FilePath("browser-state.json")

        # If dir/file exists do not create it
        videos_dir.mkdir(exist_ok=True)
        tracing_dir.mkdir(exist_ok=True)
        browser_state_file.touch(exist_ok=True)

        return Settings(
            video_dir=videos_dir,
            tracing_dir=tracing_dir,
            browser_state_file=browser_state_file
        )


settings = Settings.initialize()

