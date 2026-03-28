import os

from playwright.sync_api import expect


FIXTURES_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "fixtures")


class TestFileUpload:
    """Tests for the File Upload page."""

    def test_should_upload_a_file_successfully(self, file_upload_page):
        file_upload_page.visit()

        # Use the test fixture file
        file_path = os.path.join(FIXTURES_DIR, "test-upload.txt")
        file_upload_page.upload_file(file_path)

        # Verify the uploaded file name is displayed
        expect(file_upload_page.get_uploaded_file_name()).to_have_text("test-upload.txt")

    def test_should_show_error_when_submitting_without_file(self, file_upload_page, page):
        file_upload_page.visit()

        # Click submit without selecting a file
        page.click(file_upload_page.SUBMIT_BUTTON)

        # The page shows "Internal Server Error"
        expect(page.locator("body")).to_contain_text("Internal Server Error")
