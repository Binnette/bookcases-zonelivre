import geojson
import json
import os
import subprocess
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
import shutil

# Constants
folder = 'bookcases'
url = 'https://boite.a.livres.zonelivre.fr/wp-json/geodir/v2/markers/?post_type=gd_place'

# Set up Selenium WebDriver options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument(f'user-agent={UserAgent().chrome}')

def find_chromedriver_path():
    if os.name == 'nt':  # Windows
        result = subprocess.run(['where', 'chromedriver.exe'], capture_output=True, text=True)
        if result.returncode == 0:
            paths = result.stdout.splitlines()
            if paths:
                return paths[0]
        raise FileNotFoundError("chromedriver.exe not found in PATH")
    else:  # Linux or macOS
        return '/usr/bin/chromedriver'

chromedriver_path = find_chromedriver_path()
service = ChromeService(executable_path=chromedriver_path)

# Set up WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Delete the folder if it exists
if os.path.exists(folder):
    shutil.rmtree(folder)

# Create the folder
os.makedirs(folder, exist_ok=True)

# Get the webpage content
driver.get(url)

data = driver.find_element("tag name", "body").text

# Extract data
data = json.loads(data)
# Close driver
driver.quit()

total_bookcases = data['total']

# Exit with a non-zero status code if no bookcases were found
if total_bookcases == 0:
    print("No bookcases found. Exiting with an error.")
    exit(1)

# Parse data
features = []
coords = set()
duplicates = 0
items = data['items']

for item in sorted(items, key=lambda x: int(x['m']), reverse=True):
    coord = (float(item['ln']), float(item['lt']))

    if coord in coords:
        duplicates += 1
        continue
    
    coords.add(coord)
    features.append(geojson.Feature(
        geometry=geojson.Point(coord),
        properties={
            "id": item['m'],
            "name": item['t']
            #"icon": item['i'],
        }
    ))

# Create GeoJSON FeatureCollection
geojson_data = geojson.FeatureCollection(features)

# Save the GeoJSON to a file
output_file_path = os.path.join(folder, "bookcases.geojson")
with open(output_file_path, 'w', encoding='utf-8') as file:
    geojson.dump(geojson_data, file, ensure_ascii=False, indent=2)

# Log the results
print(f"GeoJSON created: {output_file_path}")
print(f"Total bookcases: {total_bookcases}")
print(f"Unique bookcases: {len(geojson_data['features'])}")
print(f"Duplicate bookcases: {duplicates}")