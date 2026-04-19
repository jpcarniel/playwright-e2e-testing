class DragAndDropPage:
    COLUMN_A = "#column-a"
    COLUMN_B = "#column-b"

    def __init__(self, page):
        self.page = page

    def visit(self):
        self.page.goto("/drag_and_drop")

    def get_column_a_header(self):
        return self.page.locator(f"{self.COLUMN_A} header")

    def get_column_b_header(self):
        return self.page.locator(f"{self.COLUMN_B} header")

    # Playwright's drag_to() doesn't fire HTML5 drag events on this page; dispatch them manually.
    def drag_a_to_b(self):
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
        self.page.evaluate("""() => {
            const source = document.querySelector('#column-b');
            const target = document.querySelector('#column-a');
            const dataTransfer = new DataTransfer();
            source.dispatchEvent(new DragEvent('dragstart', { dataTransfer, bubbles: true }));
            target.dispatchEvent(new DragEvent('dragover', { dataTransfer, bubbles: true }));
            target.dispatchEvent(new DragEvent('drop', { dataTransfer, bubbles: true }));
            source.dispatchEvent(new DragEvent('dragend', { dataTransfer, bubbles: true }));
        }""")
