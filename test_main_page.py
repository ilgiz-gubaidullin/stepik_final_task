from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

    # Тест что можно пройти на страницу для логина

# def test_guest_can_go_to_login_page(browser):
    # link = "http://selenium1py.pythonanywhere.com/"
    # page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    # page.open()                      # открываем страницу
    # page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    # login_page = LoginPage(browser, browser.current_url)
    # login_page.should_be_login_page()
    
    # Тест что есть ссылка для логина
    
# def test_guest_should_see_login_link(browser):
    # link = "http://selenium1py.pythonanywhere.com/"
    # page = MainPage(browser, link)
    # page.open()
    # page.should_be_login_link() 
    
    # Тест что есть формы для логина на странице логина

# def test_forms_that_should_be_login_page(browser):
    # link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    # page = LoginPage(browser, link)
    # page.open()
    # page.should_be_login_page()
    
    # Тест что нельзя увидеть наличие товара в корзине с главной страницы
    
def  test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_should_be_empty()
    
    
    # Ниже 3 теста на проверку наличия login_url, login_form, register_form
    
# def test_on_main_page_should_be_login_url(browser):
    # link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    # page = LoginPage(browser, link)
    # page.open()
    # page.should_be_login_url()
    
# def test_on_login_page_should_be_login_form(browser):
    # link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    # page = LoginPage(browser, link)
    # page.open()
    # page.should_be_login_form()


# def test_on_login_page_should_be_register_form(browser):
    # link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    # page = LoginPage(browser, link)
    # page.open()
    # page.should_be_register_form()
