#!/usr/bin/env python3
"""
Test script for Yamanashi Prefecture cities in the Japanese address contact lookup app
Tests all 13 cities added to the database
"""

import sys
import os

# Add the parent directory to sys.path to import from app.py
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import parse_address_components, estimate_coordinates_from_address, get_comprehensive_contacts

def test_yamanashi_cities():
    """Test all Yamanashi Prefecture cities"""
    
    test_addresses = [
        # Prefectural capital
        "山梨県甲府市丸の内1-18-1",
        
        # Major cities
        "山梨県富士吉田市下吉田6-1-1", 
        "山梨県都留市上谷1-1-1",
        "山梨県山梨市小原西843",
        "山梨県大月市大月2-6-20",
        "山梨県韮崎市水神1-3-4",
        "山梨県南アルプス市小笠原376",
        "山梨県北杜市須玉町大豆生田961-1",
        "山梨県甲斐市篠原2610",
        "山梨県笛吹市石和町市部777",
        "山梨県上野原市上野原3832",
        "山梨県甲州市塩山上於曽1085-1",
        "山梨県中央市臼井阿原301-1"
    ]
    
    print("🏔️ Testing Yamanashi Prefecture Cities 🏔️")
    print("=" * 60)
    
    for i, address in enumerate(test_addresses, 1):
        print(f"\n{i}. Testing address: {address}")
        print("-" * 40)
        
        # Parse address components
        try:
            prefecture, city, district = parse_address_components(address)
            print(f"   Parsed - Prefecture: {prefecture}, City: {city}, District: {district}")
            
            # Estimate coordinates
            coords = estimate_coordinates_from_address(address)
            if coords:
                print(f"   Coordinates: {coords[0]:.4f}, {coords[1]:.4f}")
            else:
                print("   Coordinates: Not found")
            
            # Get contacts
            contacts = get_comprehensive_contacts(city, district, prefecture, coords)
            
            # Count total contacts
            total_contacts = sum(len(contact_list) for contact_list in contacts.values())
            print(f"   Total contacts found: {total_contacts}")
            
            # Show sample contacts from each category
            for contact_type, contact_list in contacts.items():
                if contact_list:
                    contact = contact_list[0]  # Show first contact
                    distance = f" ({contact['distance_km']}km)" if contact.get('distance_km') else ""
                    print(f"   {contact_type}: {contact['name']}{distance}")
            
        except Exception as e:
            print(f"   ❌ Error processing address: {e}")
    
    print("\n" + "=" * 60)
    print("✅ Yamanashi Prefecture test completed!")

if __name__ == "__main__":
    test_yamanashi_cities()
