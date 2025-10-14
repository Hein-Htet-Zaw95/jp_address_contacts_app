#!/usr/bin/env python3
# Test geocoding for the problematic address

import requests
import sys
import os

def geocode_gsi(address: str):
    """Geocode address using GSI API"""
    GSI_GEOCODE = "https://msearch.gsi.go.jp/address-search/AddressSearch"
    try:
        params = {"q": address}
        response = requests.get(GSI_GEOCODE, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        print(f"API Response: {data}")
        
        if data and len(data) > 0:
            first_result = data[0]
            geometry = first_result.get("geometry")
            if geometry and "coordinates" in geometry:
                lon, lat = geometry["coordinates"]
                return lat, lon
        return None
    except Exception as e:
        print(f"Geocoding error: {e}")
        return None

# Test the problematic address
test_address = "東京都中央区築地3-1005-15"
print(f"Testing geocoding for: {test_address}")

coords = geocode_gsi(test_address)
print(f"Result: {coords}")

if coords:
    lat, lon = coords
    print(f"Latitude: {lat}, Longitude: {lon}")
else:
    print("Geocoding failed!")
