import pandas as pd

dataframe=pd.read_csv("employee_nuevo.csv")
#Análisis exploratorio con Python:



#Calcular promedios de productividad por departamento.

print(dataframe['Department']=='Finance')

#dataframe['Department']=='Finance'

print(dataframe['ProductivityIndex'].max())

print('Promedio de productividad por departamento')

print(dataframe.groupby("Department")["ProductivityIndex"].mean())

#Comparar rendimiento entre trabajadores remotos y presenciales.

print('Rendimiento entre trabajadores remotos y presenciales')

print(dataframe.groupby("RemoteWork")["ProductivityIndex"].mean())

#Ver relación entre ausencias y rendimiento.

print('Relacion entre ausencias y rendimientos')

print(dataframe.groupby("Absences")["ProductivityIndex"].mean())

print(dataframe['Absences'].value_counts()) 

print((dataframe['Absences']==7).value_counts())