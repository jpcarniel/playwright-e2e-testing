from playwright.sync_api import expect


class TestCheckboxes:
    """Tests for the Checkboxes page."""

    def test_should_have_correct_initial_states(self, checkboxes_page):
        checkboxes_page.visit()

        # First checkbox starts unchecked
        expect(checkboxes_page.get_checkbox(0)).not_to_be_checked()

        # Second checkbox starts checked
        expect(checkboxes_page.get_checkbox(1)).to_be_checked()

    def test_should_check_the_first_checkbox(self, checkboxes_page):
        checkboxes_page.visit()
        checkboxes_page.toggle(0)

        # First checkbox should now be checked
        expect(checkboxes_page.get_checkbox(0)).to_be_checked()

    def test_should_uncheck_the_second_checkbox(self, checkboxes_page):
        checkboxes_page.visit()
        checkboxes_page.toggle(1)

        # Second checkbox should now be unchecked
        expect(checkboxes_page.get_checkbox(1)).not_to_be_checked()

    def test_should_toggle_both_checkboxes(self, checkboxes_page):
        checkboxes_page.visit()
        checkboxes_page.toggle(0)
        checkboxes_page.toggle(1)

        # States should be inverted
        expect(checkboxes_page.get_checkbox(0)).to_be_checked()
        expect(checkboxes_page.get_checkbox(1)).not_to_be_checked()
