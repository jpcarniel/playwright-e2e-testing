class DropdownPage:
    DROPDOWN = "#dropdown"

    def __init__(self, page):
        self.page = page

    def visit(self):
        self.page.goto("/dropdown")

    def select_option(self, value):
        self.page.select_option(self.DROPDOWN, value)

    def get_dropdown(self):
        return self.page.locator(self.DROPDOWN)
