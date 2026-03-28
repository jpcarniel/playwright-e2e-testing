# Page Object for the Dynamic Loading pages (/dynamic_loading)


class DynamicLoadingPage:
    START_BUTTON = "#start button"
    LOADED_TEXT = "#finish h4"
    LOADING_INDICATOR = "#loading"

    def __init__(self, page):
        self.page = page

    def visit_example(self, example_number):
        """Navigate to a specific dynamic loading example (1 or 2)."""
        self.page.goto(f"/dynamic_loading/{example_number}")

    def click_start(self):
        """Click the start button to begin loading."""
        self.page.click(self.START_BUTTON)

    def get_loaded_text(self):
        """Get the loaded text locator (waits for visibility automatically)."""
        return self.page.locator(self.LOADED_TEXT)
