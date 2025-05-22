from scanners.firewall_checker import FirewallChecker
from scanners.password_checker import PasswordChecker
from scanners.patch_checker import PatchChecker
from scanners.software_checker import SoftwareChecker
from scanners.startup_checker import StartupChecker

class ScannerController:
    def __init__(self, platform):
        self.platform = platform
        self.scanners = [
            FirewallChecker(),
            PasswordChecker(),
            PatchChecker(),
            SoftwareChecker(),
            StartupChecker(),
        ]

    def run_all_scans(self):
        findings = {}
        for scanner in self.scanners:
            result = scanner.scan(self.platform)
            findings.update(result)
        return findings 