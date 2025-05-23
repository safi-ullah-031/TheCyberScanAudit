import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import json
from datetime import datetime

def get_risk_rating(category, data):
    # Simple risk logic for demonstration
    if category == "firewall":
        if data.get("error") or data.get("returncode", 0) != 0:
            return "high"
        return "low"
    if category == "open_ports":
        if data.get("output"):
            lines = data["output"].splitlines()
            if len(lines) > 10:
                return "medium"
            elif len(lines) > 0:
                return "low"
        return "info"
    if category in ("passwords", "patches", "software", "startup"):
        if "unsupported" in str(data.get("result", "")).lower():
            return "info"
        if "weak" in str(data.get("result", "")).lower() or "missing" in str(data.get("result", "")).lower():
            return "high"
        return "low"
    return "info"

class ReportGenerator:
    def __init__(self, report_dir="reports"):
        self.report_dir = report_dir
        os.makedirs(self.report_dir, exist_ok=True)

    def generate_report(self, findings):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_path = os.path.join(self.report_dir, f"tcsa_report_{timestamp}.json")
        # Add risk ratings
        findings_with_risk = {}
        for category, data in findings.items():
            findings_with_risk[category] = data.copy() if isinstance(data, dict) else {"result": data}
            findings_with_risk[category]["risk_rating"] = get_risk_rating(category, data)
        with open(report_path, "w") as f:
            json.dump(findings_with_risk, f, indent=4)
        print(f"[+] Report saved to {report_path}")
