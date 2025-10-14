#!/usr/bin/env python3
"""
Test script for complete Hiroshima Prefecture functionality including Hiroshima City wards
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import get_comprehensive_contacts, parse_address_components, calculate_distance, estimate_coordinates_from_address

def test_hiroshima_complete():
    """Test searching for contacts in all Hiroshima locations"""
    print("=== Testing Complete Hiroshima Prefecture Search ===")
    
    # Test Hiroshima City with ward
    test_address = "広島県広島市中区基町9-32"
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
            print(f"✅ {category} ({len(contacts)} found)")
            total_contacts += len(contacts)
        else:
            print(f"❌ {category}: No contacts found")
    
    print(f"\n📊 Total contacts found: {total_contacts}")
    
    # Test all Hiroshima City wards
    print("\n=== Testing All Hiroshima City Wards ===")
    
    wards = [
        ("広島県広島市中区基町9-32", "広島市", "中区"),
        ("広島県広島市東区光町2-12-8", "広島市", "東区"),
        ("広島県広島市南区皆実町1-4-46", "広島市", "南区"),
        ("広島県広島市西区福島町2-2-1", "広島市", "西区"),
        ("広島県広島市安佐南区古市1-33-14", "広島市", "安佐南区"),
        ("広島県広島市安佐北区可部4-13-13", "広島市", "安佐北区"),
        ("広島県広島市佐伯区海老園1-4-5", "広島市", "佐伯区"),
        ("広島県広島市安芸区船越南3-2-16", "広島市", "安芸区")
    ]
    
    for address, expected_city, expected_ward in wards:
        print(f"\n🎯 Testing: {address}")
        prefecture, city, district = parse_address_components(address)
        print(f"   Parsed: {city} / {district} (expected: {expected_city} / {expected_ward})")
        
        if city == expected_city and district == expected_ward:
            print("   ✅ Address parsing successful")
            coords = estimate_coordinates_from_address(address)
            contacts = get_comprehensive_contacts(city, district, prefecture, coords)
            total = sum(len(c) for c in contacts.values())
            print(f"   📊 Found {total} total contacts")
        else:
            print("   ❌ Address parsing failed")
    
    # Test major cities
    print("\n=== Testing Major Hiroshima Cities ===")
    
    cities = [
        ("広島県福山市東桜町3-5", "福山市"),
        ("広島県三原市港町3-5-1", "三原市"),
        ("広島県尾道市久保1-15-1", "尾道市"),
        ("広島県竹原市下野町3185", "竹原市"),
        ("広島県三次市十日市中2-8-1", "三次市"),
        ("広島県庄原市中本町1-10-1", "庄原市"),
        ("広島県大竹市小方1-11-1", "大竹市")
    ]
    
    for address, expected_city in cities:
        print(f"\n🎯 Testing: {address}")
        prefecture, city, district = parse_address_components(address)
        print(f"   Parsed city: {city} (expected: {expected_city})")
        
        if city == expected_city:
            print("   ✅ Address parsing successful")
            coords = estimate_coordinates_from_address(address)
            contacts = get_comprehensive_contacts(city, district, prefecture, coords)
            total = sum(len(c) for c in contacts.values())
            print(f"   📊 Found {total} total contacts")
            
            # Show a sample contact
            if contacts.get('市区町村役所'):
                city_hall = contacts['市区町村役所'][0]
                print(f"   🏛️ City Hall: {city_hall['name']} - {city_hall['phone']}")
        else:
            print("   ❌ Address parsing failed")

if __name__ == "__main__":
    test_hiroshima_complete()
