import re

from playwright.sync_api import expect


class TestLogin:
    """Tests for the Login page."""

    def test_should_login_with_valid_credentials(self, login_page, page):
        login_page.visit()
        login_page.login("tomsmith", "SuperSecretPassword!")

        # Verify redirect to secure area
        expect(page).to_have_url(re.compile(r"/secure"))

        # Verify success message is displayed
        expect(login_page.get_flash_message()).to_contain_text(
            "You logged into a secure area!"
        )

    def test_should_display_error_for_invalid_username(self, login_page):
        login_page.visit()
        login_page.login("invaliduser", "SuperSecretPassword!")

        # Verify error message is displayed
        expect(login_page.get_flash_message()).to_contain_text(
            "Your username is invalid!"
        )

    def test_should_display_error_for_invalid_password(self, login_page):
        login_page.visit()
        login_page.login("tomsmith", "wrongpassword")

        # Verify error message is displayed
        expect(login_page.get_flash_message()).to_contain_text(
            "Your password is invalid!"
        )

    def test_should_display_error_for_empty_fields(self, login_page):
        login_page.visit()
        login_page.submit()

        # Verify error message is displayed
        expect(login_page.get_flash_message()).to_contain_text(
            "Your username is invalid!"
        )

    def test_should_logout_after_successful_login(self, login_page, page):
        login_page.visit()
        login_page.login("tomsmith", "SuperSecretPassword!")

        # Click logout
        login_page.logout()

        # Verify redirect back to login page
        expect(page).to_have_url(re.compile(r"/login"))

        # Verify logout success message
        expect(login_page.get_flash_message()).to_contain_text(
            "You logged out of the secure area!"
        )
