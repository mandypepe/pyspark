from math import *
import random
from pyspark import *
from pyspark.sql import *
import pyspark.sql as sc
from pyspark import SparkConf, SparkContext
import pyspark.sql.functions as F
import pandas as pd

data = []
for x in range(5):
    data.append((random.randint(0,9), random.randint(0,9)))
df = spark.createDataFrame(data, ("label", "data"))

df.show()

# escribir en json
path_json = "/prueba.json" # Leer desde HDFS
path_json = "D:/prueba.json" # Leer desde fichero local
df.write.mode("overwrite").format("json").save(path_json)

#read json
df2 = spark.read.option("multiline", "true").json(path_json)
df2.show()

#Escribir datos en formato JSON comprimidos con gzip
path_json_gzip = "/prueba_gzip.json" # Leer desde HDFS
path_json_gzip = "D:/prueba_gzip.json" # Leer desde fichero local

df.write.mode("overwrite").format("json").option("compression", "gzip").save(path_json_gzip)

#Leer datos en formato JSON comprimidos con gzip
df2 = spark.read.option("multiline", "true").json(path_json_gzip)
df2.show()

#Escribir datos en formato JSON comprimidos con deflate
path_json_deflate = "/prueba_deflate.json" # Leer desde HDFS
path_json_deflate = "D:/prueba_deflate.json" # Leer desde fichero local
df.write.mode("overwrite").format("json").option("compression", "deflate").save(path_json_deflate)

#Leer datos en formato JSON comprimidos con deflate
df2 = spark.read.option("multiline", "true").json(path_json_deflate)
df2.show()

#Escribir datos en formato JSON comprimidos con bzip2

path_json_bzip2 = "/prueba_bzip2.json" # Leer desde HDFS
path_json_bzip2 = "D:/prueba_bzip2.json" # Leer desde fichero local

df.write.mode("overwrite").format("json").option("compression", "bzip2").save(path_json_bzip2)

#Leer datos en formato JSON comprimidos con bzip2
df2 = spark.read.option("multiline", "true").json(path_json_bzip2)
df2.show()
