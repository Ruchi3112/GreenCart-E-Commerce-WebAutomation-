from selenium import webdriver


class FinalCheckout:
    def __init__(self, driver):
        self.driver = driver

    def CheckOut(self):
        self.driver.find_element_by_xpath("//div/select").click()
        dropdown = webdriver.support.select.Select(self.driver.find_element_by_xpath("//div/select"))
        dropdown.select_by_visible_text("India")
        self.driver.find_element_by_css_selector("input[class='chkAgree']").click()
        return self.driver.find_element_by_xpath("//button[text()='Proceed']")
