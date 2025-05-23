import sys
from utils import run_command

class PatchChecker:
    def scan(self, platform):
        if platform == "windows":
            cmd = (
                "powershell -Command \"Get-WindowsUpdate -MicrosoftUpdate -AcceptAll -IgnoreReboot | Where-Object { $_.IsInstalled -eq $false } | Select-Object Title\""
            )
        elif platform == "linux":
            cmd = "apt list --upgradable 2>/dev/null | grep -i security"
        else:
            return {"patches": {"status": "unsupported platform", "error": None, "details": None, "returncode": 1}}
        out, err, code = run_command(cmd)
        details = out.strip().splitlines() if out else []
        return {"patches": {"output": out, "error": err, "returncode": code, "details": details}}
