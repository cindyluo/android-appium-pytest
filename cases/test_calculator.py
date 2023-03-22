import pytest
from appium.webdriver.webdriver import WebDriver

from base.base_page import Base
from config import SCREENSHOTS_DIR, CalculatorElements


class TestCalculator(object):
    def test_android_calculator(self, common_driver: WebDriver):
        driver = common_driver
        base = Base(driver)

        driver.get_screenshot_as_file(f'{SCREENSHOTS_DIR}/calculator_init.png')

        for num in range(1, 11):
            if num < 10:
                button_digit_element = (
                    CalculatorElements.BUTTON_DIGIT_PREFIX[0],
                    f'{CalculatorElements.BUTTON_DIGIT_PREFIX[1]}_{num}',
                )
                _, button_digit = base.find_element(button_digit_element)
                button_digit.click()
            else:
                for char in str(num):
                    button_digit_element = (
                        CalculatorElements.BUTTON_DIGIT_PREFIX[0],
                        f'{CalculatorElements.BUTTON_DIGIT_PREFIX[1]}_{char}',
                    )
                    _, button_digit = base.find_element(button_digit_element)
                    button_digit.click()

            _, button_op_add = base.find_element(CalculatorElements.BUTTON_OP_ADD)
            button_op_add.click()

        _, button_eq = base.find_element(CalculatorElements.BUTTON_EQ)
        button_eq.click()

        _, text_result = base.find_element(CalculatorElements.TEXT_RESULT)
        assert text_result.text == "55"
