from playwright.sync_api import sync_playwright, Request, Response

# Request logging
def log_request(request: Request):
    print(f"Request: {request.url}")


#Response logging
def log_response(response: Response):
    print(f"Response: {response.url}, {response.status_text}, {response.status}")


with sync_playwright() as playwright:
    #Open the browser and create new page
    browser = playwright.chromium.launch(headless=False)
    page =  browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#auth/login")

    #Create event listener/handler
    page.on("request", log_request)
    page.on("response", log_response)

    page.wait_for_timeout(2500)