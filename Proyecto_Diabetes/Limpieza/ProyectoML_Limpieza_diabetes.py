# -*- coding: utf-8 -*-
"""ProyectoMachineLearning_Diabetes.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Zgvwy4S5gVC1LTNa00t2ffsKu9IwwTLk

# Dataset load_diabetes de Scikit-Learn

El dataset `load_diabetes` es un conjunto de datos incluido en la librería Scikit-Learn que se utiliza comúnmente en **problemas de regresión**. El objetivo principal de este dataset es proporcionar información relevante para predecir el progreso de la diabetes (variable `progression`) en un año en función de un conjunto de variables independientes.

[Podemos encontrar la información de este dataset en la documentación de sklearn.](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html)
"""

import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Cargar el dataset load_diabetes
data = load_diabetes()

df = pd.DataFrame(data.data, columns=data.feature_names)
y_progression = data.target  # Variable progresión original
df['progression'] = y_progression

df

"""Si nos damos cuenta, las variables tienen valores extraños. Sobre todo `age` y `sex` que por intuición deberían ser valores enteros o por lo menos mayores que cero.

Cuando se tengan dudas de este tipo (en la vida real) siempre es conveniente retroceder a la fuente e intentar aclarar dudas con "el dueño del dato". En este caso al ser un ejemplo ficticio nuestra fuente de información es la documentación de sklearn.

La cual muestra:
`sklearn.datasets.load_diabetes(*, return_X_y=False, as_frame=False, scaled=True)`

Aparentemente con un parámetro de escalamiento.
"""

import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Cargar el dataset load_diabetes
data = load_diabetes(scaled=False)

df = pd.DataFrame(data.data, columns=data.feature_names)
y_progression = data.target  # Variable progresión original
df['progression'] = y_progression

df

"""### Variables

Las variables en este dataset se dividen en dos tipos: variables independientes y variable dependiente.

**Variable Dependiente:**
- `progression`: Esta variable es la que pretendemos predecir en un supuesto modelo. Representa la medida del progreso de la diabetes en un paciente después de un año. En términos médicos, se refiere a cómo la enfermedad ha avanzado en términos de su impacto en la salud del paciente durante un período de un año.

Un valor más alto de "progression" indica un mayor avance de la enfermedad en comparación con un valor más bajo.

**Variables Independientes:**
El dataset contiene 10 variables independientes que se consideran **posibles características predictoras** para el progreso de la diabetes. Estas variables son todas de tipo cuantitativo.

1. `age`: Edad del paciente en años.
2. `sex`: Género del paciente (0 para mujer, 1 para hombre).
3. `bmi`: Índice de masa corporal (BMI) del paciente.
4. `bp`: Presión arterial promedio.
5. `s1`: Concentración de suero de tipo s1.
6. `s2`: Concentración de suero de tipo s2.
7. `s3`: Concentración de suero de tipo s3.
8. `s4`: Concentración de suero de tipo s4.
9. `s5`: Concentración de suero de tipo s5.
10. `s6`: Concentración de suero de tipo s6.

Cada una de las variables independientes representa diferentes aspectos relacionados con la salud y la biología de los pacientes, y se espera que puedan ser utilizadas para predecir el progreso de la diabetes.

### Tipos de Datos

- `progression`: Cuantitativo Continuo
- `age`, `bmi`, `bp`, `s1`, `s2`, `s3`, `s4`, `s5`, `s6`: Cuantitativo Continuo
- `sex`: Cualitativo Nominal (0 para mujer, 1 para hombre), aunque aparentemente en la versión de sklearn tenemos una versión modificada.

## Transformar a problema de clasificación
"""

import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Cargar el dataset load_diabetes
data = load_diabetes(scaled=False)

df = pd.DataFrame(data.data, columns=data.feature_names)
y_progression = data.target  # Variable progresión original

# Definir el umbral para la clasificación
umbral = 150  # Ejemplo de umbral, puedes ajustarlo según sea necesario
y_binary = np.where(y_progression >= umbral, 1, 0)

df['crítica_level'] = y_binary

df

import matplotlib.pyplot as plt
import seaborn as sns

# Análisis de la variable dependiente "crítica_level"
sns.set(style="whitegrid")
plt.figure(figsize=(6, 4))
sns.countplot(x="crítica_level", data=df)
plt.title("Distribución de 'crítica_level'")
plt.xlabel("Nivel Crítico")
plt.ylabel("Número de Casos")
plt.show()

