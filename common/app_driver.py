import yaml
from appium import webdriver
from config.root_config import CONFIG_PATH

from common.check_port import check_port, release_port
from common.start_server import appium_start


class BaseDriver(object):
    '''
    Get Device
    '''

    def __init__(self, device_info):
        self.device_info = device_info
        self.host = self.device_info['server_host']
        self.port = int(self.device_info['server_port'])

        if not check_port(self.host, self.port):
            release_port(self.port)
        appium_start(self.host, self.port, self.device_info['title'])

        with open(CONFIG_PATH, 'r', encoding='UTF-8') as f:
            self.data = yaml.load(f, Loader=yaml.FullLoader)

    def get_base_driver(self):
        caps = self.data[self.device_info['title']]
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
