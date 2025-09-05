import json

def save_json(file_path, data):
    try:
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"[!] Error saving JSON report: {e}")

import socket
import argparse
import os
from modules import osint, vuln_scan, enumeration

def save_output(file_path, content, privacy=False, html=False):
    """Save results into file (supports txt or html)."""
    try:
        mode = "a" if not html else "w"
        with open(file_path, mode, encoding="utf-8") as f:
            if html:
                f.write("<html><body>" + content + "</body></html>")
            else:
                f.write(content + "\n")
    except Exception as e:
        print(f"[!] Error saving report: {e}")
    if privacy:
        # If privacy mode, overwrite file with empty content after use
        open(file_path, "w").close()

def main():
    parser = argparse.ArgumentParser(
        description="ReconEase - OSINT, Vulnerability Scanning & Enumeration Tool"
    )
    parser.add_argument("-d", "--domain", help="Target domain (example.com)")
    parser.add_argument("-t", "--target", help="Target IP or domain for scanning")
    parser.add_argument("--osint", action="store_true", help="Run OSINT only")
    parser.add_argument("--vuln", action="store_true", help="Run Vulnerability Scan only")
    parser.add_argument("--enum", action="store_true", help="Run Enumeration only")
    parser.add_argument("--all", action="store_true", help="Run full scan (OSINT + Vuln + Enum)")
    parser.add_argument("--scan", choices=["light", "deep"], help="Choose scan type")
    parser.add_argument("--dashboard", action="store_true", help="Launch Web Dashboard (coming soon)")
    parser.add_argument("--privacy", action="store_true", help="Enable Privacy Mode (no logs stored)")
    parser.add_argument("-o", "--output", help="Save results to file (txt or html)")

    args = parser.parse_args()

    report_file = args.output if args.output else None
    is_html = report_file.endswith(".html") if report_file else False

    if report_file:
        os.makedirs(os.path.dirname(report_file), exist_ok=True)
        open(report_file, "w").close()  # clear file first

    results = []

    # Run OSINT
    if args.osint:
        result = osint.run(args.domain)
        results.append(result)

    # Run Vulnerability Scan
    if args.vuln:
        target = args.target if args.target else args.domain
        result = vuln_scan.run(target, args.scan)
        results.append(result)

    # Run Enumeration
    if args.enum:
        target = args.target if args.target else args.domain
        result = enumeration.run(target)
        results.append(result)

    # Run Full Scan
    if args.all:
        if args.domain:
            results.append(osint.run(args.domain))
        target = args.target if args.target else args.domain
        if target:
            results.append(vuln_scan.run(target, args.scan))
            results.append(enumeration.run(target))

    if results and report_file:
        final_report = "\n\n".join(results)
        save_output(report_file, final_report, args.privacy, html=is_html)
        print(f"[+] Report saved to {report_file}")

    elif not (args.osint or args.vuln or args.enum or args.all):
        parser.print_help()

if __name__ == "__main__":
    main()
