## -------------Librerias-----------------------

import sys, os # Para definir directorio (ruta) desde donde se cargan los archivos
import pandas as pd # Para manipular datos
import numpy as np # Para manipular datos
from datetime import datetime # Para medir tiempos de carga
import warnings # Para suprimir "warnings"
warnings.filterwarnings(action='ignore') # Para suprimir "warnings"
import janitor # Para limpiar nombres de columnas
import Storage # Para abrir y guardar archivos pickle

## -------Carga de archivos desde Excel-----------

# inicio=datetime.now()
# # Abrir archivo de Empresas Críticas (EECC)
# os.chdir('C:\\Users\\lalarcon\\OneDrive - Mutual\\Escritorio\\Luis\\Proyectos Data Science\\PRP')
# pd.set_option('display.max_columns', None)
# base_eecc=pd.read_excel('Listado_Resumido_EECC2022_Feb_V5.xlsx')

# # Abrir archivo Asignaciones y Responsabilidad
# regiones=pd.read_excel('Estructura Comunas__.xlsx') # Para regiones
# rm=pd.read_excel('r pais 14-02.xlsx') # Para RM

# # Abrir archivos PGP
# os.chdir('C:\\Users\\lalarcon\\OneDrive - Mutual\\Escritorio\\Luis\\Proyectos Data Science\\PRP\\PGP')
# dx_plan_mejora_ct=pd.read_csv('Listado DiagPGP por Año 20220503.csv',sep=';', encoding='latin-1')

# # Abrir archivos Dynamics
# os.chdir('C:\\Users\\lalarcon\\OneDrive - Mutual\\Escritorio\\Luis\\Proyectos Data Science\\PRP\\Dynamics')
# dx_ct_dx_sv=pd.read_excel('Consolidado 25-11.xlsx')
# print('Codigo demora: ',datetime.now()-inicio,'en correr')

## --------------Transformar archivos a formato pickle----------------

# Empresas Críticas (EECC)
# os.chdir('C:\\Users\\lalarcon\\OneDrive - Mutual\\Escritorio\\Luis\\Proyectos Data Science\\PRP')
# Storage.guardarpickle('Listado_Resumido_EECC2022_Feb_V5',base_eecc)

# Asignaciones y Responsabilidad
# Storage.guardarpickle('Estructura Comunas__',regiones)
# Storage.guardarpickle('r pais 14-02',rm)

# PGP
# os.chdir('C:\\Users\\lalarcon\\OneDrive - Mutual\\Escritorio\\Luis\\Proyectos Data Science\\PRP\\PGP')
# Storage.guardarpickle('Listado DiagPGP por Año 20220503',dx_plan_mejora_ct)

# Dynamics
# os.chdir('C:\\Users\\lalarcon\\OneDrive - Mutual\\Escritorio\\Luis\\Proyectos Data Science\\PRP\\Dynamics')
# Storage.guardarpickle('Consolidado 25-11',dx_ct_dx_sv)


## -------Carga archivos formato pickles-----------
inicio=datetime.now()
# Abrir archivo de Empresas Críticas (EECC)
os.chdir('C:\\Users\\lalarcon\\OneDrive - Mutual\\Escritorio\\Luis\\Proyectos Data Science\\PRP')
pd.set_option('display.max_columns', None)
base_eecc=Storage.cargarpickle('Listado_Resumido_EECC2022_Feb_V5')

# Abrir archivo Asignaciones y Responsabilidad
regiones=Storage.cargarpickle('Estructura Comunas__') # Para regiones
rm=Storage.cargarpickle('r pais 14-02') # Para RM

# Abrir archivos PGP
os.chdir('C:\\Users\\lalarcon\\OneDrive - Mutual\\Escritorio\\Luis\\Proyectos Data Science\\PRP\\PGP')
dx_plan_mejora_ct=Storage.cargarpickle('Listado DiagPGP por Año 20220503')

# Abrir archivos Dynamics
os.chdir('C:\\Users\\lalarcon\\OneDrive - Mutual\\Escritorio\\Luis\\Proyectos Data Science\\PRP\\Dynamics')
dx_ct_dx_sv=Storage.cargarpickle('Consolidado 25-11')
print('Codigo demora: ',datetime.now()-inicio,'en correr')

## -------# Crear ID: ADH_ZONAL_GCLIENTE_CARTERA ----------------
base_eecc.insert(loc=0, column='id', value=base_eecc['N° Adherente'].map(str)+base_eecc['Gerencia Zonal SSO']+base_eecc['G.Cliente']+base_eecc['Cartera'])


