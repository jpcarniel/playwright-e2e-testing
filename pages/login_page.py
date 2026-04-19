class LoginPage:
    USERNAME_INPUT = "#username"
    PASSWORD_INPUT = "#password"
    SUBMIT_BUTTON = 'button[type="submit"]'
    FLASH_MESSAGE = "#flash"
    LOGOUT_BUTTON = 'a[href="/logout"]'

    def __init__(self, page):
        self.page = page

    def visit(self):
        self.page.goto("/login")

    def fill_username(self, username):
        self.page.fill(self.USERNAME_INPUT, username)

    def fill_password(self, password):
        self.page.fill(self.PASSWORD_INPUT, password)

    def submit(self):
        self.page.click(self.SUBMIT_BUTTON)

    def login(self, username, password):
        self.fill_username(username)
        self.fill_password(password)
        self.submit()

    def get_flash_message(self):
        return self.page.locator(self.FLASH_MESSAGE)

    def logout(self):
        self.page.click(self.LOGOUT_BUTTON)
