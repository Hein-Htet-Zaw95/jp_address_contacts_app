#!/usr/bin/env python3
"""Test the proximity-based search functionality"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import get_comprehensive_contacts, parse_address_components, geocode_gsi

def test_proximity_search():
    # Test addresses
    test_addresses = [
        "東京都足立区竹の塚6-8-1",  # Near Takenotsuka area
        "東京都渋谷区神宮前1-1-1",   # Near Harajuku area  
        "神奈川県横浜市鶴見区鶴見中央2-5-5",  # Yokohama Tsurumi
        "千葉市中央区中央3-10-8"    # Chiba central
    ]
    
    for address in test_addresses:
        print(f"\n=== Testing address: {address} ===")
        
        # Parse address
        pref, city_name, district_name = parse_address_components(address)
        print(f"Parsed: {pref} / {city_name} / {district_name}")
        
        # Get coordinates 
        coords = geocode_gsi(address)
        if coords:
            lat, lon = coords
            print(f"Coordinates: {lat:.6f}, {lon:.6f}")
        else:
            print("Geocoding failed")
            coords = None
        
        # Get contacts with proximity search
        contacts = get_comprehensive_contacts(city_name, district_name, pref, coords)
        
        print(f"Found contacts:")
        for category, contact_list in contacts.items():
            if contact_list:
                print(f"  {category}: {len(contact_list)} contacts")
                for contact in contact_list:
                    print(f"    - {contact.get('name', 'N/A')}")
            else:
                print(f"  {category}: No contacts")

if __name__ == "__main__":
    test_proximity_search()
