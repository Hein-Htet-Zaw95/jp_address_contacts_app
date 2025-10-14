#!/usr/bin/env python3
"""Test progressive radius search functionality"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import get_comprehensive_contacts, parse_address_components, calculate_distance, estimate_coordinates_from_address

def test_progressive_radius():
    # Test address in Tokyo
    test_address = "東京都渋谷区神宮前1-1-1"
    print(f"=== Testing Progressive Radius Search: {test_address} ===")
    
    # Coordinates for Harajuku area
    test_coords = (35.6704, 139.7026)
    print(f"User coordinates: {test_coords}")
    
    pref, city_name, district_name = parse_address_components(test_address)
    print(f"Parsed: {pref} / {city_name} / {district_name}")
    
    # Get contacts with progressive radius search
    contacts = get_comprehensive_contacts(city_name, district_name, pref, test_coords)
    
    print(f"\n=== Progressive Radius Search Results ===")
    print("Search radii: 1km → 3km → 5km → 8km → 10km → 13km → 15km → 18km")
    
    # Test each category
    for category in ['警察署', '消防署', '病院']:
        if contacts[category]:
            print(f"\n✅ {category} ({len(contacts[category])} found):")
            
            # Collect distances for analysis
            distances = []
            
            for i, contact in enumerate(contacts[category], 1):
                name = contact.get('name', 'N/A')
                address = contact.get('address', 'N/A')
                distance = contact.get('distance_km', 'N/A')
                
                print(f"  {i}. {name}")
                print(f"     📍 {address}")
                if distance != 'N/A' and distance is not None:
                    print(f"     🚶 {distance}km away")
                    distances.append(distance)
                    
                    # Determine which radius tier this falls into
                    radii = [1, 3, 5, 8, 10, 13, 15, 18]
                    tier = next((r for r in radii if distance <= r), "18+")
                    print(f"     📍 Found in {tier}km tier")
                else:
                    print(f"     🚶 Distance not calculated")
                print()
            
            # Show distance distribution
            if distances:
                min_dist = min(distances)
                max_dist = max(distances)
                avg_dist = sum(distances) / len(distances)
                print(f"   📊 Distance range: {min_dist}km - {max_dist}km (avg: {avg_dist:.1f}km)")
                
                # Verify progressive search worked (closest should be found first)
                is_sorted = all(distances[i] <= distances[i+1] for i in range(len(distances)-1))
                if is_sorted:
                    print(f"   ✅ Results properly sorted by distance")
                else:
                    print(f"   ⚠️  Warning: Results not perfectly sorted by distance")
        else:
            print(f"\n❌ {category}: No contacts found")
    
    print(f"\n=== Testing Different Scenarios ===")
    
    # Test very specific location (should find in 1km tier)
    print(f"\n🎯 **Nearest facility analysis**:")
    for category in ['警察署', '消防署']:
        if contacts[category] and contacts[category][0].get('distance_km'):
            nearest_distance = contacts[category][0]['distance_km']
            nearest_name = contacts[category][0]['name']
            
            if nearest_distance <= 1:
                tier = "1km (Excellent - within walking distance)"
            elif nearest_distance <= 3:
                tier = "3km (Very good - short trip)"
            elif nearest_distance <= 5:
                tier = "5km (Good - reasonable distance)"
            elif nearest_distance <= 8:
                tier = "8km (Acceptable - moderate distance)"
            else:
                tier = f"{nearest_distance}km (Far - longer trip required)"
            
            print(f"   {category}: {nearest_name} at {nearest_distance}km - {tier}")
    
    print(f"\n✅ Progressive radius search test complete!")

if __name__ == "__main__":
    test_progressive_radius()
