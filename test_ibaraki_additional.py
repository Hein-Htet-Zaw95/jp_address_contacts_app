#!/usr/bin/env python3
"""
Test script for additional Ibaraki Prefecture cities
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import get_comprehensive_contacts, parse_address_components, calculate_distance, estimate_coordinates_from_address

def test_additional_ibaraki_cities():
    """Test searching for contacts in additional Ibaraki cities"""
    print("=== Testing Additional Ibaraki Prefecture Cities ===")
    
    # Test the newly added Ibaraki cities
    cities = [
        ("茨城県鹿嶋市平井1187-1", "鹿嶋市", "サッカーの町"),
        ("茨城県潮来市辻626", "潮来市", "水郷の町"),
        ("茨城県守谷市大柏950-1", "守谷市", "住みやすさ日本一"),
        ("茨城県常陸大宮市中富町3135-6", "常陸大宮市", "山間部の中心地"),
        ("茨城県那珂市福田1819-5", "那珂市", "静穏の郷"),
        ("茨城県筑西市下中山732-1", "筑西市", "しもだて"),
        ("茨城県坂東市岩井4365", "坂東市", "将門の里"),
        ("茨城県稲敷市江戸崎甲1626", "稲敷市", "江戸崎カボチャ"),
        ("茨城県かすみがうら市上土田461", "かすみがうら市", "霞ヶ浦の恵み"),
        ("茨城県行方市山田2564-10", "行方市", "なめがた"),
        ("茨城県鉾田市鉾田1444-1", "鉾田市", "メロンの里"),
        ("茨城県神栖市溝口4991-5", "神栖市", "工業都市")
    ]
    
    for address, expected_city, description in cities:
        print(f"\n🎯 Testing: {address} ({description})")
        prefecture, city, district = parse_address_components(address)
        print(f"   Parsed: {prefecture} / {city} / {district}")
        
        if city == expected_city:
            print("   ✅ Address parsing successful")
            coords = estimate_coordinates_from_address(address)
            if coords:
                print(f"   📍 Coordinates: {coords[0]:.4f}, {coords[1]:.4f}")
            
            contacts = get_comprehensive_contacts(city, district, prefecture, coords)
            total = sum(len(c) for c in contacts.values())
            print(f"   📊 Found {total} total contacts")
            
            # Show a sample contact from each major category
            important_categories = ['市区町村役所', '警察署', '消防署', '病院']
            for category in important_categories:
                if contacts.get(category):
                    contact = contacts[category][0]
                    print(f"   {category}: {contact['name']} - {contact['phone']}")
            
            if total == 0:
                print("   ⚠️ WARNING: No contacts found!")
        else:
            print(f"   ❌ Address parsing failed - expected {expected_city}, got {city}")

    # Test specific functionality for special cities
    print(f"\n=== Testing Special Features ===")
    
    # Test Kashima - famous for soccer
    print(f"\n🏟️ Testing Kashima (Soccer City)")
    test_address = "茨城県鹿嶋市平井1187-1"
    prefecture, city, district = parse_address_components(test_address)
    coords = estimate_coordinates_from_address(test_address)
    contacts = get_comprehensive_contacts(city, district, prefecture, coords)
    
    print(f"Kashima City Hall: {contacts['市区町村役所'][0]['phone'] if contacts.get('市区町村役所') else 'Not found'}")
    print(f"Kashima Hospital: {contacts['病院'][0]['name'] if contacts.get('病院') else 'Not found'}")
    
    # Test Kamisu - industrial city
    print(f"\n🏭 Testing Kamisu (Industrial City)")
    test_address = "茨城県神栖市溝口4991-5"
    prefecture, city, district = parse_address_components(test_address)
    coords = estimate_coordinates_from_address(test_address)
    contacts = get_comprehensive_contacts(city, district, prefecture, coords)
    
    print(f"Kamisu City contacts: {sum(len(c) for c in contacts.values())} total")
    if contacts.get('病院'):
        print(f"Kamisu Hospital: {contacts['病院'][0]['name']}")
    
    # Test progressive search in a smaller city
    print(f"\n=== Testing Progressive Search in Hokota ===")
    test_address = "茨城県鉾田市鉾田1444-1"
    prefecture, city, district = parse_address_components(test_address)
    coords = estimate_coordinates_from_address(test_address)
    
    comprehensive_contacts = get_comprehensive_contacts(city, district, prefecture, coords)
    
    print(f"Test address: {test_address}")
    print(f"Coordinates: {coords}")
    
    print("\n=== Progressive Search Results ===")
    for category, contacts in comprehensive_contacts.items():
        if contacts:
            print(f"✅ {category} ({len(contacts)} found)")
            for i, contact in enumerate(contacts[:2]):  # Show first 2 results
                tier = contact.get('tier', 'N/A')
                distance = contact.get('distance_km', 'N/A')
                print(f"   {i+1}. {contact['name']} - Tier {tier} ({distance}km)")
        else:
            print(f"❌ {category}: No contacts found")

if __name__ == "__main__":
    test_additional_ibaraki_cities()
