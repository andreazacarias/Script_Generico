# Importar paquetes

import pandas as pd # paquete para...
from pandas_profiling import ProfileReport
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import janitor
import seaborn as sns
import lifelines
import statistics
from sklearn.impute import SimpleImputer
from lifelines import KaplanMeierFitter, CoxPHFitter
from lifelines.statistics import logrank_test
from scipy import stats
from datetime import date

# Ingesta de Datos
