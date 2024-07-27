from estudiante_presencial import EstudiantePresencial
from estudiante_distancia import EstudianteDistancia

def main():
    import locale
    import sys
    if sys.version_info[0] == 3:
        input = input

    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    nombres_est = ""
    apellidos_est = ""
    identificacion_est = ""
    edad_est = 0
    costo_cred = 0.0
    numero_creds = 0
    costo_asig = 0.0
    numero_asigs = 0
    tipo_estudiante = 0
    continuar = ""

    while True:
        print("Tipo de Estudiante a ingresar\n"
              + "Ingrese (1) para Estudiante Presencial\n"
              + "Ingrese (2) para Estudiante Distancia")
        tipo_estudiante = int(input())
        input()  # consume newline character

        print("Ingrese los nombres del estudiante")
        nombres_est = input()
        print("Ingrese los apellidos del estudiante")
        apellidos_est = input()
        print("Ingrese la identificación del estudiante")
        identificacion_est = input()
        print("Ingrese la edad del estudiante")
        edad_est = int(input())

        if tipo_estudiante == 1:
            estudianteP = EstudiantePresencial()
            print("Ingrese el número de créditos")
            numero_creds = int(input())
            print("Ingrese el costo de cada crédito")
            costo_cred = float(input())
            estudianteP.establecer_nombres_estudiante(nombres_est)
            estudianteP.establecer_apellido_estudiante(apellidos_est)
            estudianteP.establecer_identificacion_estudiante(identificacion_est)
            estudianteP.establecer_edad_estudiante(edad_est)
            estudianteP.establecer_numero_creditos(numero_creds)
            estudianteP.establecer_costo_credito(costo_cred)
            estudianteP.calcular_matricula()
            print(f"Datos Estudiante Presencial\n"
                  f"Nombres: {estudianteP.obtener_nombres_estudiante()}\n"
                  f"Apellidos: {estudianteP.obtener_apellido_estudiante()}\n"
                  f"Identificación: {estudianteP.obtener_identificacion_estudiante()}\n"
                  f"Edad: {estudianteP.obtener_edad_estudiante()}\n"
                  f"Costo Matricula: {estudianteP.obtener_matricula():.2f}\n")
        elif tipo_estudiante == 2:
            estudianteD = EstudianteDistancia()
            print("Ingrese el número de asignaturas")
            numero_asigs = int(input())
            print("Ingrese el costo de cada asignatura")
            costo_asig = float(input())
            estudianteD.establecer_nombres_estudiante(nombres_est)
            estudianteD.establecer_apellido_estudiante(apellidos_est)
            estudianteD.establecer_identificacion_estudiante(identificacion_est)
            estudianteD.establecer_edad_estudiante(edad_est)
            estudianteD.establecer_numero_asignaturas(numero_asigs)
            estudianteD.establecer_costo_asignatura(costo_asig)
            estudianteD.calcular_matricula()
            print(f"Datos Estudiante Distancia\n"
                  f"Nombres: {estudianteD.obtener_nombres_estudiante()}\n"
                  f"Apellidos: {estudianteD.obtener_apellido_estudiante()}\n"
                  f"Identificación: {estudianteD.obtener_identificacion_estudiante()}\n"
                  f"Edad: {estudianteD.obtener_edad_estudiante()}\n"
                  f"Costo Matricula: {estudianteD.obtener_matricula():.2f}\n")
        else:
            print("Opción fuera de rango")

        print("Desea ingresar más estudiante. Digite la "
              + "letra S para continuar o digite la letra N para salir "
              + "del proceso")
        continuar = input()
        if continuar.upper() != "S":
            break

if __name__ == "__main__":
    main()
