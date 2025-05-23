import sys
from utils import run_command

class OpenPortsChecker:
    def scan(self, platform):
        if platform == "windows":
            # Use netstat to list listening ports
            cmd = "netstat -ano | findstr LISTENING"
        elif platform == "linux":
            # Use ss or netstat to list listening ports
            cmd = "ss -tuln"
        else:
            return {"open_ports": {"status": "unsupported platform"}}
        out, err, code = run_command(cmd)
        return {"open_ports": {"output": out, "error": err, "returncode": code}} 