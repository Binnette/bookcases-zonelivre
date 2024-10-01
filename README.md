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
|Total                  |      5195|      6774|
|Duplicates             |         2|         6|
|Uniques                |      5193|      6768|
|Out France Metro       |         3|        18|
|France métro           |      5190|      6750|
|Nouvelle Aquitaine     |       790|      1101|
|Normandie              |       610|       763|
|Auvergne Rhone-Alpes   |       535|       711|
|Ile de France          |       477|       604|
|Grand Est              |       412|       558|
|Pays de la Loire       |       345|       509|
|Bretagne               |       403|       477|
|Occitanie              |       355|       470|
|Bourgogne Franche-Comte|       360|       439|
|Hauts de France        |       382|       435|
|Centre Val de Loire    |       329|       435|
|PACA                   |       175|       231|
|Corse                  |        17|        17|