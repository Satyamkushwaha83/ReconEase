import socket
import nmap
def run(target, scan_type):
    print(f"[+] Running Vulnerability Scan on {target}")
    try:
        nm = nmap.PortScanner()
        if scan_type == "deep":
            scan_result = nm.scan(target, arguments="-sV -O")
        else:
            scan_result = nm.scan(target, arguments="-F")

        # CLI print
        print(scan_result)

        # Report ke liye return
        report = f"<h2>Vulnerability Scan Report for {target}</h2>"
        report += "<pre>" + str(scan_result) + "</pre>"
        return report
    except Exception as e:
        print(f"[!] Scan Error: {e}")
        return f"<h2>Vulnerability Scan Report for {target}</h2><p>Error: {e}</p>"
