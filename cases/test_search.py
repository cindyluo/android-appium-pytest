import time

import pytest
from appium.webdriver.common.appiumby import AppiumBy

from base.base_page import Base
from config.root_config import SCREENSHOTS_DIR


class TestSearch(object):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self, common_driver):
        base = Base(common_driver)
        base.skip_chrome_landing()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_go_appium_official(self, common_driver):
        driver = common_driver
        base = Base(driver)

        id_url_bar = (AppiumBy.ID, 'com.android.chrome:id/search_box_text')
        _, url_bar = base.find_element(id_url_bar)
        url_bar.send_keys('https://appium.io')
        driver.press_keycode(66)
        time.sleep(1)

        class_page_title = (AppiumBy.CLASS_NAME, 'android.webkit.WebView')
        _, page_title = base.find_element(class_page_title)
        assert page_title.text == 'Appium: Mobile App Automation Made Awesome.'
        driver.get_screenshot_as_file(
            f'{SCREENSHOTS_DIR}/TestSearch_test_go_appium_official_Step_1.png'
        )


if __name__ == '__main__':
    pytest.main()
