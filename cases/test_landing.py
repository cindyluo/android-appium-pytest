import time

import pytest
from appium.webdriver.common.appiumby import AppiumBy

from base.base_page import Base
from config.root_config import SCREENSHOTS_DIR


class TestLanding(object):
    def test_landing(self, common_driver):
        driver = common_driver
        base = Base(driver)

        time.sleep(5)
        driver.get_screenshot_as_file(f'{SCREENSHOTS_DIR}/TestLanding_test_landing_Step_0.png')

        # Welcome to Chrome
        id_terms_accept_btn = (AppiumBy.ID, 'com.android.chrome:id/terms_accept')
        _, terms_accept_btn = base.find_element(id_terms_accept_btn)
        assert terms_accept_btn.text == 'Accept & continue'
        driver.get_screenshot_as_file(
            f'{SCREENSHOTS_DIR}/TestLanding_test_landing_Step_1_Welcome.png'
        )
        terms_accept_btn.click()

        time.sleep(1)

        # Turn on sync
        id_sync_no_btn = (AppiumBy.ID, 'com.android.chrome:id/negative_button')
        _, sync_no_btn = base.find_element(id_sync_no_btn)
        driver.get_screenshot_as_file(f'{SCREENSHOTS_DIR}/TestLanding_test_landing_Step_2_Sync.png')
        sync_no_btn.click()

        time.sleep(1)

        # Notification
        id_notification_yes_btn = (AppiumBy.ID, 'com.android.chrome:id/positive_button')
        is_exist, notification_yes_btn = base.find_element(id_notification_yes_btn)
        if is_exist:
            driver.get_screenshot_as_file(
                f'{SCREENSHOTS_DIR}/TestLanding_test_landing_Step_3_notification.png'
            )
            notification_yes_btn.click()

            time.sleep(1)

            # (Android 13) Notifications permission
            id_system_permission_allow_btn = (
                AppiumBy.XPATH,
                './/android.widget.Button[@text="Allow"]',
            )
            is_exist, system_permission_allow_btn = base.find_element(
                id_system_permission_allow_btn
            )
            system_permission_allow_btn.click()

            time.sleep(1)

        driver.get_screenshot_as_file(f'{SCREENSHOTS_DIR}/TestLanding_test_landing_Step_4_home.png')


if __name__ == '__main__':
    pytest.main()
