import sys
from utils import run_command

class StartupChecker:
    def scan(self, platform):
        if platform == "windows":
            cmd = (
                "powershell -Command \"Get-CimInstance -ClassName Win32_StartupCommand | Select-Object Name, Command, Location\""
            )
        elif platform == "linux":
            cmd = "ls /etc/xdg/autostart /etc/init.d ~/.config/autostart 2>/dev/null"
        else:
            return {"startup": {"status": "unsupported platform", "error": None, "details": None, "returncode": 1}}
        out, err, code = run_command(cmd)
        details = out.strip().splitlines() if out else []
        return {"startup": {"output": out, "error": err, "returncode": code, "details": details}}
