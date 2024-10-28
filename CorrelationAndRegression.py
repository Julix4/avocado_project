import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

# Cargar los datos (ajusta la ruta si es necesario)
df = pd.read_csv("avocado.csv")

# Convertir la columna 'Date' a formato datetime
df['Date'] = pd.to_datetime(df['Date'])

# Agrupar por trimestre y calcular los promedios
df_trimestral = df.groupby(pd.Grouper(key='Date', freq='QE')).agg({'AveragePrice': 'mean', 'Total Volume': 'mean'}).reset_index()

# Crear las variables independientes (X) y dependiente (y)
X = df_trimestral[['AveragePrice', 'Total Volume']].shift(1)  # Desplazar una fila para usar los datos del trimestre anterior
y = df_trimestral['AveragePrice'].shift(-1)  # Desplazar una fila para predecir el siguiente trimestre

# Eliminar las primeras y últimas filas con valores NaN
X.dropna(inplace=True)
y.dropna(inplace=True)

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 


# Regresión Lineal
model_linear = LinearRegression()
model_linear.fit(X_train, y_train)
y_pred_linear = model_linear.predict(X_test)


# Regresión Polinomial
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X_train)
model_poly = LinearRegression()
model_poly.fit(X_poly, y_train)

y_pred_poly = model_poly.predict(poly.transform(X_test))

# Evaluar los modelos
print("Regresión Lineal:")
print("R²:", r2_score(y_test, y_pred_linear))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred_linear)))

print("\nRegresión Polinomial:")
print("R²:", r2_score(y_test, y_pred_poly))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred_poly))) 