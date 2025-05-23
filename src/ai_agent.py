import os
import glob
import json
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

def get_latest_report(report_dir="reports"):
    files = glob.glob(os.path.join(report_dir, "tcsa_report_*.json"))
    if not files:
        raise FileNotFoundError("No reports found.")
    latest = max(files, key=os.path.getctime)
    with open(latest, "r") as f:
        data = json.load(f)
    return data, latest

def analyze_report_with_agent(report_data):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY environment variable not set.")
    llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=api_key)
    prompt = (
        "You are a cybersecurity expert AI agent. "
        "Given the following system scan report in JSON, provide a human-readable summary, "
        "highlighting the most critical risks, and suggest prioritized remediation steps. "
        "Be concise and actionable.\n\nReport:\n" + json.dumps(report_data, indent=2)
    )
    response = llm([HumanMessage(content=prompt)])
    return response.content

def main():
    print("[*] Loading latest scan report...")
    report, path = get_latest_report()
    print(f"[+] Loaded report: {path}")
    print("[*] Sending report to AI agent for analysis...")
    summary = analyze_report_with_agent(report)
    print("\n===== AI Agent Analysis =====\n")
    print(summary)
    print("\n============================\n")

if __name__ == "__main__":
    main() 