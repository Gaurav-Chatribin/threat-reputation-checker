import requests
from config import ABUSEIPDB_API_KEY

def get_blacklist_abuse_confidence(ip_address):
    url = 'https://api.abuseipdb.com/api/v2/blacklist'
    headers = {
        'Key': ABUSEIPDB_API_KEY,
        'Accept': 'application/json'
    }
    params = {
        'confidenceMinimum': 90
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json().get('data', [])
        for entry in data:
            if entry['ipAddress'] == ip_address:
                return entry.get('abuseConfidenceScore', 'N/A')
        return 'N/A'
    else:
        print(f"Failed to retrieve blacklist data: {response.status_code} - {response.text}")
        return 'N/A'

def check_ip(ip_address, max_age_days=90):
    check_url = 'https://api.abuseipdb.com/api/v2/check'
    check_headers = {
        'Key': ABUSEIPDB_API_KEY,
        'Accept': 'application/json'
    }
    check_params = {
        'ipAddress': ip_address,
        'maxAgeInDays': max_age_days,
        'verbose': True
    }

    check_response = requests.get(check_url, headers=check_headers, params=check_params)

    if check_response.status_code == 200:
        data = check_response.json().get('data', {})
        if not data:
            print(f"No data found for IP address {ip_address}.")
            return None

        # Get blacklist abuse confidence
        abuse_confidence = get_blacklist_abuse_confidence(ip_address)

        # Combine data with abuse confidence score
        data['abuseConfidenceScore'] = abuse_confidence

        return data
    else:
        print(f"Failed to retrieve data: {check_response.status_code} - {check_response.text}")
        return None

def get_abuseipdb_report(ip_address):
    return check_ip(ip_address)
