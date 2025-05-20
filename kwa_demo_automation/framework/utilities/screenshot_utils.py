# pylint: disable=[line-too-long, missing-module-docstring, missing-function-docstring]


import os
import re
from datetime import datetime


def get_screenshot_path(test_name: str, subdir="screenshots") -> str:
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir))
    screenshot_dir = os.path.join(base_dir, subdir)
    os.makedirs(screenshot_dir, exist_ok=True)

    # Sanitize filename
    safe_name = re.sub(r'[^a-zA-Z0-9_-]', '_', test_name)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"{safe_name}_{timestamp}.png"

    return os.path.join(screenshot_dir, file_name)
