import requests
from bs4 import BeautifulSoup

def get_whois_report(domain):
    url = f"https://whois.domaintools.com/{domain}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        try:
            data = {
                "Domain Name": soup.find('div', {'class': 'domain_name'}).text.strip(),
                "Registrant Organization": soup.find('div', {'class': 'registrant_organization'}).text.strip(),
                "Updated Date": soup.find('div', {'class': 'updated_date'}).text.strip(),
                "Creation Date": soup.find('div', {'class': 'creation_date'}).text.strip(),
                "Admin State/Province": soup.find('div', {'class': 'admin_state_province'}).text.strip(),
                "Admin Country": soup.find('div', {'class': 'admin_country'}).text.strip()
            }
            return data
        except AttributeError:
            return {"error": "No WHOIS data found"}
    else:
        return {"error": "Failed to retrieve data"}
