import os
from multiprocessing import Pool

import pytest

device_infos = [
    {
        'device_name': 'Emulator_one',
        'server_host': '127.0.0.1',
        'server_port': '4723',
    }
]

# device_infos = [
#     {
#         'device_name': 'Pixel6',
#         'server_host': '127.0.0.1',
#         'server_port': '4723',
#     }
# ]


def main(device_info):
    pytest.main(['--cmdopt={}'.format(device_info), '--alluredir', './allure-results', '-vs'])
    os.system('allure generate allure-results -o allure-report --clean')


if __name__ == '__main__':
    with Pool(1) as pool:
        pool.map(main, device_infos)
        pool.close()
        pool.join()
