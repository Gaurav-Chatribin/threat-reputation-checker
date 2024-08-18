import requests

def check_ip_reputation(ip, api_key):
    url = "https://api.criminalip.io/v1/asset/ip/report"
    headers = {
        "x-api-key": api_key
    }
    params = {
        "ip": ip,
        "full": "true"  # Ensures full data is returned to access the required fields
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        
        # Extracting only the required fields
        inbound_score = data.get("score", {}).get("inbound", "N/A")
        outbound_score = data.get("score", {}).get("outbound", "N/A")
        is_malicious = data.get("issues", {}).get("is_malicious", "N/A")
        tags = data.get("port", {}).get("data", [{}])[0].get("tags", ["N/A"])
        abuse_record = data.get("user_search_count", "N/A")
        
        return {
            "inbound_score": inbound_score,
            "outbound_score": outbound_score,
            "is_malicious": is_malicious,
            "tags": tags,
            "abuse_record": abuse_record
        }

    except requests.exceptions.HTTPError as http_err:
        return {"error": f"HTTP error occurred: {http_err}"}
    except Exception as err:
        return {"error": f"An error occurred: {err}"}
