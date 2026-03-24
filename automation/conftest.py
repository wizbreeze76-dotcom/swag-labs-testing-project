import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        # headless=False 能看到浏览器操作过程，slow_mo=500 让动作慢一点方便观察
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()