from playwright.sync_api import Page, Route



def mock_static_recourses(page: Page):
    page.route("**/*.{ico, jpg, png, svg, webp, mp3m mp4, woff, woff2}", lambda route: route.abort())