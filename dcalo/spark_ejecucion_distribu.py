from pyspark import SparkConf, SparkContext
#Nota: “\” se ponen para indicar al interprete del shell que la instrucción continua en la siguiente linea.

#spark-submit --master local[2] \
# /home/spark_ejecucion_distribu.py

conf = (SparkConf()
         .setMaster("local")
         .setAppName("My app")
         .set("spark.executor.memory", "1g"))

sc = SparkContext(conf = conf)

rdd = sc.parallelize([1, 1, 1, 1, 2, 2, 2, 3, 3, 4])
print(rdd.collect())

rdd2 = rdd.map(lambda x: x*2)
tSum = rdd2.reduce(lambda x,y: x+y)
print("La suma del producto total es: " + str(tSum))


##########################

#spark-submit --master local[2] \
# --executor-memory 1g \
# --name hola_mundo\
# --conf "spark.app.id=hola_mundo" \
# /home/hola_mundo.py

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Hola_Mundo").getOrCreate()
print("Hola mundo")
spark.stop()