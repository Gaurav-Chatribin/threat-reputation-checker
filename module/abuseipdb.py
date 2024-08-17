import requests
import config

def get_abuseipdb_report(ip):
    url = f'https://api.abuseipdb.com/api/v2/check'
    headers = {
        'Key': config.ABUSEIPDB_API_KEY,
        'Content-Type': 'application/json'
    }
    params = {'ipAddress': ip}
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "API request failed or invalid IP"}
