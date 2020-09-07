import time


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def Add_veggies(self):
        self.driver.find_element_by_css_selector("input[class='search-keyword']").send_keys("br")
        Vegies = self.driver.find_elements_by_css_selector("div[class='product'] div button")
        assert len(Vegies) == 2
        for item in Vegies:
            item.click()
        return self.driver.find_element_by_css_selector("input[class='search-keyword']")

    def Add_fruits(self):
        self.driver.find_element_by_css_selector("input[class='search-keyword']").send_keys("berry")
        time.sleep(5)
        fruits = self.driver.find_elements_by_xpath("//button[text()='ADD TO CART']")
        assert len(fruits) == 2
        for fruit in fruits:
            fruit.click()
        return self.driver.find_element_by_css_selector("input[class='search-keyword']")

    def Add_Nuts(self):
        self.driver.find_element_by_css_selector("input[class='search-keyword']").send_keys("nut")
        time.sleep(4)
        waight = self.driver.find_elements_by_css_selector("a[class='increment']")
        for item in waight:
            item.click()
        nuts = self.driver.find_elements_by_css_selector("div[class='product-action'] button")
        assert len(nuts) == 2
        for nut in nuts:
            nut.click()
        return self.driver.find_element_by_css_selector("a[class='cart-icon'] img")

    def checkout(self):
        return self.driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']")


