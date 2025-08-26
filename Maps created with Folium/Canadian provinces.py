#Displays Canadian provinces colored according to their populations
#By:   Silvana Paredes
#Date: 16/08/2025

import geopandas as gpd
import folium
import requests
from io import StringIO

# Download the GeoJSON file from Opendatasoft (includes provinces and territories)
url = "https://data.opendatasoft.com/explore/dataset/georef-canada-province%40public/download/?format=geojson&timezone=America/Toronto"
response = requests.get(url)
geojson_data = response.text

# Read the GeoJSON into a GeoDataFrame
gdf = gpd.read_file(StringIO(geojson_data))

# Dictionary with the population of provincial and territorial capitals
capital_population = {
    "Ontario": 2930000,
    "Quebec": 540000,
    "British Columbia": 85000,
    "Alberta": 1000000,
    "Manitoba": 750000,
    "Saskatchewan": 230000,
    "Nova Scotia": 430000,
    "New Brunswick": 60000,
    "Newfoundland and Labrador": 110000,
    "Prince Edward Island": 36000,
    "Yukon": 40000,  # Whitehorse
    "Northwest Territories": 20000,  # Yellowknife
    "Nunavut": 18000  # Iqaluit
}

# Add a 'population' column to the GeoDataFrame
gdf['population'] = gdf['prov_name_en'].map(capital_population)


# Create a map centered on Canada
m = folium.Map(
    location=[63.0, -100.0],  # Center coordinates
    zoom_start=3,             # Initial zoom
    min_zoom=3,               # Prevent zooming out beyond this
    max_bounds=True           # Prevents panning beyond map edges
)

m.fit_bounds([[41, -141], [83, -52]])  # southwest, northeast bounds of Canada

# Add a choropleth layer coloring provinces and territories based on capital population
folium.Choropleth(
    geo_data=gdf,
    name="choropleth",
    data=gdf,
    columns=["prov_name_en", "population"],
    key_on="feature.properties.prov_name_en",
    fill_color="Spectral",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Population of Provincial and Territorial Capitals"
).add_to(m)

# Save the map to an HTML file
m.save("canada_provinces_territories.html")
