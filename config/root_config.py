from pathlib import Path

ROOT_DIR = Path().resolve()
LOG_DIR = Path(ROOT_DIR, 'log')
CONFIG_DIR = Path(ROOT_DIR, 'config')
CONFIG_PATH = Path(CONFIG_DIR, 'desired_caps.yml')

# Save screenshots
SCREENSHOTS_DIR = Path(ROOT_DIR, 'screenshots')
SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
