#!/usr/bin/env python3
"""
Test script for Yamaguchi Prefecture functionality
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import get_comprehensive_contacts, parse_address_components, calculate_distance, estimate_coordinates_from_address

def test_yamaguchi_search():
    """Test searching for contacts in Yamaguchi Prefecture"""
    print("=== Testing Yamaguchi Prefecture Search ===")
    
    # Test address in Yamaguchi (prefectural capital)
    test_address = "山口県山口市亀山町2-1"
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
                if 'distance_km' in contact:
                    print(f"    🚶 Distance: {contact['distance_km']:.1f}km")
                total_contacts += 1
        else:
            print(f"\n❌ {category}: No contacts found")
    
    print(f"\n📊 Total contacts found: {total_contacts}")
    
    # Test a few more cities
    print("\n=== Testing Other Yamaguchi Cities ===")
    
    test_cities = [
        ("山口県下関市南部町1-1", "下関市"),
        ("山口県宇部市常盤町1-7-1", "宇部市"),
        ("山口県萩市大字江向510", "萩市")
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
        else:
            print("   ❌ Address parsing failed")

if __name__ == "__main__":
    test_yamaguchi_search()
