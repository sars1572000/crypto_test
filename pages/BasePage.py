from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def swipe_up_relative(self, ratio_start=0.8, ratio_end=0.2):
        """Slide up according to the screen ratio, the default height is from 80% to 20%"""
        size = self.driver.get_window_size()
        width = size["width"]
        height = size["height"]

        start_x = width // 2
        start_y = int(height * ratio_start)
        end_x = width // 2
        end_y = int(height * ratio_end)

        actions = ActionChains(self.driver)
        touch = PointerInput(interaction.POINTER_TOUCH, "touch")
        actions.w3c_actions = ActionBuilder(self.driver, mouse=touch)
        actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
        actions.w3c_actions.pointer_action.release()
        actions.perform()