import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from scanners.firewall_checker import FirewallChecker
from scanners.password_checker import PasswordChecker
from scanners.patch_checker import PatchChecker
from scanners.software_checker import SoftwareChecker
from scanners.startup_checker import StartupChecker
from scanners.open_ports_checker import OpenPortsChecker
from scanners.disk_encryption_checker import DiskEncryptionChecker

class ScannerController:
    def __init__(self, platform):
        self.platform = platform
        self.scanners = [
            FirewallChecker(),
            PasswordChecker(),
            PatchChecker(),
            SoftwareChecker(),
            StartupChecker(),
            OpenPortsChecker(),
            DiskEncryptionChecker(),
        ]

    def run_all_scans(self):
        findings = {}
        for scanner in self.scanners:
            result = scanner.scan(self.platform)
            findings.update(result)
        return findings 