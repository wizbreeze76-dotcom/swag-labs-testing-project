import pytest
# 修正：使用完整路径导入
from automation.pages.login_page import LoginPage

def test_successful_login(page):
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    # 验证是否跳转到了商品页
    assert "inventory.html" in page.url

def test_locked_user(page):
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login("locked_out_user", "secret_sauce")
    error_message = login_page.get_error()
    assert error_message is not None
    assert "Sorry, this user has been locked out" in error_message