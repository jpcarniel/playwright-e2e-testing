from playwright.sync_api import expect


class TestDynamicLoading:
    def test_should_show_hidden_element_after_loading_example_1(self, dynamic_loading_page):
        dynamic_loading_page.visit_example(1)
        dynamic_loading_page.click_start()

        expect(dynamic_loading_page.get_loaded_text()).to_be_visible(timeout=10000)
        expect(dynamic_loading_page.get_loaded_text()).to_have_text("Hello World!")

    def test_should_render_element_after_loading_example_2(self, dynamic_loading_page):
        dynamic_loading_page.visit_example(2)
        dynamic_loading_page.click_start()

        expect(dynamic_loading_page.get_loaded_text()).to_be_visible(timeout=10000)
        expect(dynamic_loading_page.get_loaded_text()).to_have_text("Hello World!")
