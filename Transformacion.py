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
