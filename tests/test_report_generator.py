import os
import json
from src.report_generator import ReportGenerator

def test_generate_report(tmp_path):
    findings = {
        "firewall": {"output": "ok", "error": "", "returncode": 0},
        "disk_encryption": {"details": "No LUKS volumes found", "output": "", "error": "", "returncode": 0},
    }
    report_dir = tmp_path / "reports"
    rg = ReportGenerator(report_dir=str(report_dir))
    rg.generate_report(findings)
    files = list(report_dir.glob("tcsa_report_*.json"))
    assert files, "No report file created"
    with open(files[0], "r") as f:
        data = json.load(f)
        assert "firewall" in data
        assert "risk_rating" in data["firewall"]
        assert "disk_encryption" in data
        assert "risk_rating" in data["disk_encryption"] 