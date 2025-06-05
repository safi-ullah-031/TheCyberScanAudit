import os
import glob
import json
import logging
from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
try:
    import google.generativeai as genai
except ImportError:
    genai = None

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
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    openai_api_key = os.getenv("OPENAI_API_KEY")
    prompt = (
        "You are a cybersecurity expert AI agent. "
        "Given the following system scan report in JSON, provide a human-readable summary, "
        "highlighting the most critical risks, and suggest prioritized remediation steps. "
        "Be concise and actionable.\n\nReport:\n" + json.dumps(report_data, indent=2)
    )
    if gemini_api_key and genai:
        try:
            genai.configure(api_key=gemini_api_key)
            model = genai.GenerativeModel('models/gemma-3-1b-it')
            response = model.generate_content(prompt)
            return response.text if hasattr(response, 'text') else str(response)
        except Exception as e:
            logging.error(f"Gemini agent failed: {e}")
            return f"[ERROR] Gemini agent failed: {e}"
    elif openai_api_key:
        try:
            llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=openai_api_key)
            response = llm([HumanMessage(content=prompt)])
            return response.content
        except Exception as e:
            logging.error(f"OpenAI agent failed: {e}")
            return f"[ERROR] OpenAI agent failed: {e}"
    else:
        logging.error("No API key set for either Gemini or OpenAI.")
        return "[ERROR] No API key set for either Gemini or OpenAI."

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