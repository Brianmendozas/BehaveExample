from behave import given, when, then
from pages.LoginPage import LoginPage
from pages.ProductListPage import ProductListPage


class loginSteps:
    @given("Que estamos en la pantalla de login")
    def varify_login_page(context):
        context.loginpage_object = LoginPage(context.web_driver)
        context.loginpage_object.verify_login_page()

    @when("Haya ingresado mi usuario y contraseña y presionando entrar")
    def send_user_password(context):
       context.loginpage_object.send_user_password("standard_user","secret_sauce")
       context.loginpage_object.press_login_button()

    @then("Valida que mi sesion este activa")
    def verify_active_session(context):
        context.product_list_page_object = ProductListPage(context.web_driver)
        context.product_list_page_object.verify_product_list_page()
