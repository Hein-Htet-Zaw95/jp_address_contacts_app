#!/usr/bin/env python3
# Complete pipeline test for the problematic address

import sys
import os
sys.path.append(os.path.dirname(__file__))

from app import parse_address_components, get_comprehensive_contacts, geocode_gsi, assemble_results

def test_complete_pipeline(address):
    print(f"Testing complete pipeline for: {address}")
    print("=" * 50)
    
    # Step 1: Geocoding
    print("Step 1: Geocoding...")
    coords = geocode_gsi(address.strip())
    if not coords:
        print("❌ Geocoding failed!")
        return
    lat, lon = coords
    print(f"✅ Geocoding successful: {lat:.6f}, {lon:.6f}")
    
    # Step 2: Address parsing
    print("\nStep 2: Address parsing...")
    pref, city_name, district_name = parse_address_components(address)
    print(f"✅ Parsed: Prefecture='{pref}', City='{city_name}', District='{district_name}'")
    
    # Step 3: Contact lookup
    print("\nStep 3: Contact lookup...")
    comprehensive_contacts = get_comprehensive_contacts(city_name, district_name, pref)
    total_contacts = sum(len(contacts) for contacts in comprehensive_contacts.values())
    print(f"✅ Found {total_contacts} total contacts")
    
    # Step 4: Assemble results
    print("\nStep 4: Assembling results...")
    df_contacts = assemble_results(comprehensive_contacts)
    print(f"✅ DataFrame created with {len(df_contacts)} rows")
    
    if df_contacts.empty:
        print("❌ DataFrame is empty!")
        return
    
    # Step 5: Display results
    print("\nStep 5: Results summary...")
    required_order = ['労基署', '警察署', '市区町村役所', '消防署', 'ガス', '電力', '病院', '保健所', '水道', 'NTT', '下水道']
    
    for category in required_order:
        category_df = df_contacts[df_contacts['種別'] == category]
        if not category_df.empty:
            print(f"📋 {category}: {len(category_df)} contacts")
            for idx, row in category_df.iterrows():
                print(f"  - {row['施設名']}: {row['電話番号']}")
    
    print(f"\n✅ Pipeline test completed successfully!")
    return True

# Test the problematic address
test_address = "東京都中央区築地3-1005-15"
success = test_complete_pipeline(test_address)

if success:
    print("\n🎉 All tests passed! The issue might be with the Streamlit interface.")
else:
    print("\n❌ Pipeline test failed.")
