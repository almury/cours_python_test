#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import json
import sys

# Fonction permettant d'envoyer une requête, de récupérer des données
# au format json et de le convertir en un dictionnaire Python
def dictionary_from_json_url(url):
    f = urllib.request.urlopen(url)
    return json.loads(f.read().decode('utf-8'))


def meteo_details(localite):
    temp_moy = 0
    # Requête html permettant de récupérer les données meteo d'une localité
    url = "http://www.prevision-meteo.ch/services/json/{}".format(localite)
    dico_meteo = dictionary_from_json_url(url)
    #print(dico_meteo)
    print(f'Altitude pour {localite}: {dico_meteo["city_info"]["elevation"]}')
    #for loc in dico_meteo["city_info"]:
    print(f'température de {localite} entre 12h et 20h:')
    for i in range(12,20+1):
        print(f'température à {str(i) + "H00"}:  {dico_meteo["fcst_day_0"]["hourly_data"][str(i) + "H00"]["TMP2m"]}')
        #temp_moy = temp_moy + 

if len(sys.argv) == 2:
    ville = sys.argv[1]
else:
    ville = input('Indiquez la ville: ')
meteo_details(ville)
