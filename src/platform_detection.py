# src/platform_detection.py

import platform
import sys

def detect_platform():
    system = platform.system().lower()
    if system == "windows":
        return "windows"
    elif system == "linux":
        return "linux"
    elif system == "darwin":
        return "mac"
    else:
        print(f"Unsupported platform: {system}")
        sys.exit(1)

if __name__ == "__main__":
    detected = detect_platform()
    print(f"Detected OS: {detected}")
