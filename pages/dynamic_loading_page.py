class DynamicLoadingPage:
    START_BUTTON = "#start button"
    LOADED_TEXT = "#finish h4"
    LOADING_INDICATOR = "#loading"

    def __init__(self, page):
        self.page = page

    def visit_example(self, example_number):
        self.page.goto(f"/dynamic_loading/{example_number}")

    def click_start(self):
        self.page.click(self.START_BUTTON)

    def get_loaded_text(self):
        return self.page.locator(self.LOADED_TEXT)
