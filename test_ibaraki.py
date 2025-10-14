#!/usr/bin/env python3
"""
Test script for Ibaraki Prefecture functionality
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import get_comprehensive_contacts, parse_address_components, calculate_distance, estimate_coordinates_from_address

def test_ibaraki_cities():
    """Test searching for contacts in Ibaraki cities"""
    print("=== Testing Ibaraki Prefecture Cities ===")
    
    # Test major Ibaraki cities
    cities = [
        ("茨城県水戸市中央1-4-1", "水戸市", "県庁所在地"),
        ("茨城県日立市助川町1-1-1", "日立市", "工業都市"),
        ("茨城県土浦市大和町9-1", "土浦市", "湖北地域中心地"),
        ("茨城県ひたちなか市東石川2-10-1", "ひたちなか市", "港湾都市"),
        ("茨城県古河市長谷町38-18", "古河市", "西部地域"),
        ("茨城県石岡市石岡1-1-1", "石岡市", "県南地域"),
        ("茨城県結城市中央町2-3", "結城市", "紬の町"),
        ("茨城県龍ケ崎市3710", "龍ケ崎市", "龍ヶ崎"),
        ("茨城県下妻市本城町2-22", "下妻市", "下妻"),
        ("茨城県常総市水海道諏訪町3222-3", "常総市", "常総"),
        ("茨城県常陸太田市金井町3690", "常陸太田市", "常陸太田"),
        ("茨城県高萩市本町1-100-1", "高萩市", "高萩"),
        ("茨城県北茨城市磯原町磯原1630", "北茨城市", "北茨城"),
        ("茨城県笠間市中央3-2-1", "笠間市", "笠間焼"),
        ("茨城県取手市寺田5139", "取手市", "取手"),
        ("茨城県牛久市中央3-15-1", "牛久市", "牛久"),
        ("茨城県つくば市研究学園1-1-1", "つくば市", "科学技術都市")
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

    # Test progressive search with a specific address
    print(f"\n=== Testing Progressive Search in Mito ===")
    test_address = "茨城県水戸市中央1-4-1"
    prefecture, city, district = parse_address_components(test_address)
    coords = estimate_coordinates_from_address(test_address)
    
    print(f"Test address: {test_address}")
    print(f"Coordinates: {coords}")
    
    comprehensive_contacts = get_comprehensive_contacts(city, district, prefecture, coords)
    
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
    test_ibaraki_cities()
