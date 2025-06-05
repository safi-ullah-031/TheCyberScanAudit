import gradio as gr
import subprocess
import os
from ai_agent import get_latest_report, analyze_report_with_agent

def run_full_scan():
    # Run the main scan script
    try:
        result = subprocess.run(["python", os.path.join("src", "main.py")], capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        return f"[ERROR] Scan failed: {e.stderr or e.output}"
    # Get the latest report and AI summary
    report, _ = get_latest_report()
    if not report:
        return "[ERROR] No report found after scan."
    summary = analyze_report_with_agent(report)
    return summary

def main():
    with gr.Blocks() as demo:
        gr.Markdown("""
        # Cyber Scan Audit (TCSA)
        Welcome! Click the button below to run a full security scan. The results will be summarized in plain language for you.
        """)
        scan_btn = gr.Button("Run Security Scan")
        output = gr.Textbox(label="Security Audit Summary", lines=20)
        scan_btn.click(run_full_scan, outputs=output)
    demo.launch()

if __name__ == "__main__":
    main() 