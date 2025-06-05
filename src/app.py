import gradio as gr
import subprocess
import os
import sys
from ai_agent import analyze_report_with_agent
from scanner_controller import ScannerController
from report_generator import ReportGenerator
from platform_detection import detect_platform
from scanners.firewall_checker import FirewallChecker
from scanners.password_checker import PasswordChecker
from scanners.patch_checker import PatchChecker
from scanners.software_checker import SoftwareChecker
from scanners.startup_checker import StartupChecker
from scanners.open_ports_checker import OpenPortsChecker

def run_individual_scan(scanner_name):
    platform = detect_platform()
    scanner_map = {
        "Firewall": FirewallChecker(),
        "Passwords": PasswordChecker(),
        "Patches": PatchChecker(),
        "Software": SoftwareChecker(),
        "Startup": StartupChecker(),
        "Open Ports": OpenPortsChecker(),
    }
    scanner = scanner_map.get(scanner_name)
    if not scanner:
        return f"[ERROR] Scanner '{scanner_name}' not found."
    findings = scanner.scan(platform)
    # Use the AI agent to summarize just this finding
    summary = analyze_report_with_agent(findings)
    return summary

def run_full_scan():
    platform = detect_platform()
    controller = ScannerController(platform)
    findings = controller.run_all_scans()
    reporter = ReportGenerator()
    reporter.generate_report(findings)
    summary = analyze_report_with_agent(findings)
    return summary

def main():
    with gr.Blocks() as demo:
        gr.Markdown("""
        # Cyber Scan Audit (TCSA)
        Welcome! You can run a full security scan or select an individual scan below. Results will be summarized in plain language for you.
        """)
        with gr.Row():
            firewall_btn = gr.Button("Firewall Scan")
            password_btn = gr.Button("Password Scan")
            patch_btn = gr.Button("Patch Scan")
            software_btn = gr.Button("Software Scan")
            startup_btn = gr.Button("Startup Scan")
            ports_btn = gr.Button("Open Ports Scan")
            full_btn = gr.Button("Full Scan (All)")
        output = gr.Textbox(label="Security Audit Summary", lines=20)
        firewall_btn.click(lambda: run_individual_scan("Firewall"), outputs=output)
        password_btn.click(lambda: run_individual_scan("Passwords"), outputs=output)
        patch_btn.click(lambda: run_individual_scan("Patches"), outputs=output)
        software_btn.click(lambda: run_individual_scan("Software"), outputs=output)
        startup_btn.click(lambda: run_individual_scan("Startup"), outputs=output)
        ports_btn.click(lambda: run_individual_scan("Open Ports"), outputs=output)
        full_btn.click(run_full_scan, outputs=output)
    demo.launch()

if __name__ == "__main__":
    main() 