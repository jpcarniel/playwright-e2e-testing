# Page Object for the Drag and Drop page (/drag_and_drop)
# Note: HTML5 native drag-and-drop requires a JavaScript workaround
# because Playwright's built-in drag_to() doesn't trigger HTML5 drag events


class DragAndDropPage:
    COLUMN_A = "#column-a"
    COLUMN_B = "#column-b"

    def __init__(self, page):
        """Initialize with a Playwright page instance."""
        self.page = page

    def visit(self):
        """Navigate to the Drag and Drop page."""
        self.page.goto("/drag_and_drop")

    def get_column_a_header(self):
        """Get the header text of column A."""
        return self.page.locator(f"{self.COLUMN_A} header")

    def get_column_b_header(self):
        """Get the header text of column B."""
        return self.page.locator(f"{self.COLUMN_B} header")

    def drag_a_to_b(self):
        """Simulate drag from column A to column B using JavaScript.
        This workaround dispatches native HTML5 drag events."""
        self.page.evaluate("""() => {
            const source = document.querySelector('#column-a');
            const target = document.querySelector('#column-b');
            const dataTransfer = new DataTransfer();
            source.dispatchEvent(new DragEvent('dragstart', { dataTransfer, bubbles: true }));
            target.dispatchEvent(new DragEvent('dragover', { dataTransfer, bubbles: true }));
            target.dispatchEvent(new DragEvent('drop', { dataTransfer, bubbles: true }));
            source.dispatchEvent(new DragEvent('dragend', { dataTransfer, bubbles: true }));
        }""")

    def drag_b_to_a(self):
        """Simulate drag from column B to column A using JavaScript."""
        self.page.evaluate("""() => {
            const source = document.querySelector('#column-b');
            const target = document.querySelector('#column-a');
            const dataTransfer = new DataTransfer();
            source.dispatchEvent(new DragEvent('dragstart', { dataTransfer, bubbles: true }));
            target.dispatchEvent(new DragEvent('dragover', { dataTransfer, bubbles: true }));
            target.dispatchEvent(new DragEvent('drop', { dataTransfer, bubbles: true }));
            source.dispatchEvent(new DragEvent('dragend', { dataTransfer, bubbles: true }));
        }""")
