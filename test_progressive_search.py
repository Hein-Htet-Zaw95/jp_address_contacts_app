#!/usr/bin/env python3
"""
Quick test to verify the new progressive radius search pattern
Tests one address with detailed radius information
"""

import sys
import os

# Add the parent directory to sys.path to import from app.py
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import parse_address_components, estimate_coordinates_from_address, get_comprehensive_contacts

def test_progressive_search():
    """Test the new progressive radius search pattern"""
    
    test_address = "山梨県甲府市丸の内1-18-1"
    
    print("🔍 Testing New Progressive Radius Search Pattern")
    print("=" * 60)
    print(f"Test Address: {test_address}")
    print("New Search Pattern: 1km→2km→3km→4km→5km→7km→9km→11km→13km→15km→17km")
    print("-" * 60)
    
    # Parse address components
    prefecture, city, district = parse_address_components(test_address)
    print(f"Parsed - Prefecture: {prefecture}, City: {city}, District: {district}")
    
    # Estimate coordinates
    coords = estimate_coordinates_from_address(test_address)
    if coords:
        print(f"Coordinates: {coords[0]:.4f}, {coords[1]:.4f}")
    else:
        print("Coordinates: Not found")
        return
    
    # Get contacts with the new progressive search
    contacts = get_comprehensive_contacts(city, district, prefecture, coords)
    
    # Count total contacts
    total_contacts = sum(len(contact_list) for contact_list in contacts.values())
    print(f"Total contacts found: {total_contacts}")
    print("-" * 60)
    
    # Show contacts with distances
    for contact_type, contact_list in contacts.items():
        if contact_list:
            print(f"\n{contact_type}:")
            for i, contact in enumerate(contact_list, 1):
                distance_info = f" ({contact['distance_km']}km)" if contact.get('distance_km') else " (距離不明)"
                print(f"  {i}. {contact['name']}{distance_info}")
                print(f"     📞 {contact['phone']}")
                print(f"     📍 {contact['address']}")
    
    print("\n" + "=" * 60)
    print("✅ Progressive search test completed!")
    print("Note: The system now searches in finer increments (11 steps vs 8 steps)")
    print("This provides more precise distance-based results!")

if __name__ == "__main__":
    test_progressive_search()
