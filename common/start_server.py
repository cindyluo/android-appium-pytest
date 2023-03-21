import subprocess

from appium.webdriver.appium_service import AppiumService, AppiumServiceError

from config.root_config import LOG_DIR


def appium_start(host, port, log_name):
    try:
        service = AppiumService()
        if not service.is_running:
            service.start(
                stdout=open(f'{LOG_DIR}/{log_name}.log', 'w', encoding='utf8'),
                stderr=subprocess.STDOUT,
                timeout_ms=3000,
                args=[
                    '--address',
                    host,
                    '-p',
                    str(port),
                    '--base-path',
                    '/wd/hub',
                ],
            )
    except AppiumServiceError as error:
        print(error)


if __name__ == '__main__':
    appium_start('127.0.0.1', 4723, 'appium_start_log.txt')
