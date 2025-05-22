import json
import os
from datetime import datetime

class ReportGenerator:
    def __init__(self, report_dir="reports"):
        self.report_dir = report_dir
        os.makedirs(self.report_dir, exist_ok=True)

    def generate_report(self, findings):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_path = os.path.join(self.report_dir, f"tcsa_report_{timestamp}.json")
        with open(report_path, "w") as f:
            json.dump(findings, f, indent=4)
        print(f"[+] Report saved to {report_path}")
