import pandas as pd 

dataframe=pd.read_csv("employee_nuevo.csv")

print(dataframe)

# ----------------------LIMPIEZA DE DATOS ------------------------------

#IDENTIFICAR Y REEMPLAZAR VALORES FALTANTES EN SATISFACTION O PERFOMANCESCORE

print(dataframe.isnull().sum())


#ESTANDARIZAR VARIABLES CATEGORICAS YES/NO. 


#PRODUCTIVITYINDEX = (PERFORMANCESCORE + SATISFACTION * 10) / HOURSPERWEEK

dataframe['ProductivityIndex'] = (dataframe['PerformanceScore'] + dataframe['Satisfaction']*10)/ dataframe['HoursPerWeek']


print(dataframe)

dataframe.to_csv("employee_corregido.csv")