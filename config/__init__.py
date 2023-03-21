from pathlib import Path

import yaml

ROOT_DIR = Path().resolve()

from config.elements import *

DEVICES = {}
DEFAULT_DEVICES_CONFIG = Path(ROOT_DIR, 'config', 'desired_caps.yml')
if DEFAULT_DEVICES_CONFIG.exists():
    with open(DEFAULT_DEVICES_CONFIG, 'r', encoding='UTF-8') as f:
        DEVICES = yaml.load(f, Loader=yaml.FullLoader)

LOG_DIR = Path(ROOT_DIR, 'log')
LOG_DIR.mkdir(parents=True, exist_ok=True)

SCREENSHOTS_DIR = Path(ROOT_DIR, 'screenshots')
SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
