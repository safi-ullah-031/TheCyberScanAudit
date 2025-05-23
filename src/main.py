import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from platform_detection import detect_platform
from scanner_controller import ScannerController
from report_generator import ReportGenerator
from ai_agent import analyze_report_with_agent, get_latest_report

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

    # Automatically send the report to the AI agent for summarization
    print("[*] Sending scan results to AI agent for human-readable summary...")
    report, _ = get_latest_report()
    summary = analyze_report_with_agent(report)
    print("\n===== Security Audit Summary =====\n")
    print(summary)
    print("\n==================================\n")

if __name__ == "__main__":
    main()