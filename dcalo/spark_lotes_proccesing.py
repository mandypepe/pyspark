# El DataFrame propio de Spark "pyspark" acelera el procesamiento de los datos
from pyspark.sql.types import *
from pyspark import SparkConf, SparkContext
sc = SparkContext(master='local',appName="HOME")
pathText = "/databricks-datasets/structured-streaming/events/"
jsonSchema = StructType([
                 StructField("time", TimestampType(), True),
                 StructField("action", StringType(), True)
             ])

# DataFrame que representa datos en los archivos JSON
df = (
  spark
    .read
    .schema(jsonSchema)
    .json(pathText)
)

# Visualizar el DataFrame
display(df)


#Agrupar un DataFrame por minuto y tipo
# Definir el DataFrame agrupado por minuto a partir del original
df_by_min2 = (
  df
    .groupBy(
       df.action,
       window(df.time, "1 minute"))   # 1 hour ...
    .count()
)
# Visualizar el DataFrame
display(df_by_min2)


# Almacenar el DataFrame como una tabla de SparkQL
df.createOrReplaceTempView("view_df")

# Realizar la consulta
result = spark.sql("SELECT action, COUNT(time) as total FROM view_df group by action")

# Visualizar el resultado de la consulta SQL
result.show()