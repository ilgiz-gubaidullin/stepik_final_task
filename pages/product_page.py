from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def should_add_to_basket(self):
    # метод для добавления в корзину
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()
        
        # self.solve_quiz_and_get_code() 
        # Закоментил потому что не используется, а так для проверки совпадения названия и цены
        
        # book_name = self.browser.find_element(By.CSS_SELECTOR, "#messages .alert-success:first-child strong")
        # a = book_name.text
        # book_name_in_basket = self.browser.find_element(By.CSS_SELECTOR, ".product_main h1")
        # b = book_name_in_basket.text
        # assert a == b, 'Название товара не совпадает'
        
        # book_price = self.browser.find_element(By.CSS_SELECTOR, ".alertinner p strong")
        # c = book_price.text
        # book_price_in_basket = self.browser.find_element(By.CSS_SELECTOR, '.product_main [class="price_color"]')
        # d = book_price_in_basket.text
        # assert c == d, 'Цена товара не совпадает'
        
        
        
        
        # метод для проверки что нет сообщения об успешном добавлении
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"        
        
        # метод для проверки что элемент исчезает
    def element_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Element doesn't disappear"
        
    
    