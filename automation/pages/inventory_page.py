from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        # 选择器字符串
        self.add_to_cart_buttons = "button[data-test^=add-to-cart]"
        self.cart_icon = ".shopping_cart_link"
        self.sort_dropdown = ".product_sort_container"

    def add_first_item_to_cart(self):
        # 使用 self.page.locator() 将字符串转为定位器
        self.page.locator(self.add_to_cart_buttons).first.click()

    def get_cart_count(self):
        # 获取购物车图标上的数字
        count = self.page.text_content(self.cart_icon)
        return count.strip() if count else "0"