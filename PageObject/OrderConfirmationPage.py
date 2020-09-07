import time


class OrderConfirmation:
    def __init__(self, driver):
        self.driver = driver

    def PromoCode(self):
        self.driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
        return self.driver.find_element_by_xpath("//button[text()='Apply']")

    def TotalAmountConfirmation(self):
        amounts = self.driver.find_elements_by_xpath("//tr/td[5]/p")
        intSum = 0
        for amt in amounts:
            Total1 = intSum
        return self.driver.find_element_by_xpath("//span[@class='totAmt']")


    def DiscountedAmount(self):
        return self.driver.find_element_by_xpath("//span[@class='discountAmt']")


    def PlaceOrder(self):
        return self.driver.find_element_by_xpath("//button[text()='Place Order']")


