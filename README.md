# bookcases-zonelivre

Bookcases from zonelivre: https://boite.a.livres.zonelivre.fr/

## How to

### Use the files

Open the most recent folder and download any geojson or gpx file.

Note the gpx files are Osmand favorites files, so you can import them as favorites in Osmand.
I recommand to import/show only 1 region at a time in Osmand to avoid lags.

### Update files

1. Create a folder with today date
2. Visit https://boite.a.livres.zonelivre.fr/
3. Then https://boite.a.livres.zonelivre.fr/wp-json/geodir/v2/markers/?post_type=gd_place
4. Save this file as data.json in your new folder
5. Edit pythons script to update folder name
6. Run script step1ParseDataJson.py
7. Run script step2FilterBookcasesByRegions.py
8. Run script step3ConvertGeojsonToOsmandGpx.py
9. Done

## Stats

|Date      |Bookcases|
|----------|---------|
|2024-10-01|     6768|
|2022-09-20|     5193|

## Stats by region 

|Region                 |2022-09-20|2024-10-01|
|-----------------------|----------|----------|
|Total                  |      5551|      6774|
|Duplicates             |          |         6|
|Uniques                |          |      6768|
|Out France Metro       |          |        18|
|France métro           |      5291|      6750|
|Nouvelle Aquitaine     |       871|      1101|
|Ile de France          |       671|       604|
|Auvergne Rhone-Alpes   |       646|       711|
|Occitanie              |       436|       470|
|Grand Est              |       448|       558|
|Hauts de France        |       361|       435|
|Pays de la Loire       |       361|       509|
|Bretagne               |       359|       477|
|Bourgogne Franche-Comte|       288|       439|
|Normandie              |       311|       763|
|Centre Val de Loire    |       300|       435|
|PACA                   |       240|       231|
|Corse                  |         9|        17|