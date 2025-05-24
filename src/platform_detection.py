# src/platform_detection.py

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import platform
import logging

def detect_platform():
    system = platform.system().lower()
    if system == "windows":
        return "windows"
    elif system == "linux":
        return "linux"
    elif system == "darwin":
        return "mac"
    else:
        logging.error(f"Unsupported platform: {system}")
        sys.exit(1)

if __name__ == "__main__":
    detected = detect_platform()
    print(f"Detected OS: {detected}")