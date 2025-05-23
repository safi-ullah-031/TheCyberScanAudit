import sys
from utils import run_command

class OpenPortsChecker:
    def scan(self, platform):
        if platform == "windows":
            cmd = "netstat -ano | findstr LISTENING"
        elif platform == "linux":
            cmd = "ss -tuln || netstat -tuln"
        else:
            return {"open_ports": {"status": "unsupported platform", "error": None, "details": None, "returncode": 1}}
        out, err, code = run_command(cmd)
        details = out.strip().splitlines() if out else []
        return {"open_ports": {"output": out, "error": err, "returncode": code, "details": details}} 