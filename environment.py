import time
from driver_interactions.ElementsInteractions import ElementsInteractions
from driver_interactions.InitWebDriver import InitWebDriver

def before_all(context):
    print("Esta funcion se ejecuta al inicio del script")
    context.web_driver = InitWebDriver().Init_web_driver()
    context.interactions_object = ElementsInteractions(context.web_driver)
    context.interactions_object.launch_web_page("https://www.saucedemo.com")

def after_all(context):
    print("Esta funcion se ejecuta al final del script")
    time.sleep(5)
    context.web_driver.quit()