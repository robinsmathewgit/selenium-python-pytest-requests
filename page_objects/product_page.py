from utilities.read_properties import ReadConfig


class ProductPage:
    css_list_product_name = "ul[class^='product_list'] a[class='product-name']"
    css_btn_quick_hovered_view = "li[class$='hovered'] a[class='quick-view'] span"

    def __init__(self, driver):
        self.driver = driver
        self.timeout = int(ReadConfig.get_web_element_timeout())

    def is_summer_dress_page_loaded(self):
        return self.driver.title == "Women - My Store"
