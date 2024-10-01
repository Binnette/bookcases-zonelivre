import json
import os

# Parameters
folder = './2024-10-01/'
file = 'data.json'

def save_file(file, content):
    try:
        with open(file, 'w+') as f:
            f.write(content)
        print('OK ' + file)
    except Exception as err:
        print('KO ' + file + ' ' + str(err))

def convert(data):
    count = len(data)
    print('Converting...')

    # Create default geojson object structure
    geo = {
        "type": "FeatureCollection",
        "features": []
    }

    # Loop through all the bookcase
    for b in data:
        lat = float(b['lt'])
        lon = float(b['ln'])

        # Create the geojson feature
        f = {
            "type": "Feature",
            "properties": {
                "id": b['m'],
                "name": b['t'],
                "icon": b['i'],
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    lon, lat
                ]
            }
        }
        # Adding the feature in the geojson object
        geo['features'].append(f)

    print("Converted " + str(len(geo['features'])))

    # Convert the geojson object to string
    return json.dumps(geo, indent=4)

# Read data
with open(os.path.join(folder, file), 'r') as f:
    data = json.load(f)

print("json file indicates it contains " + str(data['total']) + " bookcases")

print("Sort data...")
# sort books by id desc
books = sorted(data['items'], key=lambda x: int(x['m']), reverse=True)

# remove duplicates
coords = set()
duplicates = []
uniques = []

for cur in books:
    cur_coords = f"{cur['lt']},{cur['ln']}"
    if cur_coords in coords:
        # This is a duplicate!
        duplicates.append(cur)
    else:
        # Not a duplicate
        uniques.append(cur)
        coords.add(cur_coords)

print("# Total: " + str(len(books)))
print("# Uniques: " + str(len(uniques)))
uniques_geojson = convert(uniques)
save_file(os.path.join(folder, "bookcases.geojson"), uniques_geojson)

print("# Duplicates: " + str(len(duplicates)))
duplicates_geojson = convert(duplicates)
save_file(os.path.join(folder, "duplicates.geojson"), duplicates_geojson)

print("Done.")
