#Uso de tuberías en arboles de decisión

from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler
from pyspark import SparkConf, SparkContext
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.ml.regression import DecisionTreeRegressor
from pyspark.ml.feature import VectorIndexer
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.feature import VectorAssembler
sc = SparkContext(master='local',appName="HOME")
# Cargar un dataframe
df = sqlContext.read.format("com.databricks.spark.csv").options(delimiter='\t',header='true',inferschema='true').load("/databricks-datasets/power-plant/data")
display(df)
#Definir una semilla
seed = 1800009193
# Generar un grupo de entrenamiento y otro de prueba con una proporción 80-20
(split20DF, split80DF) = df.randomSplit([.2, .8], seed=seed)

# Cachear los conjuntos de datos
testSetDF = split20DF.cache()
trainingSetDF = split80DF.cache()
display(trainingSetDF)

# Definir un vector de ensamblado para que las variables de entrada se queden en una sola "features"
vectorizer = VectorAssembler()
vectorizer.setInputCols(["AT", "V", "AP", "RH"])
vectorizer.setOutputCol("features")

# Definir molelo de arbol de regresión
dt = DecisionTreeRegressor()

# Definir los parametros del modelo:
# - Predicted_PE: columna que almacenará las predicciones estimadas
# - features: columna que almacena el vector de variables predictoras
# - PE: columna que almacena la predicción real
# - 8 niveles de profundidad
dt.setPredictionCol("Predicted_PE").setMaxBins(100).setFeaturesCol("features").setLabelCol("PE").setMaxDepth(8)

# Crear una 'pipeline' en la cual hay 2 elementos,
# un 'Vector Assembler' y un modelo 'Decision Tree',
# accesibles mediante el atributo 'stages'.
pipeline = Pipeline(stages=[vectorizer, dt])

# Ajustar el modelo (Ejecutar)
model = pipeline.fit(trainingSetDF)

# Visualizar los resultados
vectAssembler = model.stages[0]
dtModel = model.stages[1]
print("Nodos: " + str(dtModel.numNodes))
print("Profundidad: "+ str(dtModel.depth)) # summary only
print(dtModel.toDebugString)
# prediciones
predictions = model.transform(testSetDF)
display(predictions)

####################################  EVAL MODEL
# Cargar libreria de evaluación
from pyspark.ml.evaluation import RegressionEvaluator
# Evaluación mediante el metodo de regresion
regEval = RegressionEvaluator(predictionCol="Predicted_PE", labelCol="PE", metricName="rmse")

# Evaluación 1 - RMSE:  Error cuadrático medio
rmse = regEval.evaluate(predictions)
print(" Error cuadrático medio (RMSE): %.2f" % rmse)

# Evaluación 2 - r2: Coeficiente de determinación
r2 = regEval.evaluate(predictions, {regEval.metricName: "r2"})
print("coeficiente de determinación (r2): {0:.2f}".format(r2))

 # Almacenar los datos en una tabla para poder mostrar estadisticas
sqlContext.sql("DROP TABLE IF EXISTS Power_Plant_RMSE_Evaluation")
dbutils.fs.rm("dbfs:/user/hive/warehouse/Power_Plant_RMSE_Evaluation", True)
predictions.selectExpr("PE", "Predicted_PE", "PE - Predicted_PE Residual_Error", "(PE - Predicted_PE) / {} Within_RSME".format(rmse)).registerTempTable("Power_Plant_RMSE_Evaluation")


