import time
from typing import Dict, Tuple

from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait


class Base(object):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @property
    def get_phone_size(self):
        '''
        Get Screen Size
        '''
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        return width, height

    def find_element(self, locator: tuple, timeout=30) -> Tuple[Dict, WebElement]:
        wait = WebDriverWait(self.driver, timeout)
        try:
            element = wait.until(lambda driver: driver.find_element(*locator))
            return True, element
        except (NoSuchElementException, TimeoutException):
            print(f'no found element {locator[1]} by {locator[0]}')
            return False, None

    def skip_chrome_landing(self):
        # Welcome to Chrome
        id_terms_accept_btn = (AppiumBy.ID, 'com.android.chrome:id/terms_accept')
        _, terms_accept_btn = self.find_element(id_terms_accept_btn)
        terms_accept_btn.click()

        # Turn on sync
        id_sync_no_btn = (AppiumBy.ID, 'com.android.chrome:id/negative_button')
        _, sync_no_btn = self.find_element(id_sync_no_btn)
        sync_no_btn.click()

        # Notification
        id_notification_yes_btn = (AppiumBy.ID, 'com.android.chrome:id/positive_button')
        is_exist, notification_yes_btn = self.find_element(id_notification_yes_btn)
        if is_exist:
            notification_yes_btn.click()
            time.sleep(1)

            # (Android 13) Notifications permission
            id_system_permission_allow_btn = (
                AppiumBy.XPATH,
                './/android.widget.Button[@text="Allow"]',
            )
            _, system_permission_allow_btn = self.find_element(id_system_permission_allow_btn)
            system_permission_allow_btn.click()


if __name__ == '__main__':
    pass
