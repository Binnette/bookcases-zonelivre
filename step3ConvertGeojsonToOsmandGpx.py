import json
import os

# Parameters
folder = './2022-09-20/'
file = 'data.json'

# Constants
regions = 'Régions Françaises/'
livres = 'ZoneLivre'
horsFrance = 'ZoneLivre hors France métro'

# Globals
t = ''

def save_file(file, content):
    try:
        with open(file, 'w+') as f:
            f.write(content)
        print('OK ' + file)
    except Exception as err:
        print('KO ' + file + ' ' + str(err))

def w(line):
    global t
    t += line + '\n'

# Write GPX headers
def w_header():
    w("<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>")
    w('<gpx version="1.1" creator="Binnette" xmlns="http://www.topografix.com/GPX/1/1" xmlns:osmand="https://osmand.net" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd">')

# Write GPX footer
def w_footer(title):
    w("  <extensions>")
    w("    <osmand:points_groups>")
    w(f'      <group name="{title}" color="#ff5020" icon="public_bookcase" background="square" />')
    w("    </osmand:points_groups>")
    w("  </extensions>")
    w("</gpx>")

def clean(text):
    text = text or ''
    text = text.replace('&', ' et ')
    text = ' '.join(text.split())
    return text.strip()

def get_addr(p):
    tab = []
    street = p.get("addr:street")
    zip_code = p.get("addr:zipcode")
    city = p.get("addr:city")
    country = p.get("addr:country")
    if street:
        tab.append(street)
    if zip_code or city:
        tab.append(f'{zip_code} {city}')
    if country:
        tab.append(country)
    addr = ', '.join(tab)
    return clean(addr)

def w_bookcase(b, i, title):
    try:
        p = b['properties']
        name = clean(f"{p['name']} z{p['id']}")
        lat = b['geometry']['coordinates'][1]
        lon = b['geometry']['coordinates'][0]
        w(f'  <wpt lat="{lat}" lon="{lon}">')
        w(f"    <name>{name}</name>")
        w(f"    <type>{title}</type>")
        w("    <extensions>")
        w("      <osmand:icon>public_bookcase</osmand:icon>")
        w("      <osmand:background>square</osmand:background>")
        w("      <osmand:color>#10c0f0</osmand:color>")
        w("    </extensions>")
        w("  </wpt>")
    except Exception as err:
        print(err)

def convert(geo, title):
    global t
    count = len(geo['features'])
    print(f'Converting {count} features...')

    # reset content
    t = ''
    w_header()

    for i, boite in enumerate(geo['features']):
        w_bookcase(boite, i, title)

    w_footer(title)

    return t

def read_file(file):
    try:
        with open(file, 'r') as f:
            return json.load(f)
    except Exception as err:
        print(err)

main_files = [f for f in os.listdir(folder) if f.endswith('.geojson')]
region_files = [f for f in os.listdir(os.path.join(folder, regions)) if f.endswith('.geojson')]

for file in main_files:
    name = os.path.splitext(file)[0]
    title = livres if name.startswith('bookcase') else horsFrance
    data = read_file(os.path.join(folder, file))
    converted = convert(data, title)
    gpx_path = os.path.join(folder, f'{name}.gpx')
    save_file(gpx_path, converted)

for file in region_files:
    name = os.path.splitext(file)[0]
    title = f"{livres} {name}"
    data = read_file(os.path.join(folder, regions, file))
    converted = convert(data, title)
    gpx_path = os.path.join(folder, regions, f'{name}.gpx')
    save_file(gpx_path, converted)

print("Done.")
