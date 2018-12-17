#Regresión lineal simple en python
from sklearn.datasets.samples_generator import make_blobs
from sklearn.linear_model import LinearRegression
from time import time


# Generación de un dataset de 2 dimensiones X e Y
X, Y = make_blobs(n_samples=1000, centers=2, n_features=2, random_state=1)

start_time = time()

# Definir el modelo de regresión
model = LinearRegression()

# Calcular la regresión
model.fit(X, Y)

# Calcular tiempo empleado en realizar la regresión
elapsed_time = time() - start_time
print("Elapsed time: %.10f seconds." % elapsed_time)

# Mostrar los resultados de la regresión
m = model.coef_[0]
b = model.intercept_
print("slope=", m, "intercept=", b)