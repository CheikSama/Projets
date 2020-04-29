#this code is tested with pdfminer for python 3 (pdfminer-20191125)
import os 
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import re
import pdfminer
import pandas as pd

path=r"J:\test"

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.pdf' in file:
            files.append(os.path.join(r, file))


def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
 
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text


#articles=[]  
#for f in files: 
#	articles.append(convert_pdf_to_txt(f)) 

def articles_dict(files):
    dico_articles={} # La version dico garde les nom des fichiers pratique pour les déplacer plus tard
    for f in files:
        dico_articles[f]=convert_pdf_to_txt(f)
    return(dico_articles)

def articles_clean(dico)
#df_articles=pd.DataFrame(articles)

    df_articles=pd.DataFrame.from_dict(dico,orient="index")
    df_articles.reset_index(inplace=True) # pour transformer l'index en colonne
    df_articles.columns=["nom","article"]

    
##Pour exporter en excel dans plusieurs feuilles

#writer=pd.ExcelWriter("articles.xlsx", engine="xlsxwriter")
#df_articles.to_excel(writer, sheet_name='articles')
#df_annees.to_excel(writer, sheet_name='articles_année')
#articles_double.to_excel(writer, sheet_name='articles_count')
#df_annees.to_excel(writer, sheet_name='articles_année')
#articles_double.to_excel(writer, sheet_name='articles_count')

    df_articles["nom"].replace(r"\\","/",inplace=True,regex=True) # On se débarasse du formatage windows

    return(df_articles)

def extract(df_articles):
    
    df_articles["date"]=df_articles["article"].str.extract(r"Date :\s+([^\n\r]*)",flags=re.IGNORECASE) # extrait la date soit tout ce qui suit "Date : " jusqu'au prochain retour à la ligne
    
    df_articles["année"]=df_articles["date"].str.extract("(\d{2})$",flags=re.IGNORECASE) # extrait l'année soit les deux derniers digits de chaque ligne
    df_articles["annéex"]=df_articles["année"].astype(float) # converti en chiffre pour éviter d'avoir à utiliser des regex

def move_files(df_articles):
    
    for index,row in df_articles.iterrows(): # on classe chaque article dans un dossier correpondant à son année
        if row["annéex"]==16:
            shutil.move(row["nom"],r"C:\Users\csamassa\Desktop\Celine\2016")
        elif row["annéex"]==17:
	    shutil.move(row["nom"],r"C:\Users\csamassa\Desktop\Celine\2017")
        elif row["annéex"]==18:
	    shutil.move(row["nom"],r"C:\Users\csamassa\Desktop\Celine\2018")
        elif row["annéex"]==19:
	    shutil.move(row["nom"],r"C:\Users\csamassa\Desktop\Celine\2019")
        else:
	    shutil.move(row["nom"],r"C:\Users\csamassa\Desktop\Celine\autres_na") # ceux pour lesquel la regex n'a pas réussi a trouver l'année
