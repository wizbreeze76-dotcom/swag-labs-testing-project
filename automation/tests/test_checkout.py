from automation.pages.login_page import LoginPage
from automation.pages.inventory_page import InventoryPage


def test_full_checkout_flow(page):
    # 1. 登录
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    # 2. 添加商品
    inventory_page = InventoryPage(page)
    inventory_page.add_first_item_to_cart()

    # 3. 点击购物车并结算
    page.click(inventory_page.cart_icon)
    page.click("#checkout")

    # 4. 填写信息
    page.fill("#first-name", "Test")
    page.fill("#last-name", "User")
    page.fill("#postal-code", "12345")
    page.click("#continue")

    # 5. 完成订单
    page.click("#finish")

    # 6. 断言结果
    complete_message = page.text_content(".complete-header")
    assert "Thank you for your order!" in complete_message