#fileCSV = csv.DictReader(file,delimiter=',')  con esta linea puedo pasar datos a diccionarios
'''
Puedes convertir los datos de un archivo CSV a un diccionario utilizando la 
librería estándar csv junto con la función DictReader de la librería.
La función DictReader devuelve un objeto iterable que tiene cada fila como un diccionario,
donde las claves son los nombres de las columnas y los valores son los valores de las filas.
'''

#importo la biblioteca para las funcionalidades de trabajar con archivos
import csv

def read_csv(path):  #defino una funcion a la cual le envio como argumento la ruta del archivo csv a leer
    with open(path, 'r')as csvfile:  #abrir el archivo csv el with se usa para cerrar el archivo despues de su uso
        reader = csv.reader(csvfile, delimiter = ',') #se crea un lector de csv, la ',' significa que se separa por comas
        header = next(reader)   #se utiliza para leer la primera fila del csv como las claves (los nombres de cada columna)
        data = []  #se inicializa una lista para almacenar los datos del archivo csv
        for row in reader: #itero a traves de las filas del archivo
            iterable = zip(header, row) #unimos dos arrays
            #print(list(iterable))
            country_dict = { key : value for key,value in iterable} #creo un diccionario utilizando las claves (columnas) de la primera fila y los valores de la fila actual
            data.append(country_dict)
        return data
            



#Recordar que pongo esto para correrlo como script    
if __name__== '__main__':
    data= read_csv('./data.csv')
    print(data[0])

