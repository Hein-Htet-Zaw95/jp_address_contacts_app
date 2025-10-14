# JP Address → Related Contacts (Streamlit)

A small Streamlit app that takes a Japanese address and returns a table of nearby public agencies and utilities:
- City/Town hall
- Police station
- Fire station
- Hospital
- Health center (best-effort)
- Water/Sewer bureau (best-effort)
- Electricity & Gas company (by prefecture heuristic mapping)
- NTT hotline

## How it works
- Geocoding via GSI AddressSearch API
- POI search via OpenStreetMap Overpass API (no API key required)
- Utilities mapping by prefecture (extend in `app.py`)

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Notes
- Internet access is required at runtime.
- Phone numbers for utilities are generic region hotlines; verify for your service area.
- You can extend the prefecture mapping in `PREF_UTILITY` and/or add more Overpass queries.