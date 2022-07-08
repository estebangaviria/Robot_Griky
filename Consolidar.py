from importlib.resources import path
from operator import index
from unittest.mock import patch
import pandas as pd
import os
import glob
import xlwt 
import time
import numpy as np


#pip install xlrd
#pip install xlwt

def borrar():
    py_files = glob.glob('C:/Users/Administrator/Downloads/*.xls')
    for xls_file in py_files:
        try:
            os.remove(xls_file)
        except OSError as e:
            print(f"Error:{ e.strerror}")
            pass


def generar_archivo(path_destino):

    path = 'C:/Users/Administrator/Downloads'
    xls_files = glob.glob(os.path.join(path, "*.xls"))
    today = time.strftime('%m-%d-%Y')
    dataframes= []
    
    if len(xls_files) > 0:
        # loop over the list of xls files
        for i in xls_files:
            
            # read the xls file
            df = pd.read_excel(i)
            dataframes.append(df)

        print('Cantidad de arvhivos:'+ str(len(dataframes)))
        df_consolidado = pd.concat(dataframes)
        df_consolidado.to_excel(path_destino+"Profesionales_"+today+".xlsx", index=False)



    py_files = glob.glob('C:/Users/Administrator/Downloads/*.xls')

    for xls_file in py_files:
        try:
            os.remove(xls_file)
        except OSError as e:
            print(f"Error:{ e.strerror}")



    print('Archivo generado con exito')
    # print(type(df_consolidado))
    #print(df_consolidado.columns)


# df_autonoma = df_consolidado[df_consolidado['Course Id'].str.contains('autonoma+', case=False)].dropna(axis=1, how='all')
# df_cablemas = df_consolidado[df_consolidado['Course Id'].str.contains('cablemas+', case=False)].dropna(axis=1, how='all')
# df_clase = df_consolidado[df_consolidado['Course Id'].str.contains('clase+', case=False)].dropna(axis=1, how='all')
# df_classrun = df_consolidado[df_consolidado['Course Id'].str.contains('classrun+', case=False)].dropna(axis=1, how='all')
# df_corona = df_consolidado[df_consolidado['Course Id'].str.contains('corona+', case=False)].dropna(axis=1, how='all')
# df_eanx = df_consolidado[df_consolidado['Course Id'].str.contains('eanx+', case=False)].dropna(axis=1, how='all')
# df_edp = df_consolidado[df_consolidado['Course Id'].str.contains(':edp+', case=False)].dropna(axis=1, how='all') #problem
# df_globali = df_consolidado[df_consolidado['Course Id'].str.contains('global-i+', case=False)].dropna(axis=1, how='all')
# df_griky = df_consolidado[df_consolidado['Course Id'].str.contains('griky+', case=False)].dropna(axis=1, how='all')
# df_holastaff = df_consolidado[df_consolidado['Course Id'].str.contains('holastaff+', case=False)].dropna(axis=1, how='all')
# df_isep = df_consolidado[df_consolidado['Course Id'].str.contains('isep+', case=False)].dropna(axis=1, how='all') #problem
# df_istte = df_consolidado[df_consolidado['Course Id'].str.contains('istte+', case=False)].dropna(axis=1, how='all')
# df_konfio = df_consolidado[df_consolidado['Course Id'].str.contains('konfio+', case=False)].dropna(axis=1, how='all')
# df_ocf = df_consolidado[df_consolidado['Course Id'].str.contains('ocf+', case=False)].dropna(axis=1, how='all')
# df_onconnection = df_consolidado[df_consolidado['Course Id'].str.contains('onconnection+', case=False)].dropna(axis=1, how='all')
# df_robinfood = df_consolidado[df_consolidado['Course Id'].str.contains('robinfood+'or 'demo4+', case=False)].dropna(axis=1, how='all')#problem
# df_sura = df_consolidado[df_consolidado['Course Id'].str.contains('sura+', case=False)].dropna(axis=1, how='all')
# df_ugb = df_consolidado[df_consolidado['Course Id'].str.contains('ugb+', case=False)].dropna(axis=1, how='all')
# df_uma = df_consolidado[df_consolidado['Course Id'].str.contains('uma+', case=False)].dropna(axis=1, how='all') #problem
# df_umecit = df_consolidado[df_consolidado['Course Id'].str.contains('umecit+', case=False)].dropna(axis=1, how='all')


# df_autonoma.to_excel("./Instancias/Autonoma/Profesionales/Profesionales_"+today+".xlsx", index=False)
# df_cablemas.to_excel("./Instancias/Cablemas/Profesionales/Profesionales_"+today+".xlsx", index=False)
# df_clase.to_excel("./Instancias/Clase/Profesionales/Profesionales_"+today+".xlsx", index=False)
# df_classrun.to_excel("./Instancias/Classrun/Profesionales/Profesionales_"+today+".xlsx", index=False)
# df_corona.to_excel("./Instancias/Corona/Profesionales/Profesionales_"+today+".xlsx", index=False)
# df_eanx.to_excel("./Instancias/Eanx/Profesionales/Profesionales_"+today+".xlsx", index=False)
# df_edp.to_excel("./Instancias/Edp/Profesionales/Profesionales_"+today+".xlsx", index=False)
# df_globali.to_excel("./Instancias/Globali/Profesionales/Profesionales_"+today+".xlsx", index=False)
# df_griky.to_excel("./Instancias/Griky/Profesionales/Profesionales_"+today+".xlsx", index=False)
# df_holastaff.to_excel("./Instancias/Holastaff/Profesionales/Profesionales_"+today+".xlsx", index=False)
# df_isep.to_excel("./Instancias/Isep/Profesionales/Profesionales_"+today+".xlsx", index=False)
# df_istte.to_excel("./Instancias/Istte/Profesionales/Profesionales_"+today+".xlsx", index=False)
# df_konfio.to_excel("./Instancias/Konfio/Profesionales/Profesionales_"+today+".xlsx", index=False)
# df_ocf.to_excel("./Instancias/Ocf/Profesionales/Profesionales_"+today+".xlsx", index=False)
# df_onconnection.to_excel("./Instancias/Onconnection/Profesionales/Profesionales_"+today+".xlsx", index=False)
# df_robinfood.to_excel("./Instancias/Robinfood/Profesionales/Profesionales_"+today+".xlsx", index=False)
# df_sura.to_excel("./Instancias/Sura/Profesionales/Profesionales_"+today+".xlsx", index=False)
# df_ugb.to_excel("./Instancias/Ugb/Profesionales/Profesionales_"+today+".xlsx", index=False)
# df_uma.to_excel("./Instancias/Uma/Profesionales/Profesionales_"+today+".xlsx", index=False)
# df_umecit.to_excel("./Instancias/Umecit/Profesionales/Profesionales_"+today+".xlsx", index=False)

# import shutil 
# shutil.rmtree('/path/to/folder')

#generar_archivo(path_destino='C:/')