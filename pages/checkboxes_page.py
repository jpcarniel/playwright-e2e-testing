class CheckboxesPage:
    CHECKBOXES = '#checkboxes input[type="checkbox"]'

    def __init__(self, page):
        self.page = page

    def visit(self):
        self.page.goto("/checkboxes")

    def get_checkbox(self, index):
        return self.page.locator(self.CHECKBOXES).nth(index)

    def toggle(self, index):
        self.get_checkbox(index).click()
