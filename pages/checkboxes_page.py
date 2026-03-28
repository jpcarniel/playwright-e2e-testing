# Page Object for the Checkboxes page (/checkboxes)


class CheckboxesPage:
    CHECKBOXES = '#checkboxes input[type="checkbox"]'

    def __init__(self, page):
        self.page = page

    def visit(self):
        self.page.goto("/checkboxes")

    def get_checkbox(self, index):
        """Get a specific checkbox by index (0-based)."""
        return self.page.locator(self.CHECKBOXES).nth(index)

    def toggle(self, index):
        """Toggle (click) a specific checkbox."""
        self.get_checkbox(index).click()
