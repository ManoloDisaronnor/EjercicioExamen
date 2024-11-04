class Envio:
    def __init__(self, idEnvio, peso, entregado):
        self.__idEnvio = idEnvio
        self.__peso = peso
        self.__entregado = entregado

    @property
    def idEnvio(self):
        return self.__idEnvio

    @idEnvio.setter
    def idEnvio(self, value):
        self.__idEnvio = value
        
    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, value):
        self.__peso = value

    @property
    def entregado(self):
        return self.__entregado

    @entregado.setter
    def entregado(self, value):
        self.__entregado = value

    def __str__(self):
        return f"ID: {self.__idEnvio}, Peso: {self.__peso}kg, Entregado: {'Si' if self.__entregado else 'No'}"

if __name__ == '__main__':
    e = Envio("1", 20.0, True)
    print(e)
    print(e)