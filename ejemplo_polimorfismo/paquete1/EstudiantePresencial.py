from estudiante import Estudiante

class EstudiantePresencial(Estudiante):
    def __init__(self):
        super().__init__()
        self._numero_creditos = 0
        self._costo_credito = 0.0

    def establecer_numero_creditos(self, numero):
        self._numero_creditos = numero

    def establecer_costo_credito(self, costo):
        self._costo_credito = costo

    def calcular_matricula(self):
        self._matricula = self._numero_creditos * self._costo_credito

    def obtener_numero_creditos(self):
        return self._numero_creditos

    def obtener_costo_credito(self):
        return self._costo_credito