"""##Conclusiones gráfico "Distribución de 'critical_level'"

El gráfico muestra la distribución de la variable "Critical_level" en dos categorías: 0 (menos crítico) y 1 (más crítico).

1. **Distribución de Casos**:
  - Hay más casos en la categoría 0 que en la categoría 1. Esto sugiere que una mayor cantidad de pacientes tiene un "Critical_level" menor a 150, indicando un menor progreso de la diabetes después de un año.
2. **Implicaciones Médicas**:
 - La transformación de la variable "progression" a "Critical_level" permite identificar fácilmente a los pacientes con mayor riesgo (valor 1). Esto es útil para priorizar el tratamiento y seguimiento de estos pacientes.
3. **Clasificación Binaria**:
 - La elección del umbral de 150 facilita la clasificación binaria, permitiendo la aplicación de algoritmos de clasificación para predecir la gravedad del progreso de la diabetes en nuevos pacientes basados en sus características iniciales.

En resumen, la mayoría de los pacientes en el dataset tienen un "Critical_level" menor a 150, lo que sugiere que el progreso de la diabetes es menos crítico en estos casos. Esta distribución puede ayudar en el desarrollo de modelos predictivos que identifiquen a los pacientes que requieren mayor atención médica.
"""

# Análisis exploratorio de datos
print(df.head())  # Muestra las primeras filas del DataFrame
print(df.info())  # Información sobre las columnas y tipos de datos
print(df.describe())  # Estadísticas descriptivas de las variables

# Visualización
#Observar el efecto de la correlación entre dos variables con PAIRPLOT
sns.set(style="whitegrid", context="notebook")
sns.pairplot(df, hue="crítica_level", diag_kind="kde")
plt.show()

# Matriz de correlación
correlation_matrix = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=.5)
plt.title("Matriz de Correlación")
plt.show()

"""##Conclusiones de la matriz de correlaciones (Clasificación)
La matriz de correlación muestra las relaciones entre las variables del conjunto de datos de diabetes. Los valores de correlación varían de -1 a 1, donde -1 indica una correlación negativa perfecta, 0 indica ninguna correlación y 1 indica una correlación positiva perfecta.

1.   **Correlación con la variable dependiente (Critical_level)**:

 - **S5 (concentración de suero)**: Es la variable con la correlación más alta con Critical_level, con un valor de 0.5. Esto sugiere que S5 es un buen predictor del progreso de la diabetes.
 - **BMI (índice de masa corporal)**: Tiene una correlación de 0.45 con Critical_level, lo que indica que también es un predictor significativo.
  - **BP (presión arterial) y S6 (otra concentración de suero)**: Tienen correlaciones de 0.38 y 0.32 respectivamente, mostrando una relación moderada con Critical_level.

2. **Correlaciones entre variables independientes**:

 - **S1 y S2**: Estas variables están altamente correlacionadas entre sí (0.9), lo cual podría indicar multicolinealidad. Esto podría ser importante al considerar modelos predictivos.
 - **S2 y S4**: También muestran una correlación alta (0.66), lo cual es otra señal de multicolinealidad.
 - **S3 y S4**: Tienen una correlación negativa alta (-0.74), sugiriendo que estas variables se mueven en direcciones opuestas.


3. **Otras observaciones**

  - **Age (edad)**: Tiene correlaciones bajas con Critical_level (0.16) y con otras variables. Esto sugiere que la edad podría no ser un buen predictor del progreso de la diabetes en este dataset.
  - **Sex (género)**: Tiene una correlación mínima con Critical_level (0.022), indicando que el género probablemente no afecta significativamente el progreso de la diabetes en este conjunto de datos.
  
En resumen, para predecir la variable Critical_level, sería útil centrarse en S5, BMI, BP, y S6 debido a sus correlaciones relativamente altas. Sin embargo, es importante considerar la multicolinealidad entre las variables S1 y S2, y entre S2 y S4.

$$
\ln\left(\frac{p}{1 - p}\right) = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \ldots + \beta_k x_k
$$

Donde:
- ($\ln$) es la función logaritmo natural,
- ($p$) es la probabilidad de éxito (en nuestro caso, la probabilidad de que "crítica\_level" sea 1)
- ($\beta_0$, $\beta_1$, $\beta_2$, $\ldots$, $\beta_k$\) son los coeficientes de regresión para las variables independientes ($x_1$, $x_2$, $\ldots$, $x_k$).

<br>

\begin{align*}
\text{Hipótesis Nula ($H_0$):} & \quad \beta_i = 0 \quad \text{(La variable no tiene efecto)} \\
\text{Hipótesis Alternativa ($H_1$):} & \quad \beta_i \neq 0 \quad \text{(La variable tiene efecto)}
\end{align*}
"""

import statsmodels.api as sm

# Pruebas de hipótesis (usando statsmodels)
X = df.drop("crítica_level", axis=1)
X = sm.add_constant(X)  # Agregar constante para la regresión
y = df["crítica_level"]

model = sm.Logit(y, X)
result = model.fit()

print("="*90)

