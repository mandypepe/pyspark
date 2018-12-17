# El DataFrame propio de Spark "pyspark" acelera el procesamiento de los datos
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark import SparkConf, SparkContext
sc = SparkContext(master='local',appName="HOME")

# Definir la ruta de donde extraer los ficheros
pathText = "/databricks-datasets/structured-streaming/events/"

# Definir la estrucutra del formato jsom a leer
jsonSchema = StructType([
                 StructField("time", TimestampType(), True),
                 StructField("action", StringType(), True)
             ])

# DataFrame que representa datos en los archivos JSON
df = (
  spark
    .readStream  # Cambiar `readStream` en lugar de `read` para leer en Streaming
    .schema(jsonSchema)   # Cargar la estructura json a leer
    .option("maxFilesPerTrigger", 1)  # Tratar los archivo como si fuera una secuencia seleccionando cada vez 1
    .json(pathText)
)

# Visualizar el DataFrame
display(df)


# Definir el DataFrame agrupado por minuto a partir del original
df_by_min = (
  df
    .groupBy(
      df.action,
      window(df.time, "1 minute"))
    .count()
)

# Fijamos un tamaño de shuffle pequeño
spark.conf.set("spark.sql.shuffle.partitions", "2")

query = (
  df_by_min
    .writeStream
    .format("memory") # memory = store in-memory table
    .queryName("table_streaming")     # Poner nombre a la tabla en memoria
    .outputMode("complete")  # complete = todos los contadores deben guardarse en la tabla
    .start()
)

