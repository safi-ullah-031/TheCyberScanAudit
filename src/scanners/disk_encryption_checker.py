import sys
from utils import run_command

class DiskEncryptionChecker:
    def scan(self, platform):
        if platform == "windows":
            cmd = (
                "powershell -Command \"Get-BitLockerVolume | Select-Object MountPoint, VolumeStatus, ProtectionStatus | ConvertTo-Json\""
            )
        elif platform == "linux":
            cmd = (
                "lsblk -o NAME,TYPE,MOUNTPOINT | grep 'crypt' || echo 'No LUKS volumes found'"
            )
        else:
            return {"disk_encryption": {"status": "unsupported platform", "error": None, "details": None, "returncode": 1}}
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
        return {"disk_encryption": {"output": out, "error": err, "returncode": code, "details": details}} 