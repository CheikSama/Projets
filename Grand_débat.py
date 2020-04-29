# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 10:18:47 2020

@author: csamassa
"""

import pandas as pd
import os
import re
import nltk
import numpy as np
os.chdir(r"C:\Users\csamassa\Desktop\Mémoire\Nouveau GDN")
#exploration pour extraire les qo: pas nécessaire de tout importer pour ça dans un premier temps
demo=pd.read_csv("DEMOCRATIE_ET_CITOYENNETE.csv", 
                 sep=",",
                 #nrows=10,
                 usecols=[0,10,2,11,13,14,16,17,19,20,22,23,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,45,46,47]
                 ,dtype={"authorZipCode":object}
                 )
fisc=pd.read_csv("LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES.csv", 
                 sep=",",
                 #nrows=10,
                 usecols=[0,10,2,11,12,13,14,15,16,17,18]
                 ,dtype={"authorZipCode":object}
                 )
eco=pd.read_csv("LA_TRANSITION_ECOLOGIQUE.csv", 
                sep=",",
                #nrows=10,               
                usecols=[0,10,2,11,12,14,16,17,18,20,22,23,24,25,26]
                ,dtype={"authorZipCode":object}
                )
                
org=pd.read_csv("ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS.csv", 
                sep=",",
               #nrows=10,
                usecols=[0,10,2,11,13,15,16,19,20,21,24,25,27,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43]
                ,dtype={"authorZipCode":object}
                )

# On rajoute une colonne comportant le thème de chaque question
demo.insert(column="Thème",value="DEMOCRATIE ET CITOYENNETE",loc=3)
fisc.insert(column="Thème",value="LA FISCALITE ET LES DEPENSES PUBLIQUES",loc=3)
eco.insert(column="Thème",value="LA TRANSITION ECOLOGIQUE",loc=3)
org.insert(column="Thème",value="ORGANISATION DE L'ETAT ET DES SERVICES PUBLIQUES",loc=3)


# On nettoie le début des questions
def clean_question(df):
    colonnes=df.columns
    colonnes1=[re.sub(pattern=r"\bQ[A-Za-z0-9]+\s+\-\s",repl='',string=nom) for nom in colonnes]
    return(colonnes1)



# On applique tt en même temps
demo.columns,fisc.columns,eco.columns,org.columns=clean_question(demo),clean_question(fisc),clean_question(eco),clean_question(org)
col1=["id", "authorZipCode","Thème"]

def empiller(df):
    stack_0=df.loc[:, ~df.columns.isin(col1)].stack(dropna=False) # prend les QO (toutes les questions sauf celles de col1)
    stack_1=stack_0.reset_index()                                 # On supp l'index pour avoir le level 0 pour la future jointure
    stack_2=stack_1.merge(df[col1],left_on="level_0",right_index=True,how="left")
    stack_2.columns=["idx_0","Question","Réponse","id","authorZipCode","Thème"] #idx_0 c'est le numéro de la ligne dans le fichier original de chaque thème
    stack_2.dropna(inplace=True)
    return stack_2


demo_1,fisc_1,eco_1,org_1=empiller(demo),empiller(fisc),empiller(eco),empiller(org)

del(demo,fisc,eco,org)# On supp les variables inutiles de l'environnement

contributions_emp=pd.concat([demo_1,fisc_1,eco_1,org_1],axis=0)   #On met tout dans un même df
 
contributions_emp.reset_index(drop=True,inplace=True)

del(demo_1,fisc_1,eco_1,org_1,col1)

contributions_emp.drop(columns="id", inplace=True) # On supp la colonne (on a qu'à utiliser idx_0 si on veut la trace des contributions)

contributions_emp.to_csv('contributions.csv')

########################################reprendre le script à partir de là

contributions=pd.read_csv('contributions.csv')


def compte_group(df,nom,fichier=None,export=False):
    resultat=df.loc[df["Réponse"].str.contains(nom,case=False, regex=True)]
    ###On va mettre chaque thème dans une feuille différente
    ##D'abord on filtre les résultats par thèmes
   
    if export==True:
        resultat_1=resultat.loc[resultat["Thème"]=="DEMOCRATIE ET CITOYENNETE"]
        resultat_2=resultat.loc[resultat["Thème"]=="LA FISCALITE ET LES DEPENSES PUBLIQUES"]
        resultat_3=resultat.loc[resultat["Thème"]=="LA TRANSITION ECOLOGIQUE"]
        resultat_4=resultat.loc[resultat["Thème"]=="ORGANISATION DE L'ETAT ET DES SERVICES PUBLIQUES"] # je sais que c'est public mais changer ça est trop chiant à faire pzrce que faudra changer le nom des thèmes (ou y'a la faute aussi)
    
        writer = pd.ExcelWriter(fichier+'.xlsx', engine='xlsxwriter')
    
        resultat_1.to_excel(writer, sheet_name="DEMOCRATIE")
        resultat_2.to_excel(writer, sheet_name="FISCALITE")
        resultat_3.to_excel(writer, sheet_name="TRANSITION_ECOLOGIQUE")
        resultat_4.to_excel(writer, sheet_name="ORGANISATION_DE_LETAT") 
    
        writer.save()
    return(resultat)

corona=compte_group(contributions,r"\bpand[e-é]mi[a-z]\b|\b[e-é]pid[e-é]mie\b|\bsras\b|\bcoronavirus\b",export=True, fichier="corona")

############################################################################################################################
# Text mining
####Confidentiel####
