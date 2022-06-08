from abc import ABC, abstractmethod

class distancia(ABC):

    @staticmethod
    def calcularDistanciaRecorrida(velocidad, tiempo):
        return velocidad * tiempo

class pruebaArchivos:

    def leerArchivo(self, archivo):
        file = open(archivo, 'r')
        lineas = []
        lineas_archivo = []
        for linea in file.readlines():
            lineas.append(linea.replace('\n','').split("-")) #convierte a arreglo multidimensional.
        file.close()

        #
        for f in range(0, len(lineas)):
            try:
                lineas_archivo.append([float(lineas[f][0]), float(lineas[f][1])])
            except ValueError:
                lineas_archivo.append([0,0])
        return lineas_archivo

    def calcularDistancia(self, lista):
        resultado =[]
        for f in range(0,len(lista)):
            resultado.append(distancia.calcularDistanciaRecorrida(lista[f][0], lista [f][1]))
        return resultado

    #para guardar los resultados en un archivo
    def guardarResultados(self, entrada, resultado):
        file = open("resultados.txt", "w") #guarda los resultados en el archivo
        file.write('velocidad - tiempo - resultado \n')
        for f in range (0,len(entrada)):
            linea = str(entrada[f][0]) + '\t' '\t' + str(entrada[f][1]) + '\t' + str(resultado[f]) + '\n'
            file.write(linea)
        file.close()

if __name__ == "__main__":
    prueba = pruebaArchivos()
    archivo = []
    archivo = prueba.leerArchivo("valores.txt")
    print(archivo)
    print(len(archivo))
    resultado = prueba.calcularDistancia(archivo)
    print(resultado)
    prueba.guardarResultados(archivo, resultado)

#En la línea 8 se reemplaza los saltos de línea