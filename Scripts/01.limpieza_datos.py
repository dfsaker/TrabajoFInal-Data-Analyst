import pandas as pd 

dataframe=pd.read_csv("employee_nuevo.csv")

print(dataframe)

#Limpieza de datos:

#Identificar y reemplazar valores faltantes en Satisfaction o PerformanceScore.



print(dataframe.isnull().sum())


#Estandarizar variables categóricas (por ejemplo, “Yes/No”).

#Crear una nueva columna ProductivityIndex = (PerformanceScore + Satisfaction*10) / HoursPerWeek.

dataframe['ProductivityIndex'] = (dataframe['PerformanceScore'] + dataframe['Satisfaction']*10)/ dataframe['HoursPerWeek']


print(dataframe)

dataframe.to_csv("employee_corregido.csv")