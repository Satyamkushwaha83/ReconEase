import socket
def run(domain):
    print(f"[+] Running Enumeration on {domain}")
    ip = socket.gethostbyname(domain)

    # CLI print
    print("IP Address:", ip)

    # Report ke liye return
    report = f"<h2>Enumeration Report for {domain}</h2>"
    report += f"<p>IP Address: {ip}</p>"
    return report
