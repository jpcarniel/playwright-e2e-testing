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
        self.page.click(self.ALERT_BUTTON)

    def trigger_confirm(self):
        self.page.click(self.CONFIRM_BUTTON)

    def trigger_prompt(self):
        self.page.click(self.PROMPT_BUTTON)

    def get_result(self):
        return self.page.locator(self.RESULT)
