# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 11:50:05 2020

@author: csamassa
"""
"""
import os 
import re
import pandas as pd
path = r'E:\all-data.tar\csv'

## On recueille tous les chemins de fichiers qui on l'extension csv
# r=root, d=directories, f = files
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.csv' in file:
            files.append(os.path.join(r, file))


## Jointure des noms de fichiers aux métadonnées
# On commence par extraire les noms de chaque csv
idx=[]      
for e in files[:-1]:
    capture=re.search("[0-9]*[0-9]+",e)
    if capture != None:
        grp=capture.group(0)
# On ouvre le fichier e et on lui insère une colonne id qui correspond au nom du fichier csv (sans l'extension)
        df=pd.read_csv(e)
        df.insert(loc=5,column="id",value=grp)
        idx.append(df)

#On concatène tous ces DataFrames pour les joindre aux métadonnées
df_sites= pd.concat(idx,axis=0,ignore_index=True)

#On lit les métadonnées
all_sites_csv= pd.read_csv(r"E:\all-data.tar\meta",sep=";")
df_sites["id"]=df_sites["id"].astype(int)

#On joint les deux dataframes pour enrichir all_sites des métadonnées
all_sites= df_sites.merge(all_sites_csv, left_on="id",right_on="SITE_ID")

#all_sites.to_csv(r"E:\all_sites_boss.csv") # #Pratique pour éviter d'executer tout le code qu'il y au dessus à chaque essai il suffira d'importer les données
"""
###INFLUXDB###

##PREPARATION DES DONNEES##
import pandas as pd
from influxdb import DataFrameClient
import time

client=DataFrameClient(host="localhost",port=8086) # On utilise la fonctionnalité DataFrameClient qui permet de créer une table à partir d'un DataFrame

client.switch_database("projet_nosql") # On utilise la database qu'on a créé avec une requête influx

print('chargement de la base...')
csv_read=pd.read_csv(r"E:\all_sites_boss.csv")
print('...fin chargement de la base')

print('début processing...')
csv_read.drop(axis=1, labels=["Unnamed: 0","id"],inplace=True) #On se débarrasse des colonnes inutiles

csv_read["dttm_utc"]=pd.to_datetime(csv_read["dttm_utc"],yearfirst=True) # On converti au format date pour l'utiliser en tant que time dans Influx
csv_read.index=csv_read["dttm_utc"] # il est nécessaire pour l'importation dans influx que l'index soit de format date


csv_read["timestamp"]=csv_read["timestamp"].astype(int) # On converti en integer pour faciliter les requêtes futures
print('...fin processing')

###lancement d'un timer pour voir le temps d'execution
print("chargement dans la influxdb...")
start_time=time.time()

client.write_points(dataframe=csv_read,
                    database= "projet_nosql"
                 ,measurement="ENERDOC"
                 ,tag_columns=[
                "SITE_ID",
                "INDUSTRY",
                "SUB_INDUSTRY",
                "TIME_ZONE",
                "anomaly",
                ],
                field_columns=[
                "value",
                "estimated",
                "SQ_FT",
                "LAT",
                "LNG",
                "TZ_OFFSET",
                "timestamp"
                ], batch_size=10**4)

print(time.time()-start_time,"  secondes soit",(time.time()-start_time)//60," min") # On affiche le temps d'execution en secondes et minutes
#####Requêtes###

"""
#question 0
print(client.query('SELECT  "SITE_ID", MIN("timestamp") FROM ENERDOC WHERE "SITE_ID" = \'6\' OR "SITE_ID" = \'8\' OR "SITE_ID" = \'9\' OR "SITE_ID" = \'10\' '))

#QUestion1
print(client.query('SELECT SUM("value") from ENERDOC'))

print(client.query('SELECT SUM("value") from ENERDOC GROUP BY "SUB_INDUSTRY"'))

#Question2
print(client.query('SELECT MEAN("value") FROM "ENERDOC" GROUP BY "INDUSTRY"'))

#Question3
print(client.query('SELECT SUM("value") FROM ENERDOC WHERE "timestamp" % 604800 =  259800 OR "timestamp" % 604800 = 259500 GROUP BY "SUB_INDUSTRY"'))

#question 4
print(client.query('SELECT MEAN("value") FROM ENERDOC WHERE "timestamp" % 604800 =  259800 OR "timestamp" % 604800 = 259500 GROUP BY "INDUSTRY"'))

#Question 5
print(client.query('SELECT ((SUM("SQ_FT"))/(SUM("value"))) AS "intensite_energetique" from ENERDOC GROUP BY "INDUSTRY" ORDER by time DESC'))

#Question 6
client.query('SELECT ((SUM("SQ_FT"))/(SUM("value"))) AS "intensite_energetique" FROM ENDERDOC GROUP BY "INDUSTRY","SAISON"') #saison à ajouter

#Question 7
client.query('SELECT MAX("value") FROM ENDERDOC GROUP BY "SITE_ID"')
"""
## version ligne par ligne: coûteuse, marche très bien avec peu de lignes
"""for index, rows in csv_extrait.iterrows():
    tags_0=rows[5]  # index correspondant au numéro de colonne dans notre dataframe
    tags_1=rows[6]
    tags_2=rows[7]
    tags_3=rows[11]
    tags_4=rows[4]

    value_0=rows[1]
    value_1=rows[2]
    value_2=rows[3]
    value_3=rows[8]
    value_4=rows[9]
    value_5=rows[10]
    value_6=rows[12]
    json_body=[
        {
            "measurement": "ENERNOC",
            "tags":
            {
                "SITE_ID": tags_0,
                "INDUSTRY":tags_1,
                "SUB_INDUSTRY":tags_2,
                "TIME_ZONE":tags_3,
                "anomaly": tags_4},
        
            "fields":
            {
                "dttm_utc": value_0,
                "value": value_1,
                "estimated": value_2,
                "SQ_FT": value_3,
                "LAT": value_4,
                "LNG": value_5,
                "TZ_OFFSET": value_6,
            }
        }
    ]
    print(json_body)
    client.write_points(json_body)"""

