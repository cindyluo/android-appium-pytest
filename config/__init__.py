from pathlib import Path

import yaml
from ppadb.client import Client as AdbClient

ROOT_DIR = Path().resolve()

from config.elements import *

DEVICES = {}
ANDROID_APP_ACTIVITY = 'com.android.calculator2.Calculator'
ANDROID_APP_PACKAGE = 'com.google.android.calculator'

client = AdbClient(host='127.0.0.1', port=5037)
for device in client.devices():
    DEVICES[device.serial] = {
        'platformName': 'Android',
        'automationName': 'UiAutomator2',
        'platformVersion': device.shell('getprop ro.build.version.release').replace('\n', ''),
        'language': 'en',
        'locale': 'US',
        'deviceName': device.serial,
        'appActivity': ANDROID_APP_ACTIVITY,
        'appPackage': ANDROID_APP_PACKAGE,
        'noReset': True,
        'udid': device.serial,
    }

print(DEVICES)

LOG_DIR = Path(ROOT_DIR, 'log')
LOG_DIR.mkdir(parents=True, exist_ok=True)

SCREENSHOTS_DIR = Path(ROOT_DIR, 'screenshots')
SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
