#!/usr/bin/env python3
# Test exact address format

import sys
import os
sys.path.append(os.path.dirname(__file__))

from app import parse_address_components, get_comprehensive_contacts, geocode_gsi, assemble_results

# Test different variations of the problematic address
test_addresses = [
    "東京都中央区築地3-1005-15",  # Original
    "東京都中央区築地3-10-5-15",  # Alternative format
    "東京都中央区築地3丁目10-5-15",  # With 丁目
    "東京都中央区築地3-10-5",     # Shorter version
    "東京都中央区築地",          # Just the area
]

for i, address in enumerate(test_addresses, 1):
    print(f"\n=== Test {i}: {address} ===")
    
    # Test parsing
    pref, city, district = parse_address_components(address)
    print(f"Parsed: {pref} | {city} | {district}")
    
    # Test contacts
    contacts = get_comprehensive_contacts(city, district, pref)
    total = sum(len(contacts[cat]) for cat in contacts)
    print(f"Contacts found: {total}")
    
    # Test DataFrame
    df = assemble_results(contacts)
    print(f"DataFrame rows: {len(df)}")
    
    if len(df) > 0:
        print("✅ SUCCESS")
    else:
        print("❌ FAILED - Empty results")

print("\n" + "="*50)
print("If any of these work, the issue might be with the exact address format.")
