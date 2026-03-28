# Page Object for the Key Presses page (/key_presses)


class KeyPressesPage:
    INPUT_TARGET = "#target"
    RESULT = "#result"

    def __init__(self, page):
        self.page = page

    def visit(self):
        self.page.goto("/key_presses")

    def press_key(self, key):
        """Press a specific key on the input field."""
        self.page.press(self.INPUT_TARGET, key)

    def get_result(self):
        """Get the result locator for assertions."""
        return self.page.locator(self.RESULT)
