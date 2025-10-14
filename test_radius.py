#!/usr/bin/env python3
"""Test 10km radius filtering functionality"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import get_comprehensive_contacts, parse_address_components, calculate_distance, estimate_coordinates_from_address

def test_10km_radius():
    # Test address in Tokyo
    test_address = "東京都足立区竹の塚6-8-1"
    print(f"=== Testing 10km radius for: {test_address} ===")
    
    # Mock coordinates for Takenotsuka area  
    test_coords = (35.8012, 139.7906)
    print(f"Test coordinates: {test_coords}")
    
    pref, city_name, district_name = parse_address_components(test_address)
    print(f"Parsed: {pref} / {city_name} / {district_name}")
    
    # Get contacts with 10km radius filtering
    contacts = get_comprehensive_contacts(city_name, district_name, pref, test_coords)
    
    print(f"\n=== Results within 10km radius ===")
    
    for category in ['労基署', '警察署', '消防署', '病院']:
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
                        if calc_distance > 10:
                            print(f"     ⚠️  WARNING: Distance exceeds 10km limit!")
                print()
        else:
            print(f"\n❌ {category}: No contacts found within 10km")
    
    print("\n=== Distance Filter Test Complete ===")
    total_contacts = sum(len(contact_list) for contact_list in contacts.values())
    print(f"Total contacts found within 10km: {total_contacts}")

if __name__ == "__main__":
    test_10km_radius()
