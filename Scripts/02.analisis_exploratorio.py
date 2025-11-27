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


# ---------------------------------EMPLEADO CON MAYOR PRODUCTIVIDAD---------------------------------------------

# 3. IDENTIFICAR LA FILA CON EL VALOR MÁXIMO

# Usamos idxmax() para encontrar el índice de la fila con el valor más alto en la columna 'ProductivityIndex'

indice_max_prod = dataframe['ProductivityIndex'].idxmax()

# 4. EXTRAER LA INFORMACIÓN DEL EMPLEADO MÁS PRODUCTIVO

empleado_mas_productivo = dataframe.loc[indice_max_prod]

# 5. MOSTRAR EL RESULTADO

print("--- EMPLEADO CON LA MAYOR PRODUCTIVIDAD ---")

print(empleado_mas_productivo[['EmployeeID', 'Department', 'HoursPerWeek', 'PerformanceScore', 'Satisfaction', 'ProductivityIndex']])

