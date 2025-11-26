import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv(r"C:\Users\d-sac\Downloads\TrabajoFInal Data Analyst\Scripts\employee_corregido.csv")

print(dataframe)

#------------------VISUALIZACION --------------------------------

# violinplot() COMPARANDO PRODUCTIVIDAD POR TIPO DE TRABAJO



plt.figure()
sns.violinplot(x="Department", y="ProductivityIndex", data=dataframe)
plt.title("Comparacion productividad por tipo de trabajo")
plt.savefig("productividad por tipo de trabajo")
plt.clf()

#barplot() de PRODUCTIVIDAD PROMEDIO POR DEPARTAMENTO 


sns.barplot(x="Department", y="ProductivityIndex", data=dataframe)
plt.title("productividad promedio por departamento.")
plt.ylabel("productividad promedio por departamento.")
plt.savefig("productividad promedio por departamento.")
plt.clf()

#scatterplot() RELACION ENTRE SATISFACION Y PERFOMANCE

plt.figure()
sns.scatterplot(x="Satisfaction", y= dataframe["PerformanceScore"].mean(), hue="Satisfaction", data=dataframe)
plt.title("Relacion entre satisfaccion y performance")
plt.ylabel("Perfomance Score")
plt.savefig("Relacion entre satisfaccion y performance")
plt.clf()





print(dataframe['Satisfaction'].max())

print(dataframe['Satisfaction'].min())