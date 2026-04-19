class FileUploadPage:
    FILE_INPUT = "#file-upload"
    SUBMIT_BUTTON = "#file-submit"
    UPLOADED_FILE_NAME = "#uploaded-files"

    def __init__(self, page):
        self.page = page

    def visit(self):
        self.page.goto("/upload")

    def upload_file(self, file_path):
        self.page.set_input_files(self.FILE_INPUT, file_path)
        self.page.click(self.SUBMIT_BUTTON)

    def get_uploaded_file_name(self):
        return self.page.locator(self.UPLOADED_FILE_NAME)
