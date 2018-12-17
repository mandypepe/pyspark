from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler
from pyspark import SparkConf, SparkContext
sc = SparkContext(master='local',appName="HOME")
# Definir el df Spark a utilizar
df = spark.createDataFrame([
    ('line_1', 1, 2, 3, 4),
    ('line_2', 5, 6, 7, 8),
    ('line_3', 9, 9, 9, 9)
], ("label", "x1", "x2", "x3", "x4"))

# Definir un ensamblador de las columnas 'x1' y 'x2' y tomar como salida 'features1'
assembler12 = VectorAssembler(inputCols=["x1", "x2"], outputCol="features1")
# Crear la tuberia
pipeline12 = Pipeline()
# Definir las etapas de las que está compuesta la tuberia
pipeline12.setStages([assembler12])

# Definir un ensamblador de las columnas 'x3' y 'x4' y tomar como salida 'features2'
assembler34 = VectorAssembler(inputCols=["x3", "x4"], outputCol="features2")
# Crear la tuberia
pipeline34 = Pipeline()
# Definir las etapas de las que está compuesta la tuberia
pipeline34.setStages([assembler34])

# Definir un ensamblador de las columnas 'features1' y 'features2' y tomar como salida 'features'
assemblerResult = VectorAssembler(inputCols=["features1", "features2"], outputCol="features")
# Crear la tuberia
pipelineResult = Pipeline()
# Definir las etapas de las que está compuesta la tuberia
pipelineResult.setStages([pipeline12, pipeline34, assemblerResult])

# Modelo de ajuste de la tuberia con los datos 'df' de entrada
modelResult = pipelineResult.fit(df)
#Realiza la transformación de los datos utilizando el modelo
result_df = modelResult.transform(df)
# Muestra los resultados
display(result_df)



# Crear la tuberia
pipelineResult = Pipeline()
# Definir las etapas de las que está compuesta la tuberia
pipelineResult.setStages([assembler12, assembler34, assemblerResult])

# Modelo de ajuste de la tuberia con los datos 'df' de entrada
modelResult = pipelineResult.fit(df)
#Realiza la transformación de los datos utilizando el modelo
result_df2 = modelResult.transform(df)
# Muestra los resultados
display(result_df2)


#Ejemplo de concatenación de tuberias 2 (optimizando las sentencias)
df = spark.createDataFrame([
    ('line_1', 1, 2, 3, 4),
    ('line_2', 5, 6, 7, 8),
    ('line_3', 9, 9, 9, 9)
], ("label", "x1", "x2", "x3", "x4"))

pipeline1 = Pipeline(stages=[
    VectorAssembler(inputCols=["x1", "x2"], outputCol="features1")
])

pipeline2 = Pipeline(stages=[
    VectorAssembler(inputCols=["x3", "x4"], outputCol="features2")
])

result = Pipeline(stages=[
    pipeline1, pipeline2,
    VectorAssembler(inputCols=["features1", "features2"], outputCol="features")
]).fit(df).transform(df)

display(result)