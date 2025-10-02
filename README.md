<<<<<<< HEAD
# ReconEase 🕵️‍♂️

# ReconEase is an all-in-one Python-based ethical hacking tool for:

# OSINT (Open Source Intelligence / information gathering)

 # Vulnerability Scanning

 # Enumeration

# It is designed to help penetration testers, security auditors, and hobbyist ethical hackers assess the security of systems and networks.

⚙️ Installation
# 1. Clone the repository
git clone https://github.com/Satyamkushwaha83/ReconEase.git
cd ReconEase

# 2. Install Python dependencies
pip install -r requirements.txt


# ⚠️ Note: For Vulnerability Scanning, make sure nmap is installed and in your system PATH.
# On Linux (Kali / Ubuntu):

sudo apt install nmap -y

🚀 Usage
1. Show Help
# Display all available options
python main.py --help

2. CLI Mode (Terminal)
OSINT Only
# Gather WHOIS, DNS, Subdomains, Emails
python main.py -d example.com --osint

Vulnerability Scan
# Scan by domain
python main.py -d example.com --vuln

# Scan by IP with light scan (fast)
python main.py -t 192.168.1.1 --vuln --scan light

# Scan by IP with deep scan (detailed, slower)
python main.py -t 192.168.1.1 --vuln --scan deep

Enumeration Only
# Banner grabbing, Service versions, OS details
python main.py -d example.com --enum

Full Scan (OSINT + Vulnerability + Enumeration)
python main.py -d example.com --all

Scan Modes
# Light scan (fast, basic info)
python main.py -d example.com --all --scan light

# Deep scan (detailed, more info)
python main.py -d example.com --all --scan deep

3. Reports & Privacy
Save Report to File
# Save report as TXT
python main.py -d example.com --all -o reports/example_report.txt

# Save report as HTML
python main.py -d example.com --all -o reports/example_report.html

Privacy Mode
# No local logs; only report file will be generated
python main.py -d example.com --all --privacy

4. Dashboard Mode (Web UI)
Launch Dashboard
python dashboard.py


Open in browser: http://127.0.0.1:5000/

Enter domain or IP

Select OSINT / Vulnerability / Enumeration / All

View results on the page

Download options available: TXT / HTML





















=======
# ReconEase
ReconEase is a lightweight reconnaissance tool for security researchers and pentesters. It offers OSINT (WHOIS, DNS, subdomains, emails), vulnerability scanning, and enumeration. Supports both CLI and interactive dashboard with exportable TXT/HTML reports.
>>>>>>> ce34bf05dd8213f57665c021c1fd2b9129b6ce9b
