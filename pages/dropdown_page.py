# Page Object for the Dropdown page (/dropdown)


class DropdownPage:
    DROPDOWN = "#dropdown"

    def __init__(self, page):
        """Initialize with a Playwright page instance."""
        self.page = page

    def visit(self):
        """Navigate to the Dropdown page."""
        self.page.goto("/dropdown")

    def select_option(self, value):
        """Select an option by its value."""
        self.page.select_option(self.DROPDOWN, value)

    def get_dropdown(self):
        """Get the dropdown locator for assertions."""
        return self.page.locator(self.DROPDOWN)
