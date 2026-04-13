# Page Object for the Login page (/login)


class LoginPage:
    USERNAME_INPUT = "#username"
    PASSWORD_INPUT = "#password"
    SUBMIT_BUTTON = 'button[type="submit"]'
    FLASH_MESSAGE = "#flash"
    LOGOUT_BUTTON = 'a[href="/logout"]'

    def __init__(self, page):
        """Initialize with a Playwright page instance."""
        self.page = page

    def visit(self):
        """Navigate to the Login page."""
        self.page.goto("/login")

    def fill_username(self, username):
        """Fill the username field."""
        self.page.fill(self.USERNAME_INPUT, username)

    def fill_password(self, password):
        """Fill the password field."""
        self.page.fill(self.PASSWORD_INPUT, password)

    def submit(self):
        """Click the login button."""
        self.page.click(self.SUBMIT_BUTTON)

    def login(self, username, password):
        """Perform a complete login (fill fields + submit)."""
        self.fill_username(username)
        self.fill_password(password)
        self.submit()

    def get_flash_message(self):
        """Get the flash message locator for assertions."""
        return self.page.locator(self.FLASH_MESSAGE)

    def logout(self):
        """Click the logout button."""
        self.page.click(self.LOGOUT_BUTTON)
