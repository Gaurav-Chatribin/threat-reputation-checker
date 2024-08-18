import whois

def get_whois_report(domain):
    try:
        whois_info = whois.whois(domain)
        return {
            'domain_name': whois_info.domain_name[0] if whois_info.domain_name else '',
            'registrant_organization': whois_info.registrar if whois_info.registrar else '',
            'updated_date': whois_info.updated_date[0].strftime('%Y-%m-%d %H:%M:%S') if whois_info.updated_date else '',
            'creation_date': whois_info.creation_date[0].strftime('%Y-%m-%d %H:%M:%S') if whois_info.creation_date else '',
            'admin_state_province': whois_info.state if whois_info.state else '',
            'admin_country': whois_info.country if whois_info.country else '',
        }
    except Exception as e:
        return {'error': str(e)}
