from flask import Flask, render_template, request, send_file
import os
from modules import osint, vuln_scan, enumeration

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = {}
    domain = ""
    if request.method == "POST":
        domain = request.form.get("domain")
        if domain:
            # Run scans
            results["osint"] = osint.run(domain)
            results["vuln"] = vuln_scan.run(domain, "light")
            results["enum"] = enumeration.run(domain)

            # Save reports
            os.makedirs("reports", exist_ok=True)
            with open("reports/report.txt", "w") as f:
                f.write("\n\n".join(results.values()))
            with open("reports/report.html", "w") as f:
                f.write("<br><br>".join(results.values()))
    return render_template("index.html", results=results, domain=domain)

@app.route("/download/<fmt>")
def download(fmt):
    if fmt == "txt":
        return send_file("reports/report.txt", as_attachment=True)
    elif fmt == "html":
        return send_file("reports/report.html", as_attachment=True)
    else:
        return "Invalid format", 400

if __name__ == "__main__":
    app.run(debug=True)
