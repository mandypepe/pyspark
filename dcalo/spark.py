from pyspark import SparkConf, SparkContext
sc = SparkContext(master='local',appName="HOME")
from argparse import ArgumentParser
import sys

def suma(n1, n2):
    return n1 + n2

diccionario = {"n1": 1, "n2": 2}
print(suma(**diccionario))


# ArgumentParser con una descripción de la aplicación
parser = ArgumentParser(description='%(prog)s is an ArgumentParser demo')
# Argumento posicional con descripción
parser.add_argument('fichero', help='ayuda del fichero')
# Argumento posicional. Si se parametriza, requiere un valor entero

parser.add_argument('valor', help='help for opt3', type=int)

# Argumento posicional con tres opciones posibles, puede llamarse con -f o -fruta

parser.add_argument('-f','--fruta', choices=['peras', 'manzanas', 'naranjas'])

# Argumento opcional con descripción. Si se parametriza requiere un entero, defecto es 10
parser.add_argument('-v', help='help for opt4', type=int, default=10)

# Argumento opcional. Con 'action' damos valor si el argumento se parametriza

parser.add_argument('-op1', '--opcion1', help='help for opt5', action='store_true', default=False)

# Argumento opcional que requiere dos argumentos
parser.add_argument('-op2', nargs=2)

# Argumento opcional que requiere de 1 a N argumentos
parser.add_argument('-op3', nargs='+')

# Argumento opcional que requiere de 0 a N argumentos
parser.add_argument('-op4', nargs='*')
# Por último parsear los argumentos
args = parser.parse_args()

# Imprimir los parámetros
print ('Fichero:', args.fichero)
print ('Numero parseado entero:', args.valor)
print ('Seleccionar frutas:', args.fruta)
print ('Seleccionar valor:', args.v)
print ('Opcion 1:', args.opcion1)
print ('Opcion 2:', args.op2)
print ('Opcion 3:', args.op3)
print ('Opcion 4:', args.op4)

# get input data:
if args.fichero != None:
    print("\n\nFichero de entrada: " + args.fichero )
    inputfile = args.fichero
else:
    sys.stderr.write("Por favor especifique el fichero!\n")
    sys.exit(2)