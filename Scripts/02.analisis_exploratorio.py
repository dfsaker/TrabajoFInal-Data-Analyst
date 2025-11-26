import pandas as pd

dataframe=pd.read_csv("employee_corregido.csv")



# ---------------ANALISIS EXPLORATORIO CON PYTHON--------------------------------



#CALCULAR PROMEDIOS DE PRODUCTIVIDAD POR DEPARTAMENTO



print(dataframe['ProductivityIndex'].max())

print('PROMEDIOS DE PRODUCTIVIDAD POR DEPARTAMENTO')

print(dataframe.groupby("Department")["ProductivityIndex"].mean())

"-------------------------------------------------------------------------------------------------"

# COMPARAR RENDIMIENTO ENTRE TRABAJADORES REMOTOS Y PRESENCIALES 

print('RENDIMIENTO ENTRE TRABAJADORES REMOTOS Y PRESENCIALES')

print(dataframe.groupby("RemoteWork")["ProductivityIndex"].mean())


"--------------------------------------------------------------------------------------------"

#VER RELACION ENTRE AUSENCIAS Y RENDIMIENTOS

print('RELACION ENTRE AUSENCIAS Y RENDIMIENTOS')

print(dataframe.groupby("Absences")["ProductivityIndex"].mean())

print(dataframe['Absences'].value_counts()) 


#-------------------------------- "PRODUCTIVIDAD GENERAL"-----------------------------



Productividad_General=dataframe["ProductivityIndex"].mean()


print(f"EL ÍNDICE DE PRODUCTIVIDAD PROMEDIO GENERAL DE LA EMPRESA ES: {Productividad_General:.3f}")


