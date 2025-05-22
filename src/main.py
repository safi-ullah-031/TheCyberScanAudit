# src/main.py

from platform_detection import detect_platform
from scanner_controller import ScannerController
from report_generator import ReportGenerator

def main():
    print("[*] Starting Cyber Scan Audit (TCSA)...")

    platform = detect_platform()
    print(f"[+] Detected OS: {platform}")

    # Initialize the controller with platform context
    controller = ScannerController(platform)
    
    # Run all scans and collect findings
    findings = controller.run_all_scans()
    
    # Generate and save the report
    reporter = ReportGenerator()
    reporter.generate_report(findings)

    print("[✓] Scan complete. Report saved in /reports folder.")

if __name__ == "__main__":
    main()