# The Cyber Scan Audit (TCSA)

**The Cyber Scan Audit (TCSA)** is a cross-platform cybersecurity tool designed to automate system health assessments and identify common security weaknesses. Built with Python, PowerShell, and Bash scripting, TCSA scans your system for vulnerabilities such as weak passwords, outdated software, misconfigured firewalls, missing patches, and suspicious startup entries. It generates a comprehensive security report with categorized findings and risk ratings.

## Features

- Checks for weak passwords and insecure user configurations  
- Detects outdated software and missing security patches  
- Analyzes firewall settings and open ports  
- Scans startup programs for suspicious entries  
- Generates detailed, categorized security reports  
- Helps you maintain a regular audit of your system’s security posture

## Tech Stack

- Python 3.x for core logic and orchestration  
- PowerShell scripts for Windows-specific checks  
- Bash scripts for specific checks  
- Reporting via JSON and HTML (PDF export planned)

## Getting Started

### Prerequisites

- Python 3.8+  
- PowerShell (on Windows)  

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/safi-ullah-031/TheCyberScanAudit.git
   cd TheCyberScanAudit
   ```

2. (Optional) Create a virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

### Usage

Run the platform detection module as a quick test:

```bash
python src/platform_detection.py
```

This will print the detected operating system.

## Project Structure

```
TheCyberScanAudit/
├── README.md
├── LICENSE
├── requirements.txt
├── src/
│   ├── main.py
│   ├── platform_detection.py
│   ├── scanners/
│   └── ...
├── scripts/
│   ├── windows/
│   └── linux/
├── reports/
└── tests/
```

## Contributing

Contributions, issues, and feature requests are welcome!
Feel free to open a pull request or issue.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

*Built by Safi *
---
