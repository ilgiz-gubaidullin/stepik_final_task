from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time
import pytest
   
   
@pytest.mark.parametrize('promo_offer',
                         [ 0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail(reason="Failed link")), 8, 9 ])    
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, promo_offer):
    # тест для добавления товара в корзину
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.should_add_to_basket()
    
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # тест гость не может видеть успешное письмо после добавления товара в корзину
    # link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    # page = ProductPage(browser, link)
    # page.open()
    # page.should_add_to_basket()
    # page.should_not_be_success_message()
    
# def test_message_disappeared_after_adding_product_to_basket(browser):
    # тест сообщение исчезает после добавления товара в корзину
    # link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    # page = ProductPage(browser, link)
    # page.open()
    # page.should_add_to_basket()
    # page.element_should_disappear()
    
# def test_guest_should_see_login_link_on_product_page(browser):
    # тест что ссылка для залогинивания есть на страницу товара
    # link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    # page = ProductPage(browser, link)
    # page.open()
    # page.should_be_login_link()

@pytest.mark.need_review    
def test_guest_can_go_to_login_page_from_product_page(browser):
    # тест можно перейти из страницы товара на страницу логина
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review    
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # тест, что в корзине нет товаров и есть сообщение о пустой корзине
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_should_be_empty()
    
class TestUserAddToBasketFromProductPage(object):
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):

        # setup-функция, подготавливает данные и выполняется перед запуском каждого теста из класса
        # Открывает форму регистрации, регистрирует нового пользователя
        # Проверяет, что пользователь залогинен

        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        
        email = str(time.time()) + '@fakemail.org'
        password = str(time.time())
        
        page.register_new_user(email=email, password=password)
        time.sleep(5)
        page.should_be_authorized_user()
        
    def test_user_cant_see_success_message(self, browser):
        # тест что не должно быть сообщения об успешном добавлении
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
        
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        # тест что можно добавить товар в корзину
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.should_add_to_basket()
    