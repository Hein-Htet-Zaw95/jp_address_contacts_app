#!/usr/bin/env python3
"""
Debug script with detailed output to trace the contact selection process
"""

import sys
import os

# Add the parent directory to sys.path to import from app.py
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import parse_address_components, estimate_coordinates_from_address, calculate_distance

def debug_contact_selection():
    """Debug the contact selection process step by step"""
    
    test_address = "東京都練馬区石神井町8‐10‐16"
    
    print("🔍 Debug: Contact Selection Process")
    print("=" * 60)
    print(f"Test Address: {test_address}")
    
    # Parse address
    prefecture, city, district = parse_address_components(test_address)
    print(f"Parsed - Prefecture: {prefecture}, City: {city}, District: {district}")
    
    # Get user coordinates
    user_coords = estimate_coordinates_from_address(test_address)
    if not user_coords:
        print("❌ Cannot get user coordinates")
        return
    
    user_lat, user_lon = user_coords
    print(f"User Coordinates: {user_lat:.4f}, {user_lon:.4f}")
    
    # Manually check police stations
    police_stations = [
        {"name": "石神井警察署", "address": "東京都練馬区石神井町2-15-13"},
        {"name": "練馬警察署", "address": "東京都練馬区豊玉北5-3-15"},
        {"name": "光が丘警察署", "address": "東京都練馬区光が丘2-9-7"}
    ]
    
    print("\n🚔 Police Station Distance Analysis:")
    print("-" * 40)
    
    for station in police_stations:
        station_coords = estimate_coordinates_from_address(station['address'])
        if station_coords:
            station_lat, station_lon = station_coords
            distance = calculate_distance(user_lat, user_lon, station_lat, station_lon)
            print(f"{station['name']}: {distance:.1f}km")
            print(f"  Address: {station['address']}")
            print(f"  Coordinates: {station_lat:.4f}, {station_lon:.4f}")
        else:
            print(f"{station['name']}: Distance unknown (no coordinates)")
            print(f"  Address: {station['address']}")
        print()
    
    print("=" * 60)
    print("Debug completed!")

if __name__ == "__main__":
    debug_contact_selection()
