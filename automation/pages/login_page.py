from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = "#user-name"
        self.password = "#password"
        self.login_btn = "#login-button"
        self.error = "[data-test=error]"

    def login(self, user, pwd):
        self.page.fill(self.username, user)
        self.page.fill(self.password, pwd)
        self.page.click(self.login_btn)

    def get_error(self):
        return self.page.text_content(self.error)