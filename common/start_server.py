import subprocess
from pathlib import Path

from config.root_config import LOG_DIR


def appium_start(host, port, log_name):
    # --bootstrap-port: (Android-only) port to use on device to talk to Appium
    bootstrap_port = str(port + 1)
    cmd = 'appium -a ' + host + ' -p ' + str(port) + ' -bp ' + str(bootstrap_port)

    Path(f'{LOG_DIR}/appium_log').mkdir(parents=True, exist_ok=True)
    subprocess.Popen(
        cmd,
        shell=True,
        stdout=open(f'{LOG_DIR}/appium_log/{log_name}.log', 'w', encoding='utf8'),
        stderr=subprocess.STDOUT,
    )

    # pkill -9 -f appium


if __name__ == '__main__':
    appium_start('127.0.0.1', 4723, 'appium_start_log.txt')
