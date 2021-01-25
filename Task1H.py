from floodsystem.datafetcher import fetch_station_data
import json

with open('data.json','w') as file:
    file.write(json.dumps(fetch_station_data()))