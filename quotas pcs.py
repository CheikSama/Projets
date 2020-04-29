# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 17:17:21 2019

@author: csamassa
"""
import pandas as pd
import os
import numpy as np
import re
os.chdir(r"C:\Users\csamassa\Desktop\eurostat")
fichier2= pd.read_csv("codes_pays1.csv", sep=';')

dico_functions= {1:"population par nuts1",2:"catégorie_professionelle", 3:"actifs", 4:"inactifs", 5:"chomage", 6:"ça suffit"}



####################################################
def quotas_pcs(): 
    
    
    fichier4= pd.read_csv("lfsa_egais.tsv", sep='\t', usecols=[0,1])
    fichier5=pd.read_csv("Occupation.csv", sep=";")
    fichier6=pd.read_csv("classe_age.csv", sep=";")

    fichier5.columns= ["OC","libellé_OC"]
    fichier6.columns= ["year","libellé_year"]

    asupp=fichier4.loc[fichier4.iloc[:,0].str.contains(r"\bDE_TOT\b|EA|EU|EFTA|UNK|\bAL\b|LI", regex=True)]
    fichier4.drop(index=asupp.index, inplace=True)


#on vérifie qu'on a tous les mêmes pays: c'est bon sauf pour AL et LI du coup on les ajoute à asupp

    """for k,v in dico_pays_codes.items():
    if v["Code"] in fichier4.iloc[:,0].str[-2:].unique():
        print(v["Code"],"c'est ok")
    else:
        print(v["Code"], "c'est pas ok")
        
        """
        
        
        
    fichier4["Code"]=fichier4.iloc[:,0].str[-2:]
    fichier4=fichier4.merge(fichier2, on="Code")
    
#on garde que les données chiffrées et on les converti
        
    
    fichier4_11= fichier4.loc[fichier4["2018 "].str.contains("[0-9]")]
    fichier4_11["2018 "].replace("[a-zA-Z]","", regex=True,inplace=True)
    
    fichier4_22= fichier4.loc[~fichier4["2018 "].str.contains("[0-9]")]
    fichier4_22["2018 "].replace(":|[a-zA-Z]",np.nan, regex=True, inplace=True)
    
    fichier4_propre=pd.concat([fichier4_22,fichier4_11],axis=0)
    
###On enlève toutes les lettres
    
    fichier4_propre["2018 "]=fichier4_propre["2018 "].apply(float)
#On remet en milliers


    fichier4_propre["OC"]=fichier4_propre["unit,sex,age,wstatus,isco08,geo\\time"].str.extract("(OC[0-9])")
## les charactères qu icommencent par un Y suivi d'un (nombre de 1-9 et d'un nombre de 0-9 :=> 10-99) et se terminant par un tiret puis de la même chose
    fichier4_propre["year"]=pd.concat([fichier4_propre["unit,sex,age,wstatus,isco08,geo\\time"].str.extract("((Y([1-9][0-9]))-([1-9][0-9]))")[0].dropna(),# on prend la première colonne sinon ça met les autres niveaux 
                                  fichier4_propre["unit,sex,age,wstatus,isco08,geo\\time"].str.extract("(Y_GE([1-9][0-9]))")[0].dropna()], # Ysuivi de _GE et d'un nombre de 1-9 et d'un nombre de 0-9 :=> 10-99 
                                    axis=0) #enfin on enlève les NaN

    fichier4_propre["sexe"]= pd.concat([fichier4_propre["unit,sex,age,wstatus,isco08,geo\\time"].str.extract('(,T,)').dropna(),
                                   fichier4_propre["unit,sex,age,wstatus,isco08,geo\\time"].str.extract('(,F,)').dropna(),
                                   fichier4_propre["unit,sex,age,wstatus,isco08,geo\\time"].str.extract('(,M,)').dropna()], 
                                    axis=0)

    fichier4_propre["sexe"].replace("\,", "", regex=True,inplace=True)

    fichier4_propre=fichier4_propre.merge(fichier5, on="OC")
    fichier4_propre=fichier4_propre.merge(fichier6, on="year")
    
    
                
    
        
    
    def pcs_quotas():
        dico_variables_filtre= {1:"Occupation", 2:"Sexe",3: "Age"}
        dico_OC= fichier4_propre.groupby(by=["OC","libellé_OC"], as_index=False).count().loc[:,["OC","libellé_OC"]].to_dict(orient='index')
        dico_sexe= {1:"Female", 2:"Male", 3:"Total"}
        dico_pays_pcs= fichier4_propre.groupby(by=["Pays"], as_index=False).count().to_dict(orient="index")
        dico_age_interv_pcs= fichier4_propre.groupby(by=["year","libellé_year"], as_index=False).count().loc[:,["year","libellé_year"]].to_dict(orient='index')

        while True:
            try:
                while True:
                    for k,v in dico_pays_pcs.items():
                        print(k,"=>",v["Pays"])
                
                    try: 
    
                        pays_pcs=int(input("choisir un pays: "))
                        if pays_pcs in range(len(dico_pays_pcs)+1):
                
                            print("vous avez selectionné",dico_pays_pcs[pays_pcs]["Pays"],"\n")
            #là on va utiliser notre dico de df je pense ça va aller plus vite
                            donnees_pays_pcs= fichier4_propre.loc[fichier4_propre['Pays']==dico_pays_pcs[pays_pcs]["Pays"]]
                            print(donnees_pays_pcs)
                            break
                        else:
                            print("veuillez réessayer")
            
                    except ValueError:
                        print('Value')
                    except TypeError:
                        print('Type')
                
                while True:
                    for k,v in dico_variables_filtre.items():
                        print(k,"=>",v,"\n")
                
                    try: 
                
                        variable=int(input("quelle variable souhaitez vous filtrer ?"))
                        if variable in range(1,len(dico_variables_filtre)+1):
                            if variable==1:        
                                while True:
                                    for k,v in dico_OC.items():
                                        print(k,"=>",v["OC"],"-->",v["libellé_OC"])
            
                                    try:

                                        OC= int(input("Choisir une occupation: "))
                                        if OC in range(0,len(dico_OC)+1):
                                            print("vous avez selectionné l'Occupation  ",dico_OC[OC]["libellé_OC"],"\n")
                                            donnees_OC_pcs= donnees_pays_pcs.loc[donnees_pays_pcs["OC"]==dico_OC[OC]["OC"]]
                                             
                                            
                                            
                                            return donnees_OC_pcs
                                            break
                                        else:
                                            print("Veuillez réessayer")
                                    except ValueError:
                                        print('Value')
                                    except TypeError:
                                        print('Type')
                
                            elif variable==2:
                                while True:
                                    for k,v in dico_sexe.items():
                                        print(k,"=>",v,"\n")
                                        
                                    try:
                
                                        sexe = int(input("choisir un sexe: "))
                                        if sexe in range(1,len(dico_sexe)+1):
                                            print("vous avez selectionné",dico_sexe[sexe],"\n")
                                            donnees_sexe_pcs= donnees_pays_pcs.loc[donnees_pays_pcs["sexe"]==dico_sexe[sexe][0]] # tu me prends la première lettre de la string correspondant à la variable sexe(int) dans le dico_sexe: par ex, 2=male, => "m"
                                            return donnees_sexe_pcs
                                            break
                                        else: 
                                            print("Veuillez réessayer")
                                            
                                    except ValueError:
                                        print('Value')
                                    except TypeError:
                                        print('Type')
     
                            elif variable==3:
                                while True:
                                    for k,v in dico_age_interv_pcs.items():
                                        print(k,"=>",v["year"],"-->",v["libellé_year"])
    
                                    try:
                                        age_pcs=int(input("Veuillez choisir un intervalle: "))
                                    
                                        if age_pcs in range(0,len(dico_age_interv_pcs)+1):
                                            donnees_age_pcs= donnees_pays_pcs.loc[donnees_pays_pcs["year"]==dico_age_interv_pcs[age_pcs]["year"]]
                                            return donnees_age_pcs
                                            break
                                
                                        else:
                                            print("veuillez réessayer")
                                    except ValueError:
                                        print('Value')
                                    except TypeError:
                                        print('Type')
                    
                    
                                
                        else:
                            print("Veuillez réessayer")
                                   
                    except ValueError:
                        print('Value')
                    except TypeError:
                        print('Type')
            
            except ValueError:
                print('Value')
            except TypeError:
                print('Type')
                
                
    ###version où on filtre tout###
    def pcs_quotas_1():
            
        dico_OC= fichier4_propre.groupby(by=["OC","libellé_OC"], as_index=False).count().loc[:,["OC","libellé_OC"]].to_dict(orient='index')
        dico_sexe= {1:"Female", 2:"Male", 3:"Total"}
        dico_pays_pcs= fichier4_propre.groupby(by=["Pays"], as_index=False).count().to_dict(orient="index")
        dico_age_interv_pcs= fichier4_propre.groupby(by=["year","libellé_year"], as_index=False).count().loc[:,["year","libellé_year"]].to_dict(orient='index')
            
        while True:
            for k,v in dico_pays_pcs.items():
                print(k,"=>",v["Pays"])
                    
            try: 
    
                pays_pcs=int(input("choisir un pays: "))
                if pays_pcs in range(len(dico_pays_pcs)+1):
                        
                    print("vous avez selectionné",dico_pays_pcs[pays_pcs]["Pays"],"\n")
                    #là on va utiliser notre dico de df je pense ça va aller plus vite
                    donnees_pays_pcs= fichier4_propre.loc[fichier4_propre['Pays']==dico_pays_pcs[pays_pcs]["Pays"]]
                    print(donnees_pays_pcs)
                    break
               
                else:
                    print("veuillez réessayer")
            
            except ValueError:
                print('Value')
            except TypeError:
                print('Type')
                
        
        while True:
            for k,v in dico_OC.items():
                print(k,"=>",v["OC"],"-->",v["libellé_OC"])
            
            try:

                OC= int(input("Choisir une occupation: "))
                if OC in range(0,len(dico_OC)+1):
                    print("vous avez selectionné l'Occupation  ",dico_OC[OC]["libellé_OC"],"\n")
                    donnees_OC_pcs= donnees_pays_pcs.loc[donnees_pays_pcs["OC"]==dico_OC[OC]["OC"]]

                    print(donnees_OC_pcs)
                    break
                else:
                    print("Veuillez réessayer")
                
            except ValueError:
                print('Value')
            except TypeError:
                print('Type')
                
                            
        while True:
            for k,v in dico_sexe.items():
                print(k,"=>",v,"\n")
                                        
            try:
                
                sexe = int(input("choisir un sexe: "))
                if sexe in range(1,len(dico_sexe)+1):
                    print("vous avez selectionné",dico_sexe[sexe],"\n")
                    donnees_sexe_pcs= donnees_OC_pcs.loc[donnees_OC_pcs["sexe"]==dico_sexe[sexe][0]] # tu me prends la première lettre de la string correspondant à la variable sexe(int) dans le dico_sexe: par ex, 2=male, => "m"
                    print(donnees_sexe_pcs)
                    break
                else: 
                    print("Veuillez réessayer")
                                            
            except ValueError:
                print('Value')
            except TypeError:
                print('Type')
     
                            
        while True:
            for k,v in dico_age_interv_pcs.items():
                print(k,"=>",v["year"],"-->",v["libellé_year"])
    
            try:
                age_pcs=int(input("Veuillez choisir un intervalle: "))
                                    
                if age_pcs in range(0,len(dico_age_interv_pcs)+1):
                    donnees_age_pcs= donnees_sexe_pcs.loc[donnees_sexe_pcs["year"]==dico_age_interv_pcs[age_pcs]["year"]]
                    return donnees_age_pcs
                    break
                                
                else:
                    print("veuillez réessayer")
            except ValueError:
                print('Value')
            except TypeError:
                print('Type')
    
    
    dico_oui_non= {"OUI v1":1, "OUI v2":2, "NON":3}
    liste_stockage=[]
    


    while True: 
        for k,v in dico_oui_non.items():
            print(k,"->",v)
        try:
            tour2= int(input("souhaitez vous ajouter des infos à votre tableau ?: " ))
            if tour2== 1:
                liste_stockage.append(pcs_quotas())                                       
                
            elif tour2== 2:
                liste_stockage.append(pcs_quotas_1()) 
            elif tour2== 3:
                break
        
            else:
                print("veuillez réessayer")    
        except ValueError: 
            print ("vérifiez la valeur")
        except TypeError: 
            print ("vérifiez le type")
    
        result= pd.concat(liste_stockage, axis=0)
        print(result)

    while True:
        try:
        
            nom_fichier= input("saisir un nom pour le fichier excel à exporter: ")
          
  
    # Make own character set and pass  
    # this as argument in compile method 
            regex = re.compile('[@!#$%^&*()<>?/\|}{~:]') 
      
    # Pass the string in search  
    # method of regex object.     
            if(regex.search(nom_fichier) == None): 
            
                xlsx= nom_fichier+r".xlsx"
                print(xlsx, "is accepted")     
                result.to_excel(xlsx)
                break
          
            else: 
                print("String is not accepted. Réessayer...") 
            
        except ValueError:
            print("Erreur de valeur. Réessayer...")
        except TypeError:
            print("Erreur de type. Réessayer...")

#########################################################
def quotas_inactifs():
    
    fichier4_1= pd.read_csv("lfsa_igan.tsv", sep='\t', usecols=[0,1])
    fichier6_4= pd.read_csv("classe_age_inactifs.csv", sep=";", encoding="utf-8")

    fichier6_4.columns= ["year","libellé_year"]

        
    asupp=fichier4_1.loc[fichier4_1.iloc[:,0].str[-4:].str.contains(r"DE_TOT|EA|EU|EFTA|UNK|AL|LI")]
    fichier4_1.drop(index=asupp.index, inplace=True)
    fichier4_1["Code"]=fichier4_1.iloc[:,0].str[-2:]
    fichier4_1=fichier4_1.merge(fichier2, on="Code")

    fichier4_111= fichier4_1.loc[fichier4_1["2018 "].str.contains("[0-9]")]
    fichier4_111["2018 "].replace("[a-zA-Z]","", regex=True,inplace=True)
    
    fichier4_122= fichier4_1.loc[~fichier4_1["2018 "].str.contains("[0-9]")]
    fichier4_122["2018 "].replace(":|[a-zA-Z]",np.nan, regex=True, inplace=True)
    
    fichier4_1propre=pd.concat([fichier4_122,fichier4_111],axis=0)

    fichier4_1propre["2018 "]=fichier4_1propre["2018 "].apply(float)
    fichier4_1propre["year"]=pd.concat([fichier4_1propre["unit,sex,age,citizen,geo\\time"].str.extract("((Y([1-9][0-9]))-([1-9][0-9]))")[0].dropna(),# on prend la première colonne sinon ça met les autres niveaux 
                                  fichier4_1propre["unit,sex,age,citizen,geo\\time"].str.extract("(Y_GE([1-9][0-9]))")[0].dropna()], # Ysuivi de _GE et d'un nombre de 1-9 et d'un nombre de 0-9 :=> 10-99 
                                    axis=0) #enfin on enlève les NaN

    fichier4_1propre["sexe"]= pd.concat([fichier4_1propre["unit,sex,age,citizen,geo\\time"].str.extract('(,T,)').dropna(),
                                   fichier4_1propre["unit,sex,age,citizen,geo\\time"].str.extract('(,F,)').dropna(),
                                   fichier4_1propre["unit,sex,age,citizen,geo\\time"].str.extract('(,M,)').dropna()], 
                                    axis=0)

    fichier4_1propre["sexe"].replace("\,", "", regex=True,inplace=True)
    fichier4_1propre=fichier4_1propre.merge(fichier6_4, on="year")
    
    def inactifs_quotas():
        
        dico_sexe= {1:"Female", 2:"Male", 3:"Total"}
        dico_pays_inactifs= fichier4_1propre.groupby(by=["Pays"], as_index=False).count().to_dict(orient="index")
        dico_age_interv_inactifs= fichier4_1propre.groupby(by=["year","libellé_year"], as_index=False).count().loc[:,["year","libellé_year"]].to_dict(orient='index')  
        while True:
            for k,v in dico_pays_inactifs.items():
                print(k,"=>",v["Pays"])
                    
            try: 
    
                pays_inactifs=int(input("choisir un pays: "))
                if pays_inactifs in range(len(dico_pays_inactifs)+1):
                        
                    print("vous avez selectionné",dico_pays_inactifs[pays_inactifs]["Pays"],"\n")
                    #là on va utiliser notre dico de df je pense ça va aller plus vite
                    donnees_pays_inactifs= fichier4_1propre.loc[fichier4_1propre['Pays']==dico_pays_inactifs[pays_inactifs]["Pays"]]
                    print(donnees_pays_inactifs)
                    break
               
                else:
                    print("veuillez réessayer")
            
            except ValueError:
                print('Value')
            except TypeError:
                print('Type')
                
        
                
                            
        while True:
            for k,v in dico_sexe.items():
                print(k,"=>",v,"\n")
                                        
            try:
                
                sexe = int(input("choisir un sexe: "))
                if sexe in range(1,len(dico_sexe)+1):
                    print("vous avez selectionné",dico_sexe[sexe],"\n")
                    donnees_sexe_inactifs= donnees_pays_inactifs.loc[donnees_pays_inactifs["sexe"]==dico_sexe[sexe][0]] # tu me prends la première lettre de la string correspondant à la variable sexe(int) dans le dico_sexe: par ex, 2=male, => "m"
                    print(donnees_sexe_inactifs)
                    break
                else: 
                    print("Veuillez réessayer")
                                            
            except ValueError:
                print('Value')
            except TypeError:
                print('Type')
     
                            
        while True:
            for k,v in dico_age_interv_inactifs.items():
                print(k,"=>",v["year"],"-->",v["libellé_year"])
    
            try:
                age_inactifs=int(input("Veuillez choisir un intervalle: "))
                                    
                if age_inactifs in range(0,len(dico_age_interv_inactifs)+1):
                    donnees_age_inactifs= donnees_sexe_inactifs.loc[donnees_sexe_inactifs["year"]==dico_age_interv_inactifs[age_inactifs]["year"]]
                    return donnees_age_inactifs
                    break
                                
                else:
                    print("veuillez réessayer")
            except ValueError:
                print('Value')
            except TypeError:
                print('Type')

    dico_oui_non= {"OUI":1, "NON":2}
    liste_stockage=[]
    

    while True: 
        for k,v in dico_oui_non.items():
            print(k,"->",v)
        try:
            tour2= int(input("souhaitez vous ajouter des infos à votre tableau ?: " ))
            if tour2== 1:
                liste_stockage.append(inactifs_quotas())                                       
                
            elif tour2== 2:
                break
        
            else:
                print("veuillez réessayer")    
        except ValueError: 
            print ("vérifiez la valeur")
        except TypeError: 
            print ("vérifiez le type")
    
        result= pd.concat(liste_stockage, axis=0)
        print(result)

    while True:
        try:
        
            nom_fichier= input("saisir un nom pour le fichier excel à exporter: ")
          
  
    # Make own character set and pass  
    # this as argument in compile method 
            regex = re.compile('[@!#$%^&*()<>?/\|}{~:]') 
      
    # Pass the string in search  
    # method of regex object.     
            if(regex.search(nom_fichier) == None): 
            
                xlsx= nom_fichier+r".xlsx"
                print(xlsx, "is accepted")     
                result.to_excel(xlsx)
                break
          
            else: 
                print("String is not accepted. Réessayer...") 
            
        except ValueError:
            print("Erreur de valeur. Réessayer...")
        except TypeError:
            print("Erreur de type. Réessayer...")
            
            
#################################################################
def quotas_actifs():
    
    fichier4_2= pd.read_csv("lfsa_agan.tsv", sep='\t', usecols=[0,1])
    fichier6_1=pd.read_csv("classe_age_activité.csv", sep=";")
    
    fichier6_1.columns= ["year","libellé_year"]


    asupp=fichier4_2.loc[fichier4_2.iloc[:,0].str[-4:].str.contains(r"DE_TOT|EA|EU|EFTA|UNK|AL|LI")]

    fichier4_2.drop(index=asupp.index, inplace=True)
    fichier4_2["Code"]=fichier4_2.iloc[:,0].str[-2:]
    fichier4_2=fichier4_2.merge(fichier2, on="Code")

    fichier4_211=fichier4_2.loc[fichier4_2["2018 "].str.contains("[0-9]",regex=True)]
    fichier4_211["2018 "].replace("[a-zA-Z]","", regex=True, inplace=True)

    
    fichier4_222= fichier4_2.loc[~fichier4_2["2018 "].str.contains("[0-9]")]
    fichier4_222["2018 "].replace(":|[a-zA-Z]",np.nan, regex=True, inplace=True)

    fichier4_2propre=pd.concat([fichier4_222,fichier4_211],axis=0)


    fichier4_2propre["2018 "]=fichier4_2propre["2018 "].apply(float)

    fichier4_2propre["year"]=pd.concat([fichier4_2propre["unit,sex,age,citizen,geo\\time"].str.extract("((Y([1-9][0-9]))-([1-9][0-9]))")[0].dropna(),# on prend la première colonne sinon ça met les autres niveaux 
                                  fichier4_2propre["unit,sex,age,citizen,geo\\time"].str.extract("(Y_GE([1-9][0-9]))")[0].dropna()], # Ysuivi de _GE et d'un nombre de 1-9 et d'un nombre de 0-9 :=> 10-99 
                                    axis=0) #enfin on enlève les NaN
    fichier4_2propre["sexe"]= pd.concat([fichier4_2propre["unit,sex,age,citizen,geo\\time"].str.extract('(,T,)').dropna(),
                                   fichier4_2propre["unit,sex,age,citizen,geo\\time"].str.extract('(,F,)').dropna(),
                                   fichier4_2propre["unit,sex,age,citizen,geo\\time"].str.extract('(,M,)').dropna()], 
                                    axis=0)

    fichier4_2propre["sexe"].replace("\,", "", regex=True,inplace=True)

    fichier4_2propre=fichier4_2propre.merge(fichier6_1, on="year")
    
    def actifs_quotas():
        
        dico_sexe= {1:"Female", 2:"Male", 3:"Total"}
        dico_pays_actifs= fichier4_2propre.groupby(by=["Pays"], as_index=False).count().to_dict(orient="index")
        dico_age_interv_actifs= fichier4_2propre.groupby(by=["year","libellé_year"], as_index=False).count().loc[:,["year","libellé_year"]].to_dict(orient='index')
            
        while True:
            for k,v in dico_pays_actifs.items():
                print(k,"=>",v["Pays"])
                    
            try: 
    
                pays_actifs=int(input("choisir un pays: "))
                if pays_actifs in range(len(dico_pays_actifs)+1):
                        
                    print("vous avez selectionné",dico_pays_actifs[pays_actifs]["Pays"],"\n")
                    #là on va utiliser notre dico de df je pense ça va aller plus vite
                    donnees_pays_actifs= fichier4_2propre.loc[fichier4_2propre['Pays']==dico_pays_actifs[pays_actifs]["Pays"]]
                    print(donnees_pays_actifs)
                    break
               
                else:
                    print("veuillez réessayer")
            
            except ValueError:
                print('Value')
            except TypeError:
                print('Type')
                
        
                
                            
        while True:
            for k,v in dico_sexe.items():
                print(k,"=>",v,"\n")
                                        
            try:
                
                sexe = int(input("choisir un sexe: "))
                if sexe in range(1,len(dico_sexe)+1):
                    print("vous avez selectionné",dico_sexe[sexe],"\n")
                    donnees_sexe_actifs= donnees_pays_actifs.loc[donnees_pays_actifs["sexe"]==dico_sexe[sexe][0]] # tu me prends la première lettre de la string correspondant à la variable sexe(int) dans le dico_sexe: par ex, 2=male, => "m"
                    print(donnees_sexe_actifs)
                    break
                else: 
                    print("Veuillez réessayer")
                                            
            except ValueError:
                print('Value')
            except TypeError:
                print('Type')
     
                            
        while True:
            for k,v in dico_age_interv_actifs.items():
                print(k,"=>",v["year"],"-->",v["libellé_year"])
    
            try:
                age_actifs=int(input("Veuillez choisir un intervalle: "))
                                    
                if age_actifs in range(0,len(dico_age_interv_actifs)+1):
                    donnees_age_actifs= donnees_sexe_actifs.loc[donnees_sexe_actifs["year"]==dico_age_interv_actifs[age_actifs]["year"]]
                    return donnees_age_actifs
                    break
                                
                else:
                    print("veuillez réessayer")
            except ValueError:
                print('Value')
            except TypeError:
                print('Type')

    dico_oui_non= {"OUI":1, "NON":2}
    liste_stockage=[]
    

    while True: 
        for k,v in dico_oui_non.items():
            print(k,"->",v)
        try:
            tour2= int(input("souhaitez vous ajouter des infos à votre tableau ?: " ))
            if tour2== 1:
                liste_stockage.append(actifs_quotas())                                       
                
            elif tour2== 2:
                break
        
            else:
                print("veuillez réessayer")    
        except ValueError: 
            print ("vérifiez la valeur")
        except TypeError: 
            print ("vérifiez le type")
    
        result= pd.concat(liste_stockage, axis=0)
        print(result)

    while True:
        try:
        
            nom_fichier= input("saisir un nom pour le fichier excel à exporter: ")
          
  
    # Make own character set and pass  
    # this as argument in compile method 
            regex = re.compile('[@!#$%^&*()<>?/\|}{~:]') 
      
    # Pass the string in search  
    # method of regex object.     
            if(regex.search(nom_fichier) == None): 
            
                xlsx= nom_fichier+r".xlsx"
                print(xlsx, "is accepted")     
                result.to_excel(xlsx)
                break
          
            else: 
                print("String is not accepted. Réessayer...") 
            
        except ValueError:
            print("Erreur de valeur. Réessayer...")
        except TypeError:
            print("Erreur de type. Réessayer...")
#############################################################################
def quotas_chomage():
    
    fichier4_3= pd.read_csv("lfsa_ugan.tsv", sep='\t', usecols=[0,1])
    fichier6_3=pd.read_csv("classe_age_chomage.csv", sep=";")

    fichier6_3.columns= ["year","libellé_year"]
    


    asupp=fichier4_3.loc[fichier4_3.iloc[:,0].str[-4:].str.contains(r"DE_TOT|EA|EU|EFTA|UNK|AL|LI")]

    fichier4_3.drop(index=asupp.index, inplace=True)
    fichier4_3["Code"]=fichier4_3.iloc[:,0].str[-2:]

    fichier4_3=fichier4_3.merge(fichier2,on='Code')

    fichier4_311=fichier4_3.loc[fichier4_3["2018 "].str.contains("[0-9]",regex=True)]
    fichier4_311["2018 "].replace("[a-zA-Z]","", regex=True, inplace=True)

    
    fichier4_322= fichier4_3.loc[~fichier4_3["2018 "].str.contains("[0-9]")]
    fichier4_322["2018 "].replace(":|[a-zA-Z]",np.nan, regex=True, inplace=True)

    fichier4_3propre=pd.concat([fichier4_322,fichier4_311],axis=0)

    fichier4_3propre["2018 "]=fichier4_3propre["2018 "].apply(float)


    fichier4_3propre["year"]=pd.concat([fichier4_3propre["unit,sex,age,citizen,geo\\time"].str.extract("((Y([1-9][0-9]))-([1-9][0-9]))")[0].dropna(),# on prend la première colonne sinon ça met les autres niveaux 
                                  fichier4_3propre["unit,sex,age,citizen,geo\\time"].str.extract("(Y_GE([1-9][0-9]))")[0].dropna()], # Ysuivi de _GE et d'un nombre de 1-9 et d'un nombre de 0-9 :=> 10-99 
                                    axis=0) #enfin on enlève les NaN


    fichier4_3propre["sexe"]= pd.concat([fichier4_3propre["unit,sex,age,citizen,geo\\time"].str.extract('(,T,)').dropna(),
                                   fichier4_3propre["unit,sex,age,citizen,geo\\time"].str.extract('(,F,)').dropna(),
                                   fichier4_3propre["unit,sex,age,citizen,geo\\time"].str.extract('(,M,)').dropna()], 
                                    axis=0)

    fichier4_3propre["sexe"].replace("\,", "", regex=True,inplace=True)


# le fichier contenant les classes d'age est différent ici
    fichier4_3propre=fichier4_3propre.merge(fichier6_3, on="year")
    
    def chomage_quotas():
        
        dico_sexe= {1:"Female", 2:"Male", 3:"Total"}
        dico_pays_chomage= fichier4_3propre.groupby(by=["Pays"], as_index=False).count().to_dict(orient="index")
        dico_age_interv_chomage= fichier4_3propre.groupby(by=["year","libellé_year"], as_index=False).count().loc[:,["year","libellé_year"]].to_dict(orient='index')
            
        while True:
            for k,v in dico_pays_chomage.items():
                print(k,"=>",v["Pays"])
                    
            try: 
    
                pays_chomage=int(input("choisir un pays: "))
                if pays_chomage in range(len(dico_pays_chomage)+1):
                        
                    print("vous avez selectionné",dico_pays_chomage[pays_chomage]["Pays"],"\n")
                    #là on va utiliser notre dico de df je pense ça va aller plus vite
                    donnees_pays_chomage= fichier4_3propre.loc[fichier4_3propre['Pays']==dico_pays_chomage[pays_chomage]["Pays"]]
                    print(donnees_pays_chomage)
                    break
               
                else:
                    print("veuillez réessayer")
            
            except ValueError:
                print('Value')
            except TypeError:
                print('Type')
                
        
                
                            
        while True:
            for k,v in dico_sexe.items():
                print(k,"=>",v,"\n")
                                        
            try:
                
                sexe = int(input("choisir un sexe: "))
                if sexe in range(1,len(dico_sexe)+1):
                    print("vous avez selectionné",dico_sexe[sexe],"\n")
                    donnees_sexe_chomage= donnees_pays_chomage.loc[donnees_pays_chomage["sexe"]==dico_sexe[sexe][0]] # tu me prends la première lettre de la string correspondant à la variable sexe(int) dans le dico_sexe: par ex, 2=male, => "m"
                    print(donnees_sexe_chomage)
                    break
                else: 
                    print("Veuillez réessayer")
                                            
            except ValueError:
                print('Value')
            except TypeError:
                print('Type')
     
                            
        while True:
            for k,v in dico_age_interv_chomage.items():
                print(k,"=>",v["year"],"-->",v["libellé_year"])
    
            try:
                age_chomage=int(input("Veuillez choisir un intervalle: "))
                                    
                if age_chomage in range(0,len(dico_age_interv_chomage)+1):
                    donnees_age_chomage= donnees_sexe_chomage.loc[donnees_sexe_chomage["year"]==dico_age_interv_chomage[age_chomage]["year"]]
                    return donnees_age_chomage
                    break
                                
                else:
                    print("veuillez réessayer")
            except ValueError:
                print('Value')
            except TypeError:
                print('Type')

    dico_oui_non= {"OUI":1, "NON":2}
    liste_stockage=[]
    

    while True: 
        for k,v in dico_oui_non.items():
            print(k,"->",v)
        try:
            tour2= int(input("souhaitez vous ajouter des infos à votre tableau ?: " ))
            if tour2== 1:
                liste_stockage.append(chomage_quotas())                                       
                
            elif tour2== 2:
                break
        
            else:
                print("veuillez réessayer")    
        except ValueError: 
            print ("vérifiez la valeur")
        except TypeError: 
            print ("vérifiez le type")
    
        result= pd.concat(liste_stockage, axis=0)
        print(result)

    while True:
        try:
        
            nom_fichier= input("saisir un nom pour le fichier excel à exporter: ")
          
  
    # Make own character set and pass  
    # this as argument in compile method 
            regex = re.compile('[@!#$%^&*()<>?/\|}{~:]') 
      
    # Pass the string in search  
    # method of regex object.     
            if(regex.search(nom_fichier) == None): 
            
                xlsx= nom_fichier+r".xlsx"
                print(xlsx, "is accepted")     
                result.to_excel(xlsx)
                break
          
            else: 
                print("String is not accepted. Réessayer...") 
            
        except ValueError:
            print("Erreur de valeur. Réessayer...")
        except TypeError:
            print("Erreur de type. Réessayer...")
###############################################################################
def quotas_regions(): 
    
####chargement/nettoyages/prétraitements####
    fichier1=pd.read_csv("demo_r_d2jan.tsv", sep='\t', usecols=[0,1])
    fichier3= pd.read_csv("NUTS_AT_2016.csv", sep=",")
#on renomme code pour la jointure
    fichier3.columns=['CNTR_CODE', 'Code_reg', 'NUTS_NAME']

    codes=fichier2["Code"].tolist()
    #On créé un dictionnaire dont les keys vont être les codes et les values les pays
    dico_cod_pay= dict(zip(fichier2["Code"], fichier2["Pays"]))
    fichier2.reset_index(inplace=True)
    fichier1.columns=['unit_age_sex_geo_time','Population au 1er Janvier 2018']
#On suppp tt ça  DE_TOT allemagne avant 90, EA: zone euro, EU, FX: france metropolitaine, efta: libre echange,UNK: unknown

    supp=fichier1.loc[fichier1.iloc[:,0].str.contains(r"DE_TOT|\bEA\b|EU|EFTA|UNK", regex=True)]
 
    fichier1.drop(index=supp.index, inplace=True)
###

##on met Y0, pour les 0-1 ans
    fichier1.iloc[:,0].replace(r"\bY_LT1\b", "Y0", inplace=True, regex=True)    
    fichier1['Population au 1er Janvier 2018'].replace(":", np.nan, regex=True, inplace=True)
    fichier1['Population au 1er Janvier 2018'].fillna(0, inplace=True)
    fichier1['Population au 1er Janvier 2018']=fichier1['Population au 1er Janvier 2018'].apply(int)


# on fait une fusion entre le fichier2 et le dico de df pour garder un dico qui contient les nouvelles clés et leurs pays
    def quotas_reg():
        dico_df={}
        for element in codes:
            dico_df[element]=fichier1.loc[fichier1['unit_age_sex_geo_time'].str.contains(element)]


## on rajoute une colonne code pour faire notre jointure
        for k,v in dico_df.items():
            if len(v)>1:
                v["Code"]=k
                v["Pays"]= dico_cod_pay[k]

#on supp les pays pas présents:
            
        for k,v in list(dico_df.items()):
            if len(v)<1:
                del dico_df[k]

        dico_pays_codes= fichier2.merge(pd.DataFrame(dico_df.keys(),columns=['Code']), on='Code').to_dict(orient='index')
        dico_sexe= {1:"Female", 2:"Male", 3:"Total"}
        dico_age= {1:"Un age précis", 2:"un intervalle", 3:"Pas d'âge"}

        while True:
            for k,v in dico_pays_codes.items():
                print(k,"=>",v["Pays"],"\n")
            try: 
    
                pays=int(input("choisir un pays: "))
                if pays in range(len(dico_pays_codes)+1):
                
                    print("vous avez selectionné",dico_pays_codes[pays]["Pays"],"\n")
            #là on va utiliser notre dico de df je pense ça va aller plus vite
                    donnees_pays= dico_df[dico_pays_codes[pays]["Code"]]
                    print(donnees_pays)
                    break
                else:      
                    print("veuillez réessayer")
            except ValueError:
                print('Value')
            except TypeError:
                print('Type')
            
    # le code du pays suivi d'une lettre de l'alphabet
        pattern=r"\b"+ dico_pays_codes[pays]["Code"]+ r"[a-zA-Z]\b|\b"+dico_pays_codes[pays]["Code"]+r"\b|\b"+dico_pays_codes[pays]["Code"]+r"[1-9]\b" 
        dico_regions= donnees_pays.loc[donnees_pays["unit_age_sex_geo_time"].str.contains(pattern, regex=True)]
        dico_regions.loc[:,"Code_reg"]=dico_regions.iloc[:,0].str[-3:].replace(",","",regex=True)

    #on joint le code de nuts1 à leur libéllé
        dico_regions=dico_regions.merge(fichier3, on="Code_reg")
        nuts1=dico_regions.groupby(by=['Code_reg','NUTS_NAME'], as_index=False).count()
        nuts1_dic=nuts1.loc[:,["Code_reg","NUTS_NAME"]].to_dict(orient='index')


        while True:
            for k,v in nuts1_dic.items():
                print(k,"=>",v["Code_reg"],'correspond à la région',v["NUTS_NAME"],"\n")
            try: 
            
                nuts=int(input("choisir une région: "))
                if nuts in range(len(nuts1_dic)+1):
                
                    print("vous avez selectionné la région",nuts1_dic[nuts]["NUTS_NAME"],"\n")
            #là on va utiliser notre dico de df je pense ça va aller plus vite
                    donnees_region= dico_regions.loc[dico_regions["unit_age_sex_geo_time"].str.contains(nuts1_dic[nuts]["Code_reg"])]
            
                    print( donnees_region)
                    break

                else:      
                    print("veuillez réessayer")
            
            except ValueError:
                print('Value')
            except TypeError:
                print('Type')
        
        
        
        while True:
            for k,v in dico_sexe.items():
                print(k,"=>",v,"\n")
            try:  
                sexe = int(input("choisir un sexe: "))
                if sexe in range(1,len(dico_sexe)+1):
                    print("vous avez selectionné",dico_sexe[sexe],"\n")
                    if sexe in range (1,4): # En somme on lui demande si c'est compris entre 1 et 4
                        lettre= dico_sexe[sexe][0]
                        pattern_sexe= r"\b,"+lettre+r",\b"     # On crée un pattern qui va utiliser la première lettre de la variable sexe systématiquement
                    #ce sera donc soit F, M ou T vu qu'on a dit de zapper Pas de sexe
                        donnees_sexe= donnees_region.loc[donnees_region.iloc[:,0].str.contains(pattern_sexe, regex=True)]
                        print(donnees_sexe)
               
                        break
                    else:
                        print("veuillez réessayer")
            except ValueError:
                print('Erreur de valeur')
            except TypeError:
                print('Erreur de Type')


    

        while True:
            for k,v in dico_age.items():
                print(k,"=>",v,"\n")     
            try: 
                choix_age = int(input("Souhaitez vous sélectionner: "))
                if choix_age in range(1,len(dico_age)+1):
                    print("vous avez selectionné",dico_age[choix_age],"\n")
                
                    age_max=donnees_sexe["unit_age_sex_geo_time"].str.extractall("([7-9][0-9])").max()
                    pattern_age_max= ",Y"+str(int(age_max))+r"+"
                    donnees_sexe.replace(r"\b,Y_OPEN\b", pattern_age_max, regex=True,inplace=True)

                
                    if choix_age==1:
                        while True:
                            try:
                                age_precis=int(input("quel age souhaitez vous selectionner ?: " ))
                                if age_precis in range (0,100):
                                    print("vous avez selectionné",age_precis,"ans")
                                    pattern_age= r"\b,Y"+str(age_precis)+r",\b"
                                    donnees_age_precis= donnees_sexe.loc[donnees_sexe.iloc[:,0].str.contains(pattern_age, regex=True)]
                                    return donnees_age_precis
                                    break
                                else:
                                    print("veuillez réessayer")
                            except ValueError:
                                print('Erreur de valeur')
                            except TypeError:
                                print('Erreur de Type')
                            
                            
            
                    elif choix_age ==2 :
                        while True:
                            try:
                                borne_inf=int(input("quelle est la borne inférieure?: " ))
                                borne_sup=int(input("quelle est la borne supérieure?: " ))
                                if (borne_sup in range (0,100) and borne_inf< borne_sup):
                                    print("vous avez selectionné l'intervalle suivant: ",borne_inf,'-',borne_sup,"ans")
                                    intervalle= list(range(borne_inf, borne_sup))
                                    dico_intervalle={}
                                    i=borne_inf
                                    for element in intervalle:
                                        dico_intervalle[i]= r"\b,Y"+str(element)+r",\b"
                                        i+=1
                                        
                                    liste_df=[]
                                    for k,v in dico_intervalle.items():
                                        liste_df.append(donnees_sexe.loc[donnees_sexe.iloc[:,0].str.contains(v, regex=True)])
                                    donnees_age_interv= pd.concat(liste_df, axis=0)
                                    pop= donnees_age_interv["Population au 1er Janvier 2018"].sum()
                                    
                                    print(pop)
                                    return donnees_age_interv
                                    
                            
                                    break
                                else: 
                                    print("la borne supérieure n'est pas > à la borne inférieure (ou la valeur est incorrecte), veuillez réessayer: ")                           
                            except ValueError:
                                print('Erreur de valeur')
                            except TypeError:
                                print('Erreur de Type')
                            
                    elif choix_age== 3:
                        donnees_age= donnees_sexe.copy()
                        return donnees_age
                        break
            ## je comprends pas ce dernier break: il fait en sorte qu'on sorte d'une boucle infinie mais normalement on en sort avec chaque break
                    else:
                        print("veuillez réessayer") 
                    break  
                    
                    
            
                else:
                    print("veuillez réessayer")
            except ValueError:
                print('Erreur de valeur')
            except TypeError:
                print('Erreur de Type')
        
    liste_stockage=[]
    dico_oui_non= {"OUI":1, "NON":2}

    while True: 
        for k,v in dico_oui_non.items():
            print(k,"->",v)
        try:
            tour2= int(input("souhaitez vous ajouter des infos à votre tableau ?: " ))
            if tour2== 1:
                liste_stockage.append(quotas_reg())                                       
                
            elif tour2== 2:
                break
        
            else:
                print("veuillez réessayer")    
        except ValueError: 
            print ("vérifiez la valeur")
        except TypeError: 
            print ("vérifiez le type")
    
        result= pd.concat(liste_stockage, axis=0)
        print(result)

    while True:
        try:
        
            nom_fichier= input("saisir un nom pour le fichier excel à exporter: ")
          
  
    # Make own character set and pass  
    # this as argument in compile method 
            regex = re.compile('[@!#$%^&*()<>?/\|}{~:]') 
      
    # Pass the string in search  
    # method of regex object.     
            if(regex.search(nom_fichier) == None): 
            
                xlsx= nom_fichier+r".xlsx"
                print(xlsx, "is accepted")     
                result.to_excel(xlsx)
                break
          
            else: 
                print("String is not accepted. Réessayer...") 
            
        except ValueError:
            print("Erreur de valeur. Réessayer...")
        except TypeError:
            print("Erreur de type. Réessayer...") 
###############################################################################

while True: 
    for k,v in dico_functions.items():
        print(k,"->",v)
    try:
        tour= int(input("quelle base de donnée souhaitez vous utiliser? : " ))
        if tour in range (1,5):
                print("vous avez selectionné",dico_functions[tour])
        
        if tour ==1:
            quotas_regions()
        elif tour== 2:
            quotas_pcs()                                       
                
        elif tour== 3:
            quotas_actifs()
        elif tour== 4:
            quotas_inactifs()
        elif tour== 5:
            quotas_chomage()
        elif tour== 6:
            break
        else:
            print("veuillez réessayer")    
    except ValueError: 
        print ("vérifiez la valeur")
    except TypeError: 
        print ("vérifiez le type")
###############################################################################
            
import tkinter    
from tkinter import *

window=tkinter.Tk()
window.title("GUI")
var = IntVar()

C1=tkinter.Radiobutton(window,text="population par nuts1", value=1).grid(row=0,column=0 )

C2=tkinter.Radiobutton(window,text="catégorie_professionelle",value=2).grid(row=0,column=1)
C3=tkinter.Radiobutton(window,text="actifs",value=3).grid(row=0,column=2)
C4=tkinter.Radiobutton(window,text="inactifs", value=4).grid(row=1,column=0)
C5=tkinter.Radiobutton(window,text="chomage", value=5).grid(row=1,column=1)

window.mainloop()