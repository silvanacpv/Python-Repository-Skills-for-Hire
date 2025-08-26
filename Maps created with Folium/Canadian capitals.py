#Displays the capital of the Canadian provinces and their populations
#By:   Silvana Paredes
#Date: 16/08/2025

import folium

# List of Canadian provincial capitals with coordinates and approximate population
provinces = [
    {"province": "Ontario", "city": "Toronto", "lat": 43.65107, "lon": -79.347015, "population": 2930000},
    {"province": "Quebec", "city": "Quebec City", "lat": 46.8139, "lon": -71.2082, "population": 540000},
    {"province": "British Columbia", "city": "Victoria", "lat": 48.4284, "lon": -123.3656, "population": 85000},
    {"province": "Alberta", "city": "Edmonton", "lat": 53.5461, "lon": -113.4938, "population": 1000000},
    {"province": "Manitoba", "city": "Winnipeg", "lat": 49.8951, "lon": -97.1384, "population": 750000},
    {"province": "Saskatchewan", "city": "Regina", "lat": 50.4452, "lon": -104.6189, "population": 230000},
    {"province": "Nova Scotia", "city": "Halifax", "lat": 44.6488, "lon": -63.5752, "population": 430000},
    {"province": "New Brunswick", "city": "Fredericton", "lat": 45.9636, "lon": -66.6431, "population": 60000},
    {"province": "Newfoundland and Labrador", "city": "St. John's", "lat": 47.5615, "lon": -52.7126, "population": 110000},
    {"province": "Prince Edward Island", "city": "Charlottetown", "lat": 46.2382, "lon": -63.1311, "population": 36000}
]

# Create a map centered on Canada
canada_map = folium.Map(location=[56.1304, -106.3468], zoom_start=4)

# Add colored circles proportional to population
for p in provinces:
    # Determine color based on population
    if p["population"] > 1000000:
        color = 'red'
    elif p["population"] > 500000:
        color = 'orange'
    else:
        color = 'green'
    
    folium.Circle(
        location=[p["lat"], p["lon"]],
        radius=p["population"] * 0.1,  # Scale the radius for visibility
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.6,
        popup=f"{p['city']}, {p['province']}<br>Population: {p['population']}"
    ).add_to(canada_map)

# Save the map
canada_map.save("canada_capitals.html")