# Crear una tabla para mostrar los resultados y la relevancia de variables
table_data = result.summary().tables[1].data[1:]  # Excluir la primera fila (encabezados)
columns = ["X","Coeficiente", "Std Err", "Z", "P>|z|", "[0.025", "0.975]"]
summary_df = pd.DataFrame(table_data, columns=columns)

# Convertir las columnas numéricas a tipo float
for column in columns:
  if(column != "X"):
    summary_df[column] = pd.to_numeric(summary_df[column], errors="coerce")
  else:
    pass

# Agregar la columna "Variable Relevante" basada en el p-value y una significancia de 0.05
summary_df["Relevante"] = summary_df["P>|z|"].apply(lambda p: "Sí" if p <= 0.05 else "No")

# Imprimir la tabla con la decisión de relevancia
print(summary_df)

"""## Analizar el problema de regresión"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_diabetes
from scipy.stats import ttest_ind

# Cargar el conjunto de datos de diabetes
data = load_diabetes(scaled=False)
df = pd.DataFrame(data.data, columns=data.feature_names)
df['progression'] = data.target

# Información general sobre el dataset
print("Información general:")
print(df.info())

# Estadísticas descriptivas
print("\nEstadísticas descriptivas:")
print(df.describe())

# Distribución de la variable 'progression'
plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='progression', bins=20, kde=True)
plt.title("Distribución de 'progression'")
plt.xlabel("Nivel de Progresión")
plt.ylabel("Frecuencia")
plt.show()

"""
##Conclusión Gráfico Histograma "Distribución de 'progression'"

El eje X del gráfico representa el nivel de progresión de la diabetes y el eje Y representa la frecuencia. En este caso, la distribución de la variable objetivo "progression" parece ser aproximadamente unimodal.

Si bien no se puede determinar la forma exacta de la distribución (por ejemplo, normal, sesgada a la derecha) a partir del histograma provisto, sí se puede observar que la mayoría de los valores de progresión se encuentran en el rango de 50 a 150.

Es importante tener en cuenta que este es solo un análisis visual de la distribución y se necesitarían pruebas estadísticas formales para confirmar cualquier suposición"""

# Correlación entre variables
correlation_matrix = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=.5)
plt.title("Matriz de Correlación")
plt.show()

"""##Conclusión de matriz de correlaciones (Regresión)

La matriz de correlación muestra las relaciones entre las variables del conjunto de datos de diabetes. Los valores de correlación varían de -1 a 1, donde -1 indica una correlación negativa perfecta, 0 indica ninguna correlación y 1 indica una correlación positiva perfecta.

1. **Correlación con la variable dependiente**: Las variables con la correlación más fuerte con la variable dependiente "progression" son:

  - **s6**: Concentración de suero de tipo s6 (r = 0.57)
  - **s5**: Concentración de suero de tipo s5 (r = 0.53)
  - **age**: Edad del paciente en años (r = 0.44)
  - **s4**: Concentración de suero de tipo s4 (r = 0.43)
  - **bmi**: Índice de masa corporal (BMI) del paciente (r = 0.41)

  Estas variables tienen una correlación positiva con la variable dependiente "progression", lo que significa que a medida que aumentan los valores de estas variables, también aumenta el valor de la variable dependiente "progression".

2. **Correlación entre variables independientes**: Las variables con la correlación más débil con la variable dependiente "progression" son:

  - **sex**: Género del paciente (0 para mujer, 1 para hombre) (r = 0.043)

  Esta variable tiene una correlación muy débil con la variable dependiente "progression", lo que significa que no hay una relación significativa entre el género del paciente y el progreso de la diabetes.

En general, la matriz de correlación proporciona información valiosa sobre las relaciones entre las variables del conjunto de datos de diabetes. Esta información puede ser utilizada para desarrollar un modelo de regresión para predecir el progreso de la diabetes.
"""

# Visualización
sns.set(style="whitegrid", context="notebook")
sns.pairplot(df, hue="progression", diag_kind="kde")
plt.show()

# Análisis de características individuales con 'progression'
features = data.feature_names
for feature in features:
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=feature, y='progression', data=df)
    plt.title(f"{feature} vs Progression")
    plt.xlabel(feature)
    plt.ylabel("Progression")
    plt.show()

# Comparación de 'progression' entre sexos
male_progression = df[df['sex'] == 1]['progression']
female_progression = df[df['sex'] == 0]['progression']
t_stat, p_value = ttest_ind(male_progression, female_progression)
print("\nComparación de 'progression' entre sexos:")
print(f"T-estadística: {t_stat}")
print(f"P-valor: {p_value}")

print("Información general del conjunto de datos:")
print(df.info())

print("\nPrimeros registros del conjunto de datos:")
print(df.head())

print("\nEstadísticas descriptivas del conjunto de datos:")
print(df.describe())