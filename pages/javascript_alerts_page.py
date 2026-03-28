# Page Object for the JavaScript Alerts page (/javascript_alerts)


class JavaScriptAlertsPage:
    ALERT_BUTTON = 'button:text("Click for JS Alert")'
    CONFIRM_BUTTON = 'button:text("Click for JS Confirm")'
    PROMPT_BUTTON = 'button:text("Click for JS Prompt")'
    RESULT = "#result"

    def __init__(self, page):
        self.page = page

    def visit(self):
        self.page.goto("/javascript_alerts")

    def trigger_alert(self):
        """Click the JS Alert button."""
        self.page.click(self.ALERT_BUTTON)

    def trigger_confirm(self):
        """Click the JS Confirm button."""
        self.page.click(self.CONFIRM_BUTTON)

    def trigger_prompt(self):
        """Click the JS Prompt button."""
        self.page.click(self.PROMPT_BUTTON)

    def get_result(self):
        """Get the result text locator for assertions."""
        return self.page.locator(self.RESULT)
