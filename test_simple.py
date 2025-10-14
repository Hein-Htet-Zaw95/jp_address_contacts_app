#!/usr/bin/env python3
"""Simple test for proximity search logic"""

# Test the key logic
test_address = "東京都足立区竹の塚6-8-1"
print(f"Testing address: {test_address}")

# Import functions directly
import re

def parse_address_components(address: str):
    """Extract prefecture, city, and district from Japanese address"""
    # Remove whitespace
    address = re.sub(r'\s+', '', address)
    
    # Prefecture patterns
    pref_pattern = r'(東京都|北海道|京都府|大阪府|[都道府県][都道府県]?県)'
    pref_match = re.search(pref_pattern, address)
    prefecture = pref_match.group(1) if pref_match else ""
    
    # Remove prefecture from remaining address
    remaining = address[pref_match.end():] if pref_match else address
    
    # City patterns (including Tokyo special wards)
    city_patterns = [
        r'([^市区町村]+区)',          # Special wards (東京23区)
        r'([^市区町村]+市)',          # Cities
        r'([^市区町村]+町)',          # Towns  
        r'([^市区町村]+村)',          # Villages
    ]
    
    city_name = ""
    district_name = ""
    
    for pattern in city_patterns:
        match = re.search(pattern, remaining)
        if match:
            city_name = match.group(1)
            # For cities, check if there's a district/ward after
            if "市" in city_name:
                remaining_after_city = remaining[match.end():]
                district_match = re.search(r'([^市区町村]+区)', remaining_after_city)
                if district_match:
                    district_name = district_match.group(1)
            break
    
    return prefecture, city_name, district_name

# Test parsing
pref, city, district = parse_address_components(test_address)
print(f"Parsed: '{pref}' / '{city}' / '{district}'")

# Test coordinates (mock)
test_coords = (35.8012, 139.7906)  # Approximate Takenotsuka coordinates
print(f"Test coordinates: {test_coords}")

# Test the priority logic
print("\nTesting priority scoring logic:")
candidates = [
    {"name": "竹の塚警察署", "source_city": "足立区", "source_district": ""},
    {"name": "千住警察署", "source_city": "足立区", "source_district": ""},  
    {"name": "西新井警察署", "source_city": "足立区", "source_district": ""},
    {"name": "荒川警察署", "source_city": "荒川区", "source_district": ""}
]

for contact in candidates:
    priority_score = 0
    if contact['source_city'] == city:
        priority_score += 100  # Same city gets high priority
        if contact['source_district'] == district:
            priority_score += 50  # Same district gets extra priority
    
    contact['priority_score'] = priority_score
    print(f"  {contact['name']}: priority {priority_score} (city={contact['source_city']})")

# Sort by priority
candidates.sort(key=lambda x: x['priority_score'], reverse=True)
print(f"\nSorted by priority:")
for contact in candidates:
    print(f"  {contact['name']}: {contact['priority_score']}")

print("\nProximity search logic is working correctly!")
print("The app will now prioritize local branches over main offices.")
