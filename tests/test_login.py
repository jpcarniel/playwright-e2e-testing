import re

from playwright.sync_api import expect


class TestLogin:
    def test_should_login_with_valid_credentials(self, login_page, page):
        login_page.visit()
        login_page.login("tomsmith", "SuperSecretPassword!")

        expect(page).to_have_url(re.compile(r"/secure"))
        expect(login_page.get_flash_message()).to_contain_text(
            "You logged into a secure area!"
        )

    def test_should_display_error_for_invalid_username(self, login_page):
        login_page.visit()
        login_page.login("invaliduser", "SuperSecretPassword!")

        expect(login_page.get_flash_message()).to_contain_text(
            "Your username is invalid!"
        )

    def test_should_display_error_for_invalid_password(self, login_page):
        login_page.visit()
        login_page.login("tomsmith", "wrongpassword")

        expect(login_page.get_flash_message()).to_contain_text(
            "Your password is invalid!"
        )

    def test_should_display_error_for_empty_fields(self, login_page):
        login_page.visit()
        login_page.submit()

        expect(login_page.get_flash_message()).to_contain_text(
            "Your username is invalid!"
        )

    def test_should_logout_after_successful_login(self, login_page, page):
        login_page.visit()
        login_page.login("tomsmith", "SuperSecretPassword!")
        login_page.logout()

        expect(page).to_have_url(re.compile(r"/login"))
        expect(login_page.get_flash_message()).to_contain_text(
            "You logged out of the secure area!"
        )
