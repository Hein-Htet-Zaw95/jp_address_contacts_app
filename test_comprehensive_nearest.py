#!/usr/bin/env python3
"""
Comprehensive test script to verify nearest place search across all supported regions
Tests the progressive radius search functionality for various address types
"""

import sys
import os

# Add the parent directory to sys.path to import from app.py
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import parse_address_components, estimate_coordinates_from_address, get_comprehensive_contacts

def test_comprehensive_nearest_search():
    """Test nearest place search across all supported regions"""
    
    test_addresses = [
        # Tokyo - Different areas
        ("東京都新宿区西新宿2-8-1", "Tokyo Metropolitan Government"),
        ("東京都渋谷区神宮前1-1-1", "Shibuya area"),
        ("東京都練馬区石神井町8-10-16", "Nerima - Shakujii area"),
        ("東京都足立区竹の塚1-1-1", "Adachi - Takenotsuka"),
        
        # Kanagawa
        ("神奈川県横浜市港北区新横浜2-5-1", "Yokohama - Shin-Yokohama"),
        ("神奈川県川崎市川崎区駅前本町1-1", "Kawasaki Station area"),
        
        # Chiba
        ("千葉県千葉市中央区中央1-1-1", "Chiba City Center"),
        ("千葉県市川市八幡1-1-1", "Ichikawa"),
        
        # Saitama
        ("埼玉県さいたま市大宮区大門町1-1", "Omiya"),
        ("埼玉県川口市本町1-1-1", "Kawaguchi"),
        
        # Yamaguchi Prefecture
        ("山口県下関市竹崎町1-1-1", "Shimonoseki"),
        ("山口県山口市滝町1-1", "Yamaguchi City"),
        
        # Hiroshima Prefecture
        ("広島県広島市中区基町10-52", "Hiroshima City Center"),
        ("広島県呉市中央1-1-1", "Kure City"),
        
        # Ibaraki Prefecture
        ("茨城県つくば市研究学園1-1-1", "Tsukuba Science City"),
        ("茨城県水戸市笠原町978-6", "Mito City"),
        
        # Yamanashi Prefecture
        ("山梨県甲府市丸の内1-18-1", "Kofu City Hall"),
        ("山梨県富士吉田市下吉田6-1-1", "Fujiyoshida"),
    ]
    
    print("🎯 Comprehensive Nearest Place Search Test")
    print("=" * 80)
    print("Testing progressive radius search across all supported regions")
    print("Search Pattern: 1km→2km→3km→4km→5km→7km→9km→11km→13km→15km→17km")
    print("=" * 80)
    
    success_count = 0
    total_tests = len(test_addresses)
    
    for i, (address, description) in enumerate(test_addresses, 1):
        print(f"\n{i}. Testing: {description}")
        print(f"   Address: {address}")
        print("-" * 60)
        
        try:
            # Parse address
            prefecture, city, district = parse_address_components(address)
            print(f"   Parsed: {prefecture} > {city} > {district}")
            
            # Get coordinates
            coords = estimate_coordinates_from_address(address)
            if not coords:
                print("   ❌ No coordinates found for address")
                continue
            
            print(f"   Coordinates: {coords[0]:.4f}, {coords[1]:.4f}")
            
            # Get contacts
            contacts = get_comprehensive_contacts(city, district, prefecture, coords)
            
            # Analyze results
            total_contacts = sum(len(contact_list) for contact_list in contacts.values())
            print(f"   Total contacts: {total_contacts}")
            
            if total_contacts == 0:
                print("   ❌ No contacts found")
                continue
            
            # Check key services and their distances
            key_services = ['警察署', '消防署', '病院']
            nearest_found = False
            
            for service_type in key_services:
                service_contacts = contacts.get(service_type, [])
                if service_contacts:
                    closest = service_contacts[0]
                    distance = closest.get('distance_km', 'Unknown')
                    print(f"   🏢 {service_type}: {closest['name']} ({distance}km)")
                    
                    # Check if we found a reasonably close service
                    if isinstance(distance, (int, float)) and distance <= 20:
                        nearest_found = True
            
            # Test other important services
            other_services = ['市区町村役所', 'ガス', '電力']
            for service_type in other_services:
                service_contacts = contacts.get(service_type, [])
                if service_contacts:
                    closest = service_contacts[0]
                    distance = closest.get('distance_km', 'Unknown')
                    print(f"   🏛️  {service_type}: {closest['name']} ({distance}km)")
            
            if nearest_found or total_contacts >= 5:
                print("   ✅ SUCCESS: Found nearest places successfully")
                success_count += 1
            else:
                print("   ⚠️  WARNING: Limited results found")
                
        except Exception as e:
            print(f"   ❌ ERROR: {str(e)}")
    
    print("\n" + "=" * 80)
    print("📊 TEST SUMMARY")
    print("=" * 80)
    print(f"Total tests: {total_tests}")
    print(f"Successful: {success_count}")
    print(f"Success rate: {(success_count/total_tests)*100:.1f}%")
    
    if success_count == total_tests:
        print("🎉 EXCELLENT: All addresses can find nearest places!")
    elif success_count >= total_tests * 0.8:
        print("✅ GOOD: Most addresses working well")
    else:
        print("⚠️  NEEDS IMPROVEMENT: Some regions need more data")
    
    print("\n🔍 PROGRESSIVE SEARCH ANALYSIS:")
    print("The app uses 11-step radius search to ensure users always get:")
    print("• Closest emergency services (police, fire, hospital)")
    print("• Nearest administrative offices")
    print("• Most convenient utility contacts")
    print("• Cross-city referencing when local services unavailable")

if __name__ == "__main__":
    test_comprehensive_nearest_search()
