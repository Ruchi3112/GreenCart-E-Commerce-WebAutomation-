import time
from PageObject.FinalCheckout import FinalCheckout
from PageObject.HomePage import HomePage
from PageObject.OrderConfirmationPage import OrderConfirmation
from utilities.BaseClass import BaseClass


class TestGreenCart(BaseClass):
    def test_Greencart(self):
        log = self.getLogger()

        homepage = HomePage(self.driver)
        homepage.Add_veggies().clear()
        log.info("Adding Veggies into the cart : ")

        homepage.Add_fruits().clear()
        log.info("Adding Fruits into the cart :")

        homepage.Add_Nuts().click()
        log.info("Adding Nuts into the cart :")

        homepage.checkout().click()

        orderconfirmation = OrderConfirmation(self.driver)
        orderconfirmation.PromoCode().click()
        time.sleep(12)
        code_validation = self.driver.find_element_by_class_name("promoInfo").text
        assert code_validation == "Code applied ..!"
        log.info("Promo Code Validation :"+code_validation)

        orderconfirmation.TotalAmountConfirmation().text
        TotalAmount = self.driver.find_element_by_xpath("//span[@class='totAmt']").text
        log.info("The Total purchase amount is :"+TotalAmount)

        orderconfirmation.DiscountedAmount().text
        DiscountedAmount = self.driver.find_element_by_xpath("//span[@class='discountAmt']").text
        log.info("The discounted amount is :"+DiscountedAmount)

        orderconfirmation.PlaceOrder().click()
        log.info("Placing the final order")

        checkout = FinalCheckout(self.driver)
        checkout.CheckOut().click()
        log.info("The order has been placed ")














