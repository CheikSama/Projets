#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 13:05:56 2018

@author: cheiksamassa
"""

import pandas as pd



path= '/Users/cheiksamassa/Desktop/Programmation et données structurées/Orientation post bac.csv'
df_postbac= pd.read_csv(path, sep=',' )

print(df_postbac)

df_postbac2= df_postbac.iloc[:, [1,2,3, 18, 19,20,21,22,23,24,25,26,27,28,29,30,31]]

print(df_postbac.iloc[:,[30]])
df_postbac2=df_postbac2.fillna('X')



liste1= ['Architecte', 'Commandant', 'Logicien']
liste2= ['Défenseur', 'Médiateur', 'Protagoniste', 'Militant']
liste3=['Logisticien', 'Protecteur', 'Exécuteur', 'Consul']
liste4=['Virtuose', 'Aventurier', 'Entrepreneur', 'Artiste']


df_postbac2.columns

mots= ['^.*' +liste1[0]+ '.*$',  '^.*' +liste1[1]+ '.*$',  '^.*' +liste1[2]+ '.*$']
mots1=['^.*' +liste2[0]+ '.*$',  '^.*' +liste2[1]+ '.*$',  '^.*' +liste2[2]+ '.*$','^.*' +liste2[3]+ '.*$']
mots2=['^.*' +liste3[0]+ '.*$',  '^.*' +liste3[1]+ '.*$',  '^.*' +liste3[2]+ '.*$','^.*' +liste3[3]+ '.*$']
mots3=['^.*' +liste4[0]+ '.*$',  '^.*' +liste4[1]+ '.*$',  '^.*' +liste4[2]+ '.*$', '^.*' +liste4[3]+'.*$']

df_postbac2.loc[:,['La personnalité qui te définit le mieux ']].replace([mots,mots1],[1,2], regex=True, inplace=True)
df_postbac2.loc[:,['La personnalité qui te définit le mieux ']]= df_postbac.loc[:,['La personnalité qui te définit le mieux ']].replace([mots,mots1,mots2,mots3],['1','2','3','4'], regex=True)

print(df_postbac2.iloc[:,[15]])

"""possible soluce https://stackoverflow.com/questions/36072626/pandas-replace-multiple-values-at-once/36073001"""


df_postbac2.loc[:,['La personnalité qui te définit le mieux ']].replace((mots,mots1),(1,2), regex=True)



