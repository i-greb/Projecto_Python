from abc import ABC

class movimientos(ABC):

    _velocidad = float(0)
    _tiempo = float(0)
    _velocidadInicial = float(0)
    _velocidadFinal = float(0)

    # constructor
    def __init__(self, tiempo):
        self._tiempo = tiempo

    @staticmethod
    def calcularDistanciaRecorrida(self):
        pass

    @staticmethod
    def calcularAceleracion(self):
        pass

    @staticmethod
    def calcularDistancia(self):
        pass

    @staticmethod
    def getDistanciaRecorrida(self):
        pass

    @staticmethod
    def getAceleracion(self):
        pass

    @staticmethod
    def getDistancia(self):
        pass


class movimientoRectilieoUniforme(movimientos):
    _distanciaRecorrida = float(0)

    def __init__(self,velocidad,tiempo):
        movimientos.__init__(self,tiempo)
        self.__velocidad = velocidad
        self.calcularDistanciaRecorrida()

    def calcularDistanciaRecorrida(self):
        self.__distanciaRecorrida= self.__velocidad * self._tiempo

    def getDistanciaRecorrida(self):
        return self.__distanciaRecorrida

class movimientoRectilineoUniformementeVariado (movimientos):
    __aceleracion = float(0)
    __distanciaRecorrida = float (0)
    def __init__(self,tiempo, velocidadInicial, velocidadFinal):
        movimientos.__init__(self, tiempo)
        self._tiempo = tiempo
        self.__velocidadInicial = velocidadInicial
        self.__velocidadFinal = velocidadFinal
        self.calcularAceleracion()
        self.calcularDistanciaRecorrida()

    def calcularAceleracion(self):
        self.__aceleracion=(self.__velocidadFinal-self.__velocidadInicial)/self._tiempo

    def calcularDistanciaRecorrida(self):
        self.__distanciaRecorrida = ((self.__velocidadFinal + self.__velocidadInicial)/2)*self._tiempo

    def getAceleracion(self):
        return self.__aceleracion

    def getDistanciaRecorrida(self):
        return self.__distanciaRecorrida








