from flask import Flask, request, render_template
import re
from module.virustotal import get_virustotal_report
from module.abuseipdb import get_abuseipdb_report
from module.whois_lookup import get_whois_report

app = Flask(__name__)

def is_ip(input_string):
    ip_pattern = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    return bool(ip_pattern.match(input_string))

def is_domain(input_string):
    domain_pattern = re.compile(r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.[A-Za-z]{2,6}$")
    return bool(domain_pattern.match(input_string))

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    virustotal_report = None
    abuseipdb_report = None
    whois_report = None

    if request.method == 'POST':
        ip_or_domain = request.form.get('ip_or_domain')
        report_type = request.form.get('report_type')

        if not ip_or_domain:
            return render_template('index.html', error="Please enter an IP or domain.")
        
        if report_type == 'ip':
            if not is_ip(ip_or_domain):
                if is_domain(ip_or_domain):
                    return render_template('index.html', error="You have selected the IP type, but entered a domain name. Please enter a valid IP address (e.g., 192.168.1.1).")
                return render_template('index.html', error="Invalid IP address. Please enter a valid IP (e.g., 192.168.1.1).")
            virustotal_report = get_virustotal_report(ip_or_domain, report_type)
            abuseipdb_report = get_abuseipdb_report(ip_or_domain)
        
        elif report_type == 'domain':
            if not is_domain(ip_or_domain):
                if is_ip(ip_or_domain):
                    return render_template('index.html', error="You have selected the domain type, but entered an IP address. Please enter a valid domain name (e.g., example.com).")
                return render_template('index.html', error="Invalid domain name. Please enter a valid domain (e.g., example.com).")
            virustotal_report = get_virustotal_report(ip_or_domain, report_type)
            abuseipdb_report = None
            whois_report = get_whois_report(ip_or_domain)
        
        else:
            return render_template('index.html', error="Invalid report type selected.")
        
        return render_template('index.html', virustotal_report=virustotal_report, abuseipdb_report=abuseipdb_report, whois_report=whois_report)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
