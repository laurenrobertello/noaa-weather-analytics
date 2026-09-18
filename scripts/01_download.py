import urllib.request

STATIONS = [
    "USC00309383",  # Whiteface Mountain
    "USC00306659",  # Plattsburgh AFB
    "USC00307472",  # Saranac Lake
    "USC00308631",  # Tupper Lake Sunmount
    "USC00304555",  # Lake Placid 2 S
    "USC00305711",  # Newcomb 3 W
]

BASE = "https://www.ncei.noaa.gov/pub/data/ghcn/daily/all"

for station in STATIONS:
    print(f"Downloading {station}...")
    urllib.request.urlretrieve(f"{BASE}/{station}.dly", f"{station}.dly")

print(f"Done. {len(STATIONS)} files.")
