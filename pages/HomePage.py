from appium.webdriver.common.appiumby import AppiumBy
import time
from pages.BasePage import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
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
        self.swipe_up_relative()
        self.swipe_up_relative()
        ninth_day = self.driver.find_element(*self.ninth_day_field)
        return ninth_day.text