import requests
import config

def get_virustotal_report(ip_or_domain, report_type):
    if report_type == 'ip':
        url = f'https://www.virustotal.com/api/v3/ip_addresses/{ip_or_domain}'
    elif report_type == 'domain':
        url = f'https://www.virustotal.com/api/v3/domains/{ip_or_domain}'
    else:
        return {"error": "Invalid report type"}
    
    headers = {'x-apikey': config.VIRUSTOTAL_API_KEY}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        tags = data.get("data", {}).get("attributes", {}).get("tags", [])
        details = data.get("data", {}).get("attributes", {}).get("last_analysis_stats", {})
        return {
            "tags": tags,
            "details": details,
            "data": data.get("data", {})
        }
    else:
        return {"error": "API request failed or invalid IP/domain"}
