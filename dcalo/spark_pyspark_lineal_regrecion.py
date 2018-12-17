# Regresión lineal simple en Python Spark
# -*- coding: utf-8 -*-
"""
Spark Regression
"""

from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from time import time
import random

from pyspark import SparkConf, SparkContext
sc = SparkContext(master='local',appName="HOME")

# Crear la sesión de Spark
spark = SparkSession\
    .builder \
    .appName('abc')\
    .config("spark.python.worker.reuse","true") \
    .getOrCreate()

# Generación de un dataset de 2 dimensiones
data = []
for x in range(10000):
    data.append( (random.randint(0,9), random.randint(0,9)) )
df = spark.createDataFrame(data, ("label", "data"))

df.show()

# Definir la tubería que transforma los datos en entrada los que usa la regresión
result = Pipeline(stages=[
    VectorAssembler(inputCols=["data"], outputCol="features")
]).fit(df).transform(df)

start_time = time()

# Definir el modelo de regresión
lr = LinearRegression(maxIter=50, regParam=1.12)

# Calcular la regresión
model = lr.fit(result)

# Calcular tiempo empleado en realizar la regresión
elapsed_time = time() - start_time
print("Elapsed time: %.10f seconds." % elapsed_time)

# Mostrar los resultados de la regresión
print(model.coefficients)
print(model.intercept)

# Cerrar la sesión de Spark
spark.stop()