import sys
from src.scanners.utils import run_command

class FirewallChecker:
    def scan(self, platform):
        if platform == "windows":
            cmd = "powershell -Command 'Get-NetFirewallProfile | Select-Object Name, Enabled'"
        elif platform == "linux":
            cmd = "sudo ufw status"
        else:
            return {"firewall": {"status": "unsupported platform"}}
        out, err, code = run_command(cmd)
        return {"firewall": {"output": out, "error": err, "returncode": code}}
