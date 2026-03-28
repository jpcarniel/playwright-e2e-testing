import pytest

from pages.checkboxes_page import CheckboxesPage
from pages.drag_and_drop_page import DragAndDropPage
from pages.dropdown_page import DropdownPage
from pages.dynamic_loading_page import DynamicLoadingPage
from pages.file_upload_page import FileUploadPage
from pages.hovers_page import HoversPage
from pages.javascript_alerts_page import JavaScriptAlertsPage
from pages.key_presses_page import KeyPressesPage
from pages.login_page import LoginPage


@pytest.fixture()
def checkboxes_page(page):
    return CheckboxesPage(page)


@pytest.fixture()
def drag_and_drop_page(page):
    return DragAndDropPage(page)


@pytest.fixture()
def dropdown_page(page):
    return DropdownPage(page)


@pytest.fixture()
def dynamic_loading_page(page):
    return DynamicLoadingPage(page)


@pytest.fixture()
def file_upload_page(page):
    return FileUploadPage(page)


@pytest.fixture()
def hovers_page(page):
    return HoversPage(page)


@pytest.fixture()
def javascript_alerts_page(page):
    return JavaScriptAlertsPage(page)


@pytest.fixture()
def key_presses_page(page):
    return KeyPressesPage(page)


@pytest.fixture()
def login_page(page):
    return LoginPage(page)
