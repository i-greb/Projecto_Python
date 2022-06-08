class lista:
    __distancia = []
    __tiempo = []
    __velocidadInicial = []
    __velocidadFinal = []
#agregar las 4 variables en una sola variable de 4 espacios
    def agregarDatos(self):
        self.__distancia.append(20)
        self.__tiempo.append(25)
        self.__velocidadFinal.append(20)
        self.__velocidadInicial.append(80)

    def mostrarDatos(self):
        for x in self.__distancia:
            print(x)
        for x in self.__tiempo:
            print(x)
        for x in self.__velocidadInicial:
            print(x)
        for x in self.__velocidadFinal:
            print(x)
if __name__ == "__main__":
    lista=lista()
    lista.agregarDatos()
    lista.mostrarDatos()

