#Generar datos a utilizar para leer y escribir en formato Parquet
data = []
for x in range(5):
    data.append((random.randint(0,9), random.randint(0,9)))
df = spark.createDataFrame(data, ("label", "data"))

df.show()

# escribiendo en formato paquet
path_parquet = "/prueba.parquet" # Leer desde HDFS
path_parquet = "D:/prueba.parquet" # Leer desde fichero local

df.write.mode("overwrite").format("parquet").save(path_parquet)

#Leer datos en formato Parquet
df2 = spark.read.option("multiline", "true").parquet(path_parquet)
df2.show()

#Escribir datos en formato Parquet comprimidos con gzip

path_parquet_gzip = "/prueba_gzip.parquet" # Leer desde HDFS
path_parquet_gzip = "D:/prueba_gzip.parquet" # Leer desde fichero local

df.write.mode("overwrite").format("parquet").option("compression", "gzip").save(path_parquet_gzip)

#Leer datos en formato Parquet comprimidos con gzip

df2 = spark\
    .read\
    .option("multiline", "true") \
    .parquet(path_parquet_gzip)

df2.show()

#Escribir datos en formato Parquet comprimidos con snappy
path_parquet_snappy = "/prueba_snappy.parquet" # Leer desde HDFS
path_parquet_snappy = "D:/prueba_snappy.parquet" # Leer desde fichero local

df.write\
    .mode("overwrite")\
    .format("parquet")\
    .option("compression", "snappy")\
    .save(path_parquet_snappy)

#Leer datos en formato Parquet comprimidos con snappy
df2 = spark\
    .read\
    .option("multiline", "true") \
    .parquet(path_parquet_snappy)

df2.show()