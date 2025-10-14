#!/usr/bin/env python3
"""
Test script for Hiroshima Prefecture functionality
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import get_comprehensive_contacts, parse_address_components, calculate_distance, estimate_coordinates_from_address

def test_hiroshima_search():
    """Test searching for contacts in Hiroshima Prefecture"""
    print("=== Testing Hiroshima Prefecture Search ===")
    
    # Test address in Kure City
    test_address = "広島県呉市中央4-1-6"
    print(f"Test address: {test_address}")
    
    # Parse address components
    prefecture, city, district = parse_address_components(test_address)
    print(f"Parsed: {prefecture} / {city} / {district}")
    
    # Estimate coordinates
    coords = estimate_coordinates_from_address(test_address)
    if coords:
        print(f"Estimated coordinates: {coords[0]:.6f}, {coords[1]:.6f}")
    else:
        print("Could not estimate coordinates")
    
    # Get comprehensive contacts
    comprehensive_contacts = get_comprehensive_contacts(city, district, prefecture, coords)
    
    print("\n=== Search Results ===")
    total_contacts = 0
    for category, contacts in comprehensive_contacts.items():
        if contacts:
            print(f"\n✅ {category} ({len(contacts)} found):")
            for contact in contacts:
                print(f"  • {contact['name']}")
                print(f"    📞 {contact['phone']}")
                print(f"    📍 {contact['address']}")
                if 'distance_km' in contact and contact['distance_km'] is not None:
                    print(f"    🚶 Distance: {contact['distance_km']:.1f}km")
                total_contacts += 1
        else:
            print(f"\n❌ {category}: No contacts found")
    
    print(f"\n📊 Total contacts found: {total_contacts}")
    
    # Test the specific cities mentioned
    print("\n=== Testing Specific Hiroshima Cities ===")
    
    test_cities = [
        ("広島県呉市中央4-1-6", "呉市"),
        ("広島県東広島市西条栄町8-29", "東広島市"),
        ("広島県安芸高田市吉田町吉田791-2", "安芸高田市"),
        ("広島県廿日市市下平良1-11-1", "廿日市市"),
        ("広島県府中市府川町315", "府中市")
    ]
    
    for address, expected_city in test_cities:
        print(f"\n🎯 Testing: {address}")
        prefecture, city, district = parse_address_components(address)
        print(f"   Parsed city: {city} (expected: {expected_city})")
        
        if city == expected_city:
            print("   ✅ Address parsing successful")
            # Quick check if we have data
            coords = estimate_coordinates_from_address(address)
            contacts = get_comprehensive_contacts(city, district, prefecture, coords)
            total = sum(len(c) for c in contacts.values())
            print(f"   📊 Found {total} total contacts")
            
            # Show some specific contacts
            if contacts.get('警察署'):
                police = contacts['警察署'][0]
                print(f"   🚔 Police: {police['name']} - {police['phone']}")
            if contacts.get('病院'):
                hospital = contacts['病院'][0]
                print(f"   🏥 Hospital: {hospital['name']} - {hospital['phone']}")
        else:
            print("   ❌ Address parsing failed")

if __name__ == "__main__":
    test_hiroshima_search()
