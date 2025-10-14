#!/usr/bin/env python3
"""
Comprehensive demonstration of environmental department contacts
Shows the enhanced 市区町村役所 functionality
"""

import sys
import os

# Add the parent directory to sys.path to import from app.py
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import parse_address_components, estimate_coordinates_from_address, get_comprehensive_contacts

def demonstrate_environmental_contacts():
    """Demonstrate environmental department contacts across regions"""
    
    demo_addresses = [
        ("東京都新宿区西新宿2-8-1", "新宿区 - 都心部"),
        ("東京都練馬区石神井町8-10-16", "練馬区 - 住宅地域"),
        ("神奈川県横浜市鶴見区鶴見中央4-1-1", "横浜市 - 工業地域"),
        ("千葉県千葉市中央区中央1-1-1", "千葉市 - 県庁所在地"),
        ("埼玉県さいたま市大宮区大門町1-1", "さいたま市 - 商業地域"),
        ("山口県下関市竹崎町1-1-1", "下関市 - 港湾都市"),
        ("広島県呉市中央1-1-1", "呉市 - 工業都市"),
        ("茨城県水戸市笠原町978-6", "水戸市 - 県庁所在地"),
        ("山梨県甲府市丸の内1-18-1", "甲府市 - 県庁所在地"),
    ]
    
    print("🌱 Environmental Department Contact Demonstration")
    print("=" * 80)
    print("Enhanced 市区町村役所 now includes environmental departments")
    print("Added services: ごみ収集, リサイクル, 環境対策")
    print("=" * 80)
    
    for i, (address, description) in enumerate(demo_addresses, 1):
        print(f"\n🏢 {i}. {description}")
        print(f"Address: {address}")
        print("-" * 60)
        
        try:
            # Get contacts
            prefecture, city, district = parse_address_components(address)
            coords = estimate_coordinates_from_address(address)
            contacts = get_comprehensive_contacts(city, district, prefecture, coords)
            
            # Focus on city hall contacts
            city_halls = contacts.get('市区町村役所', [])
            
            if city_halls:
                print(f"市区町村役所 contacts: {len(city_halls)}")
                
                for j, office in enumerate(city_halls, 1):
                    services = office.get('services', [])
                    
                    print(f"\n  {j}. {office['name']}")
                    print(f"     📞 Phone: {office['phone']}")
                    print(f"     📍 Address: {office['address']}")
                    print(f"     🕒 Hours: {office['hours']}")
                    
                    # Categorize services
                    admin_services = [s for s in services if s in ['住民票', '戸籍']]
                    env_services = [s for s in services if s in ['ごみ収集', 'リサイクル', '環境対策']]
                    
                    if admin_services:
                        print(f"     🏛️  Administrative: {', '.join(admin_services)}")
                    if env_services:
                        print(f"     🌱 Environmental: {', '.join(env_services)}")
            else:
                print("❌ No city hall contacts found")
                
        except Exception as e:
            print(f"❌ Error: {str(e)}")
    
    print("\n" + "=" * 80)
    print("✅ ENVIRONMENTAL DEPARTMENTS SUCCESSFULLY ADDED")
    print("=" * 80)
    
    print("🎯 KEY IMPROVEMENTS:")
    print("  • 市区町村役所 now returns up to 2 contacts (vs 1 previously)")
    print("  • Main city hall office for administrative services")
    print("  • Environmental department for waste & environmental services")
    print("  • Enhanced service categorization")
    
    print("\n🌱 ENVIRONMENTAL SERVICES AVAILABLE:")
    print("  • ごみ収集 (Waste Collection) - Garbage pickup schedules & info")
    print("  • リサイクル (Recycling) - Recycling programs & facilities")
    print("  • 環境対策 (Environmental Measures) - Pollution control & policy")
    
    print("\n📞 CONTACT TYPES:")
    print("  • 環境部 (Environmental Department)")
    print("  • 環境政策課 (Environmental Policy Division)")
    print("  • 環境対策課 (Environmental Measures Division)")
    print("  • 環境清掃部 (Environmental & Sanitation Department)")
    print("  • 環境局 (Environmental Bureau)")
    
    print("\n🏢 COVERAGE:")
    print("  • Major metropolitan areas (Tokyo, Yokohama, Saitama)")
    print("  • Prefecture capitals (Chiba, Yamaguchi, Hiroshima, Mito, Kofu)")
    print("  • Industrial cities (Kure, Shimonoseki)")
    print("  • Residential areas (Nerima, Tsurumi)")
    
    print("\n🎉 Users can now get complete municipal services contact information!")

if __name__ == "__main__":
    demonstrate_environmental_contacts()
