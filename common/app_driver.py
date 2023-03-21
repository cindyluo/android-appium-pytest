import yaml
from appium import webdriver

from common.check_port import check_port, release_port
from common.start_server import appium_start
from config import DEVICES


class BaseDriver(object):
    '''
    Get Device
    '''

    def __init__(self, device_info):
        self.device_info = device_info
        self.device_name = self.device_info['device_name']
        self.host = self.device_info['server_host']
        self.port = int(self.device_info['server_port'])
        self.data = DEVICES

        if not check_port(self.host, self.port):
            release_port(self.port)
        appium_start(self.host, self.port, self.device_name)

    def get_base_driver(self):
        caps = self.data[self.device_name]
        driver = webdriver.Remote(
            command_executor='http://' + self.host + ':' + str(self.port) + '/wd/hub',
            desired_capabilities=caps,
        )
        return driver


if __name__ == '__main__':
    device_info = {
        'title': 'Emulator_two',
        'server_host': '127.0.0.1',
        'server_port': 4725,
    }
    base = BaseDriver(device_info)
