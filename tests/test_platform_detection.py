import pytest
from src.platform_detection import detect_platform

def test_detect_platform_supported(monkeypatch):
    monkeypatch.setattr("platform.system", lambda: "Windows")
    assert detect_platform() == "windows"
    monkeypatch.setattr("platform.system", lambda: "Linux")
    assert detect_platform() == "linux"
    monkeypatch.setattr("platform.system", lambda: "Darwin")
    assert detect_platform() == "mac"

# Uncomment to test unsupported platform (will exit)
# def test_detect_platform_unsupported(monkeypatch):
#     monkeypatch.setattr("platform.system", lambda: "Solaris")
#     with pytest.raises(SystemExit):
#         detect_platform() 