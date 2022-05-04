# Importar paquetes

import pandas as pd # paquete para manejar datos
from pandas_profiling import ProfileReport
import numpy as np # paquete para manejar datos
import matplotlib.pyplot as plt # paquete para graficar
%matplotlib inline # para graficar
import janitor # para limpiar los nombres de la base de datos
import seaborn as sns
import lifelines
import statistics
from sklearn.impute import SimpleImputer
from lifelines import KaplanMeierFitter, CoxPHFitter # Paquete para modelos de sobrevida
from lifelines.statistics import logrank_test # paquete para modelos de sobrevida
from scipy import stats
from datetime import date # paquete para manejar formatos fecha

# Ingesta de Datos
## Excels 
df = pd.read_excel('nombre.xlsx').clean_names() #para subir excels
## Csv
df = pd.read_csv('nombre.xlsx', sep=';').clean_names() # Los archivos csv siempre los separamos en ;
## Pickle
import Storage as ST
ST.cargarpickle('ISTAS_pickle')

# Guardar datos
## Excel 
df.to_excel('nombre archivo.xlsx')
## Csv
df.to_csv('nombre archivo.csv', sep=';')
## Pickle
import Storage as ST
ST.guardarpickle(df,nombre archivo) # Se deja el nombre del archivo sin punto
