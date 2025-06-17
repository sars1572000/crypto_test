from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.navigate_up_button = (AppiumBy.ACCESSIBILITY_ID, 'Navigate up')
        self.warning_services_button = (AppiumBy.XPATH, "(//android.widget.ImageView[@resource-id='hko.MyObservatory_v1_0:id/icon'])[1]")
        self.nine_day_forecast = (AppiumBy.XPATH, "(//android.widget.ImageView[@resource-id='hko.MyObservatory_v1_0:id/icon'])[6]")
        self.ninth_day_field =  (AppiumBy.XPATH, "//android.widget.ListView[@resource-id='hko.MyObservatory_v1_0:id/mainAppSevenDayView']/android.widget.LinearLayout[3]/android.widget.LinearLayout[2]/android.widget.LinearLayout[4]/android.widget.TextView[1]")


    def go_to_9_day_forecast(self):
        self.driver.find_element(*self.navigate_up_button).click()
        self.driver.find_element(*self.warning_services_button).click()
        self.driver.find_element(*self.nine_day_forecast).click()

    def get_ninth_day_weather(self):
        time.sleep(1)
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(586, 2097)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(582, 909)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(557, 2048)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(590, 872)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        ninth_day = self.driver.find_element(*self.ninth_day_field)
        return ninth_day.text