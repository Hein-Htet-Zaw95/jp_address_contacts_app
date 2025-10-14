#!/usr/bin/env python3
"""
Debug script to check coordinate estimation for police station addresses
"""

import sys
import os

# Add the parent directory to sys.path to import from app.py
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import estimate_coordinates_from_address

def debug_coordinates():
    """Debug coordinate estimation for police stations"""
    
    addresses_to_test = [
        "東京都練馬区石神井町2-15-13",  # 石神井警察署
        "東京都練馬区光が丘2-9-7",      # 光が丘警察署  
        "東京都練馬区豊玉北5-3-15",     # 練馬警察署
        "東京都練馬区石神井町8‐10‐16",  # User's address
    ]
    
    print("🔍 Debug: Coordinate Estimation for Police Stations")
    print("=" * 60)
    
    for address in addresses_to_test:
        coords = estimate_coordinates_from_address(address)
        if coords:
            print(f"✅ {address}")
            print(f"   Coordinates: {coords[0]:.4f}, {coords[1]:.4f}")
        else:
            print(f"❌ {address}")
            print(f"   Coordinates: NOT FOUND")
        print()
    
    print("=" * 60)
    print("Debug completed!")

if __name__ == "__main__":
    debug_coordinates()
