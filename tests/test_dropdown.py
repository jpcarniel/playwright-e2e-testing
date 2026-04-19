from playwright.sync_api import expect


class TestDropdown:
    def test_should_have_no_option_selected_by_default(self, dropdown_page):
        dropdown_page.visit()

        expect(dropdown_page.get_dropdown()).to_have_value("")

    def test_should_select_option_1(self, dropdown_page):
        dropdown_page.visit()
        dropdown_page.select_option("1")

        expect(dropdown_page.get_dropdown()).to_have_value("1")

    def test_should_select_option_2(self, dropdown_page):
        dropdown_page.visit()
        dropdown_page.select_option("2")

        expect(dropdown_page.get_dropdown()).to_have_value("2")

    def test_should_change_selection_from_option_1_to_option_2(self, dropdown_page):
        dropdown_page.visit()
        dropdown_page.select_option("1")
        expect(dropdown_page.get_dropdown()).to_have_value("1")

        dropdown_page.select_option("2")
        expect(dropdown_page.get_dropdown()).to_have_value("2")
