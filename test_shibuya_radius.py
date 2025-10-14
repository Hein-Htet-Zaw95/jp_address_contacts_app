#!/usr/bin/env python3
"""Test 10km radius filtering with Shibuya address"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import get_comprehensive_contacts, parse_address_components, calculate_distance, estimate_coordinates_from_address

def test_shibuya_radius():
    # Test address in Shibuya (should exclude far places like Chiba, distant Saitama)
    test_address = "東京都渋谷区神宮前1-1-1"
    print(f"=== Testing 10km radius for: {test_address} ===")
    
    # Coordinates for Harajuku area
    test_coords = (35.6704, 139.7026)
    print(f"Test coordinates: {test_coords}")
    
    pref, city_name, district_name = parse_address_components(test_address)
    print(f"Parsed: {pref} / {city_name} / {district_name}")
    
    # Get contacts with 10km radius filtering
    contacts = get_comprehensive_contacts(city_name, district_name, pref, test_coords)
    
    print(f"\n=== Results within 10km of Harajuku ===")
    
    for category in ['警察署', '消防署', '病院']:
        if contacts[category]:
            print(f"\n✅ {category} ({len(contacts[category])} found):")
            
            for i, contact in enumerate(contacts[category], 1):
                name = contact.get('name', 'N/A')
                address = contact.get('address', 'N/A')
                distance = contact.get('distance_km', 'N/A')
                
                print(f"  {i}. {name}")
                print(f"     📍 {address}")
                if distance != 'N/A' and distance is not None:
                    print(f"     🚶 {distance}km away")
                    if distance > 10:
                        print(f"     ⚠️  WARNING: Exceeds 10km limit!")
                else:
                    print(f"     🚶 Distance not calculated")
                
                # Verify distance calculation
                if address != 'N/A':
                    estimated_coords = estimate_coordinates_from_address(address)
                    if estimated_coords:
                        calc_distance = calculate_distance(
                            test_coords[0], test_coords[1],
                            estimated_coords[0], estimated_coords[1]
                        )
                        print(f"     ✓ Verified distance: {calc_distance:.1f}km")
                print()
        else:
            print(f"\n❌ {category}: No contacts found within 10km")
    
    # Test some distant locations to verify they're excluded
    print(f"\n=== Testing exclusion of distant locations ===")
    distant_locations = [
        ("千葉市", (35.6074, 140.1065)),
        ("さいたま市", (35.8617, 139.6455)),
        ("横浜市", (35.4437, 139.6377))
    ]
    
    for location, coords in distant_locations:
        distance = calculate_distance(test_coords[0], test_coords[1], coords[0], coords[1])
        status = "✅ Should be included" if distance <= 10 else "❌ Should be excluded"
        print(f"{location}: {distance:.1f}km away - {status}")
    
    print("\n=== Distance Filter Test Complete ===")
    total_contacts = sum(len(contact_list) for contact_list in contacts.values())
    print(f"Total contacts found within 10km: {total_contacts}")

if __name__ == "__main__":
    test_shibuya_radius()
