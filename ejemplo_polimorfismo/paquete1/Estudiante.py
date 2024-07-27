from abc import ABC, abstractmethod

class Estudiante(ABC):
    def __init__(self):
        self._nombres_estudiante = ""
        self._apellidos_estudiante = ""
        self._identificacion_estudiante = ""
        self._edad_estudiante = 0
        self._matricula = 0.0

    def establecer_nombres_estudiante(self, nombre):
        self._nombres_estudiante = nombre

    def establecer_apellido_estudiante(self, apellido):
        self._apellidos_estudiante = apellido

    def establecer_identificacion_estudiante(self, identificacion):
        self._identificacion_estudiante = identificacion

    def establecer_edad_estudiante(self, edad):
        self._edad_estudiante = edad

    @abstractmethod
    def calcular_matricula(self):
        pass

    def obtener_nombres_estudiante(self):
        return self._nombres_estudiante

    def obtener_apellido_estudiante(self):
        return self._apellidos_estudiante

    def obtener_identificacion_estudiante(self):
        return self._identificacion_estudiante

    def obtener_edad_estudiante(self):
        return self._edad_estudiante

    def obtener_matricula(self):
        return self._matricula
