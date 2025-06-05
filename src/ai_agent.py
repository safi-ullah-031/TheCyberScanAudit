import os
import glob
import json
import logging
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv

load_dotenv()

def get_latest_report(report_dir="reports"):
    files = glob.glob(os.path.join(report_dir, "tcsa_report_*.json"))
    if not files:
        logging.error("No reports found.")
        return None, None
    latest = max(files, key=os.path.getctime)
    try:
        with open(latest, "r") as f:
            data = json.load(f)
        return data, latest
    except Exception as e:
        logging.error(f"Failed to load report: {e}")
        return None, None

def analyze_report_with_agent(report_data):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        logging.error("OPENAI_API_KEY environment variable not set.")
        return "[ERROR] AI analysis unavailable: API key not set."
    try:
        llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=api_key)
        prompt = (
            "You are a cybersecurity expert AI agent. "
            "Given the following system scan report in JSON, provide a human-readable summary, "
            "highlighting the most critical risks, and suggest prioritized remediation steps. "
            "Be concise and actionable.\n\nReport:\n" + json.dumps(report_data, indent=2)
        )
        response = llm([HumanMessage(content=prompt)])
        return response.content
    except Exception as e:
        logging.error(f"AI agent failed: {e}")
        return f"[ERROR] AI agent failed: {e}"

def main():
    print("[*] Loading latest scan report...")
    report, path = get_latest_report()
    if not report:
        print("[!] No valid report found. Please run a scan first.")
        return
    print(f"[+] Loaded report: {path}")
    print("[*] Sending report to AI agent for analysis...")
    summary = analyze_report_with_agent(report)
    print("\n===== AI Agent Analysis =====\n")
    print(summary)
    print("\n============================\n")

if __name__ == "__main__":
    main() 