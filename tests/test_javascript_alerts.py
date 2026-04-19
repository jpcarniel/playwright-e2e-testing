from playwright.sync_api import expect


class TestJavaScriptAlerts:
    def test_should_accept_js_alert(self, javascript_alerts_page, page):
        javascript_alerts_page.visit()

        page.on("dialog", lambda dialog: dialog.accept())

        javascript_alerts_page.trigger_alert()

        expect(javascript_alerts_page.get_result()).to_have_text(
            "You successfully clicked an alert"
        )

    def test_should_accept_js_confirm(self, javascript_alerts_page, page):
        javascript_alerts_page.visit()

        page.on("dialog", lambda dialog: dialog.accept())

        javascript_alerts_page.trigger_confirm()

        expect(javascript_alerts_page.get_result()).to_have_text("You clicked: Ok")

    def test_should_dismiss_js_confirm(self, javascript_alerts_page, page):
        javascript_alerts_page.visit()

        page.on("dialog", lambda dialog: dialog.dismiss())

        javascript_alerts_page.trigger_confirm()

        expect(javascript_alerts_page.get_result()).to_have_text("You clicked: Cancel")

    def test_should_enter_text_in_js_prompt_and_accept(self, javascript_alerts_page, page):
        javascript_alerts_page.visit()

        page.on("dialog", lambda dialog: dialog.accept("Hello from Playwright"))

        javascript_alerts_page.trigger_prompt()

        expect(javascript_alerts_page.get_result()).to_have_text(
            "You entered: Hello from Playwright"
        )

    def test_should_dismiss_js_prompt_without_text(self, javascript_alerts_page, page):
        javascript_alerts_page.visit()

        page.on("dialog", lambda dialog: dialog.dismiss())

        javascript_alerts_page.trigger_prompt()

        expect(javascript_alerts_page.get_result()).to_have_text("You entered: null")
