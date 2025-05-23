import sys
from utils import run_command

class SoftwareChecker:
    def scan(self, platform):
        if platform == "windows":
            cmd = (
                "powershell -Command \"Get-WmiObject -Class Win32_Product | Select-Object Name, Version\""
            )
        elif platform == "linux":
            cmd = "dpkg -l | grep '^ii'"
        else:
            return {"software": {"status": "unsupported platform", "error": None, "details": None, "returncode": 1}}
        out, err, code = run_command(cmd)
        details = out.strip().splitlines() if out else []
        return {"software": {"output": out, "error": err, "returncode": code, "details": details}}
