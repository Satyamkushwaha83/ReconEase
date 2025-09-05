import socket
import whois
import dns.resolver

def get_whois(domain):
    """Fetch WHOIS information"""
    try:
        w = whois.whois(domain)
        return str(w)
    except Exception as e:
        return f"[!] WHOIS lookup failed: {e}"

def get_dns_records(domain):
    """Fetch DNS records"""
    try:
        records = []
        for qtype in ["A", "MX", "NS"]:
            try:
                answers = dns.resolver.resolve(domain, qtype)
                for rdata in answers:
                    records.append(f"{qtype}: {rdata.to_text()}")
            except Exception:
                records.append(f"{qtype}: Not Found")
        return "\n".join(records)
    except Exception as e:
        return f"[!] DNS lookup failed: {e}"

def run(domain):
    print(f"[+] Running OSINT on {domain}")
    results = []

    # WHOIS
    whois_info = get_whois(domain)
    results.append("WHOIS Information:\n" + whois_info)

    # DNS
    dns_info = get_dns_records(domain)
    results.append("DNS Records:\n" + dns_info)

    final_result = "\n\n".join(results)
    return final_result
