from playwright.sync_api import expect


class TestDropdown:
    """Tests for the Dropdown page."""

    def test_should_have_no_option_selected_by_default(self, dropdown_page):
        dropdown_page.visit()

        # The default option is the placeholder with no value
        expect(dropdown_page.get_dropdown()).to_have_value("")

    def test_should_select_option_1(self, dropdown_page):
        dropdown_page.visit()
        dropdown_page.select_option("1")

        # Verify Option 1 is selected
        expect(dropdown_page.get_dropdown()).to_have_value("1")

    def test_should_select_option_2(self, dropdown_page):
        dropdown_page.visit()
        dropdown_page.select_option("2")

        # Verify Option 2 is selected
        expect(dropdown_page.get_dropdown()).to_have_value("2")

    def test_should_change_selection_from_option_1_to_option_2(self, dropdown_page):
        dropdown_page.visit()
        dropdown_page.select_option("1")
        expect(dropdown_page.get_dropdown()).to_have_value("1")

        # Change to Option 2
        dropdown_page.select_option("2")
        expect(dropdown_page.get_dropdown()).to_have_value("2")
