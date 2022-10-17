import time

import pytest

from common.check_port import release_port
from common.app_driver import BaseDriver

base_driver = None


def pytest_addoption(parser):
    parser.addoption('--cmdopt', action='store', default='device_info', help=None)


@pytest.fixture(scope='session')
def cmd_opt(request):
    return request.config.getoption('--cmdopt')


@pytest.fixture(scope='session')
def common_driver(cmd_opt):
    cmd_opt = eval(cmd_opt)
    print('cmd_opt', cmd_opt)
    global base_driver
    base_driver = BaseDriver(cmd_opt)
    time.sleep(1)
    driver = base_driver.get_base_driver()
    yield driver
    # driver.close_app()
    driver.quit()
    release_port(cmd_opt['server_port'])
