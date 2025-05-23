import sys
from utils import run_command

class FirewallChecker:
    def scan(self, platform):
        if platform == "windows":
            cmd = (
                "powershell -Command \""
                "$profiles = Get-NetFirewallProfile | Select-Object Name, Enabled, DefaultInboundAction, DefaultOutboundAction; "
                "$profiles | ConvertTo-Json\""
            )
        elif platform == "linux":
            cmd = "sudo ufw status verbose"
        else:
            return {"firewall": {"status": "unsupported platform", "error": None, "details": None, "returncode": 1}}
        out, err, code = run_command(cmd)
        details = None
        if code == 0 and out:
            try:
                if platform == "windows":
                    import json as _json
                    details = _json.loads(out)
                else:
                    details = out
            except Exception as e:
                err = str(e)
        return {"firewall": {"output": out, "error": err, "returncode": code, "details": details}}
