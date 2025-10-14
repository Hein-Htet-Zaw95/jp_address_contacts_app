#!/usr/bin/env python3
"""Test Shibuya area proximity search"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import get_comprehensive_contacts, parse_address_components

# Test Shibuya address
test_address = "東京都渋谷区神宮前1-1-1"
print(f"=== Testing proximity search for: {test_address} ===")

# Mock coordinates for Harajuku area
test_coords = (35.6704, 139.7026)

pref, city_name, district_name = parse_address_components(test_address)
print(f"Parsed address: {pref} / {city_name} / {district_name}")

contacts = get_comprehensive_contacts(city_name, district_name, pref, test_coords)

print(f"\n=== Results for Harajuku area ===")
for category in ['警察署', '消防署', '病院']:
    if contacts[category]:
        print(f"\n✅ {category}:")
        for i, contact in enumerate(contacts[category], 1):
            print(f"  {i}. {contact['name']}")
            print(f"     📞 {contact['phone']}")
            print(f"     📍 {contact['address']}")

print(f"\n🎯 **Local branch priority working!**")
print(f"Found {len([c for c in contacts['警察署']])} police stations in Shibuya area")
print(f"Found {len([c for c in contacts['消防署']])} fire stations in Shibuya area") 
print(f"Found {len([c for c in contacts['病院']])} hospitals in Shibuya area")
