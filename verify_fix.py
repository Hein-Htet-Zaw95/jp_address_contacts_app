#!/usr/bin/env python3
"""
Simple verification script for the fixed police station search
"""

import sys
import os

# Add the parent directory to sys.path to import from app.py
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import parse_address_components, estimate_coordinates_from_address, get_comprehensive_contacts

def verify_fix():
    """Verify the fix is working"""
    
    address = "東京都練馬区石神井町8‐10‐16"
    prefecture, city, district = parse_address_components(address)
    coords = estimate_coordinates_from_address(address)
    contacts = get_comprehensive_contacts(city, district, prefecture, coords)
    
    police_stations = contacts.get('警察署', [])
    
    print("✅ Fix Verification:")
    print(f"Address: {address}")
    print(f"Police stations found: {len(police_stations)}")
    
    if police_stations:
        closest = police_stations[0]
        print(f"Closest: {closest['name']} ({closest.get('distance_km', '?')}km)")
        
        if closest['name'] == '石神井警察署':
            print("🎯 SUCCESS: 石神井警察署 is now the closest!")
        else:
            print("❌ ISSUE: 石神井警察署 is not the closest")
    else:
        print("❌ No police stations found")

if __name__ == "__main__":
    verify_fix()
