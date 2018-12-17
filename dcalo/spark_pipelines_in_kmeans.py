#Uso de tuberías en
#Análisis clúster no Jerárquico K-means en Spark
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler
from pyspark import SparkConf, SparkContext
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.ml.regression import DecisionTreeRegressor
from pyspark.ml.feature import VectorIndexer
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.feature import VectorAssembler
from pyspark import SparkConf, SparkContext
sc = SparkContext(master='local',appName="HOME")

# Definir el 'df' Spark a utilizar
df = spark.createDataFrame([
    ('line_1', 100, 10, 1),
    ('line_2', 200, 20, 2),
    ('line_3', 300, 30, 2),
    ('line_4', 300, 30, 3),
    ('line_5', 200, 20, 1),
    ('line_6', 100, 10, 1)
],  ("label", "x1", "x2", "x3"))

# Definir un ensamblador de las columnas 'x1', 'x2' y 'x3' que toma como salida 'aux_features'
assembler = VectorAssembler(inputCols=["x1", "x2","x3"], outputCol="features")

# Crear la tuberia
pipelineResult = Pipeline()
# Definir las etapas de las que está compuesta la tuberia
pipelineResult.setStages([assembler])

# Modelo de ajuste de la tuberia con los datos 'df' de entrada
modelResult = pipelineResult.fit(df)

# Realiza la transformación de los datos utilizando el modelo
result_df = modelResult.transform(df)


# Definir el modelo de k-means.
kmeans = KMeans().setK(3).setSeed(1)
model = kmeans.fit(result_df)

# Obtener la suma cuadrada de errores 'SSE'
SSE = model.computeCost(result_df)
print ("Suma cuadrada de errores: " + str(SSE))

# Obtener el número de elementos
n = result_df.count()

# Calcular el error cuadratico medio 'RMSE'
RMSE = math.sqrt(SSE/n)
print ("Error cuadratico medio: " + str(RMSE))

# Mostrar los centroides.
centers = model.clusterCenters()
print("Cluster Centers: ")
for center in centers:
    print(center)

