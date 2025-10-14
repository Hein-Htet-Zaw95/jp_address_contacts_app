#!/usr/bin/env python3
# Test the actual get_comprehensive_contacts function

import re
import sys
import os
sys.path.append(os.path.dirname(__file__))

from app import parse_address_components, get_comprehensive_contacts, CONTACT_DATABASE

# Test the problematic address
test_address = "東京都中央区築地3-1005-15"
pref, city, district = parse_address_components(test_address)

print(f"Address: {test_address}")
print(f"Prefecture: '{pref}'")
print(f"City: '{city}'") 
print(f"District: '{district}'")

# Test the actual function
contacts = get_comprehensive_contacts(city, district, pref)

print(f"\nContacts found:")
total_contacts = sum(len(contacts[cat]) for cat in contacts)
print(f"Total contacts: {total_contacts}")

for category, contact_list in contacts.items():
    if contact_list:
        print(f"{category}: {len(contact_list)} contacts")
        for contact in contact_list:
            print(f"  - {contact.get('name', 'N/A')}: {contact.get('phone', 'N/A')}")

# Check if 中央区 exists in database
print(f"\nDatabase structure check:")
print(f"Prefecture '{pref}' exists: {pref in CONTACT_DATABASE}")
if pref in CONTACT_DATABASE:
    print(f"City '{city}' exists: {city in CONTACT_DATABASE[pref]}")
    if city in CONTACT_DATABASE[pref]:
        print(f"City data keys: {list(CONTACT_DATABASE[pref][city].keys())}")
        if "" in CONTACT_DATABASE[pref][city]:
            sample_data = CONTACT_DATABASE[pref][city][""]
            print(f"Sample categories in empty district: {list(sample_data.keys())}")
