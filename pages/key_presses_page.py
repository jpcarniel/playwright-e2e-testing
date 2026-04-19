class KeyPressesPage:
    INPUT_TARGET = "#target"
    RESULT = "#result"

    def __init__(self, page):
        self.page = page

    def visit(self):
        self.page.goto("/key_presses")

    def press_key(self, key):
        self.page.press(self.INPUT_TARGET, key)

    def get_result(self):
        return self.page.locator(self.RESULT)
