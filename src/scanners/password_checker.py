import sys
from utils import run_command

class PasswordChecker:
    def scan(self, platform):
        if platform == "windows":
            cmd = (
                "powershell -Command \""
                "Get-LocalUser | Where-Object { $_.PasswordRequired -eq $false } | Select-Object Name,Enabled\""
            )
        elif platform == "linux":
            cmd = "awk -F: '($2=="" || $2=="*" || $2=="!") {print $1}' /etc/shadow"
        else:
            return {"passwords": {"status": "unsupported platform", "error": None, "details": None, "returncode": 1}}
        out, err, code = run_command(cmd)
        details = out.strip().splitlines() if out else []
        return {"passwords": {"output": out, "error": err, "returncode": code, "details": details}}
