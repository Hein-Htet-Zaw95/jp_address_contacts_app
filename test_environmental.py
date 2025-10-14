#!/usr/bin/env python3
"""
Test script to verify environmental department contacts are included in 市区町村役所
"""

import sys
import os

# Add the parent directory to sys.path to import from app.py
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import parse_address_components, estimate_coordinates_from_address, get_comprehensive_contacts

def test_environmental_departments():
    """Test that environmental departments are included in city hall contacts"""
    
    test_addresses = [
        ("東京都新宿区西新宿2-8-1", "新宿区"),
        ("東京都渋谷区神宮前1-1-1", "渋谷区"),
        ("東京都練馬区石神井町8-10-16", "練馬区"),
        ("東京都足立区竹の塚1-1-1", "足立区"),
        ("神奈川県横浜市鶴見区鶴見中央4-1-1", "横浜市鶴見区"),
        ("神奈川県川崎市川崎区駅前本町1-1", "川崎市"),
        ("千葉県千葉市中央区中央1-1-1", "千葉市"),
        ("埼玉県さいたま市大宮区大門町1-1", "さいたま市"),
        ("山口県山口市滝町1-1", "山口市"),
        ("広島県広島市中区基町10-52", "広島市中区"),
        ("茨城県つくば市研究学園1-1-1", "つくば市"),
        ("山梨県甲府市丸の内1-18-1", "甲府市"),
    ]
    
    print("🌱 Environmental Department Contact Test")
    print("=" * 70)
    print("Verifying 環境クリーン部・環境対策課 contacts are included in 市区町村役所")
    print("=" * 70)
    
    success_count = 0
    total_tests = len(test_addresses)
    
    for i, (address, area_name) in enumerate(test_addresses, 1):
        print(f"\n{i}. Testing: {area_name}")
        print(f"   Address: {address}")
        print("-" * 50)
        
        try:
            # Parse and get contacts
            prefecture, city, district = parse_address_components(address)
            coords = estimate_coordinates_from_address(address)
            contacts = get_comprehensive_contacts(city, district, prefecture, coords)
            
            # Check city hall contacts
            city_halls = contacts.get('市区町村役所', [])
            
            if not city_halls:
                print("   ❌ No city hall contacts found")
                continue
            
            print(f"   市区町村役所 contacts found: {len(city_halls)}")
            
            # Check each contact
            has_main_office = False
            has_env_dept = False
            
            for j, office in enumerate(city_halls, 1):
                services = ', '.join(office.get('services', []))
                print(f"   {j}. {office['name']}")
                print(f"      📞 {office['phone']}")
                print(f"      🏢 Services: {services}")
                
                # Check if this is main office or environmental department
                if any(keyword in office['name'] for keyword in ['役所', '区役所', '市役所']):
                    has_main_office = True
                if any(keyword in office['name'] for keyword in ['環境', 'クリーン']):
                    has_env_dept = True
            
            # Evaluate success
            if has_main_office and has_env_dept:
                print("   ✅ SUCCESS: Both main office and environmental department found")
                success_count += 1
            elif has_main_office:
                print("   ⚠️  PARTIAL: Main office found, but environmental department missing")
            else:
                print("   ❌ FAILED: Main office not found")
                
        except Exception as e:
            print(f"   ❌ ERROR: {str(e)}")
    
    print("\n" + "=" * 70)
    print("📊 ENVIRONMENTAL DEPARTMENT TEST SUMMARY")
    print("=" * 70)
    print(f"Total areas tested: {total_tests}")
    print(f"Areas with environmental departments: {success_count}")
    print(f"Coverage rate: {(success_count/total_tests)*100:.1f}%")
    
    if success_count >= total_tests * 0.8:
        print("✅ EXCELLENT: Most areas have environmental department contacts")
    elif success_count >= total_tests * 0.5:
        print("✅ GOOD: Many areas have environmental department contacts")
    else:
        print("⚠️  NEEDS WORK: More environmental departments need to be added")
    
    print("\n🌱 Environmental services now available:")
    print("• ごみ収集 (Waste collection)")
    print("• リサイクル (Recycling)")
    print("• 環境対策 (Environmental measures)")

if __name__ == "__main__":
    test_environmental_departments()
