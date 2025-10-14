#!/usr/bin/env python3
# Debug script to test address parsing

import re
from typing import Tuple

def parse_address_components(address: str) -> Tuple[str, str, str]:
    """Parse Japanese address to extract prefecture, city, and district"""
    clean_addr = re.sub(r'^〒?\d{3}-?\d{4}\s*', '', address)
    
    # Extract prefecture
    pref_match = re.search(r'(東京都|北海道|京都府|大阪府|[^都道府県]*[都道府県])', clean_addr)
    prefecture = pref_match.group(1) if pref_match else ""
    
    # Remove prefecture from address
    addr_without_pref = clean_addr.replace(prefecture, "") if prefecture else clean_addr
    
    # Extract city (市区町村)
    city_match = re.search(r'([^市区町村]*[市区町村])', addr_without_pref)
    city = city_match.group(1) if city_match else ""
    
    # Remove city from address to get district
    addr_without_city = addr_without_pref.replace(city, "") if city else addr_without_pref
    
    # Extract district (区) - only the district name without city prefix
    district_match = re.search(r'([^区]*区)', addr_without_city)
    district = district_match.group(1) if district_match else ""
    
    return prefecture, city, district

# Test the address
test_address = "東京都中央区築地3-1005-15"
pref, city, district = parse_address_components(test_address)

print(f"Address: {test_address}")
print(f"Prefecture: '{pref}'")
print(f"City: '{city}'")
print(f"District: '{district}'")

# Test if 中央区 is in the database structure
CONTACT_DATABASE_SAMPLE = {
    "東京都": {
        "中央区": {
            "": {
                "労基署": [{"name": "中央労働基準監督署", "phone": "03-5547-1879"}]
            }
        }
    }
}

print(f"\nDatabase check:")
print(f"Prefecture '{pref}' in database: {pref in CONTACT_DATABASE_SAMPLE}")
if pref in CONTACT_DATABASE_SAMPLE:
    print(f"City '{city}' in database: {city in CONTACT_DATABASE_SAMPLE[pref]}")
    if city in CONTACT_DATABASE_SAMPLE[pref]:
        print(f"District key '{district}' in city data: {district in CONTACT_DATABASE_SAMPLE[pref][city]}")
        print(f"Empty district key '' in city data: {'' in CONTACT_DATABASE_SAMPLE[pref][city]}")
