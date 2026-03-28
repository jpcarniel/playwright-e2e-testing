from playwright.sync_api import expect


class TestKeyPresses:
    """Tests for the Key Presses page."""

    def test_should_detect_letter_key_press(self, key_presses_page):
        key_presses_page.visit()
        key_presses_page.press_key("a")

        expect(key_presses_page.get_result()).to_have_text("You entered: A")

    def test_should_detect_space_key_press(self, key_presses_page):
        key_presses_page.visit()
        key_presses_page.press_key("Space")

        expect(key_presses_page.get_result()).to_have_text("You entered: SPACE")

    def test_should_detect_tab_key_press(self, key_presses_page):
        key_presses_page.visit()
        key_presses_page.press_key("Tab")

        expect(key_presses_page.get_result()).to_have_text("You entered: TAB")

    def test_should_detect_escape_key_press(self, key_presses_page):
        key_presses_page.visit()
        key_presses_page.press_key("Escape")

        expect(key_presses_page.get_result()).to_have_text("You entered: ESCAPE")
