#!/usr/bin/env python3
"""
Test script to verify the nearest police station search for 石神井町
Tests the specific address mentioned by the user
"""

import sys
import os

# Add the parent directory to sys.path to import from app.py
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import parse_address_components, estimate_coordinates_from_address, get_comprehensive_contacts

def test_shakujii_address():
    """Test the specific address for nearest police station"""
    
    test_address = "東京都練馬区石神井町8‐10‐16"
    
    print("🚔 Testing Nearest Police Station Search")
    print("=" * 60)
    print(f"Test Address: {test_address}")
    print("Expected: 石神井警察署 should be closest (750m, 2min drive)")
    print("Previous Issue: 練馬警察署 was showing as closest (6km, 18min drive)")
    print("-" * 60)
    
    # Parse address components
    prefecture, city, district = parse_address_components(test_address)
    print(f"Parsed - Prefecture: {prefecture}, City: {city}, District: {district}")
    
    # Estimate coordinates
    coords = estimate_coordinates_from_address(test_address)
    if coords:
        print(f"Address Coordinates: {coords[0]:.4f}, {coords[1]:.4f}")
    else:
        print("Address Coordinates: Not found")
        return
    
    # Get contacts with progressive search
    contacts = get_comprehensive_contacts(city, district, prefecture, coords)
    
    # Focus on police stations
    police_stations = contacts.get('警察署', [])
    print(f"\nFound {len(police_stations)} police station(s):")
    print("-" * 40)
    
    for i, station in enumerate(police_stations, 1):
        distance_info = f" ({station['distance_km']}km)" if station.get('distance_km') else " (距離不明)"
        print(f"{i}. {station['name']}{distance_info}")
        print(f"   📞 {station['phone']}")
        print(f"   📍 {station['address']}")
        
        # Check if this is the expected closest station
        if station['name'] == "石神井警察署":
            if i == 1:
                print("   ✅ CORRECT: 石神井警察署 is listed first (closest)")
            else:
                print("   ❌ ISSUE: 石神井警察署 should be listed first")
        print()
    
    # Also show all contact types for completeness
    total_contacts = sum(len(contact_list) for contact_list in contacts.values())
    print(f"Total contacts found: {total_contacts}")
    
    print("\n" + "=" * 60)
    print("✅ Address test completed!")

if __name__ == "__main__":
    test_shakujii_address()
