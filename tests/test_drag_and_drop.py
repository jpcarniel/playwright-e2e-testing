from playwright.sync_api import expect


class TestDragAndDrop:
    """Tests for the Drag and Drop page."""

    def test_should_display_correct_initial_column_headers(self, drag_and_drop_page):
        drag_and_drop_page.visit()

        expect(drag_and_drop_page.get_column_a_header()).to_have_text("A")
        expect(drag_and_drop_page.get_column_b_header()).to_have_text("B")

    def test_should_swap_headers_when_dragging_a_to_b(self, drag_and_drop_page):
        drag_and_drop_page.visit()
        drag_and_drop_page.drag_a_to_b()

        # After drag, headers should be swapped
        expect(drag_and_drop_page.get_column_a_header()).to_have_text("B")
        expect(drag_and_drop_page.get_column_b_header()).to_have_text("A")

    def test_should_restore_headers_when_dragging_back(self, drag_and_drop_page):
        drag_and_drop_page.visit()

        # Drag A to B
        drag_and_drop_page.drag_a_to_b()

        # Drag B back to A
        drag_and_drop_page.drag_b_to_a()

        # Headers should be back to original positions
        expect(drag_and_drop_page.get_column_a_header()).to_have_text("A")
        expect(drag_and_drop_page.get_column_b_header()).to_have_text("B")
