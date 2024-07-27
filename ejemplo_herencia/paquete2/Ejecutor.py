from herencia1.estudiante_presencial import EstudiantePresencial

def main():
    # Objeto de tipo Estudiante Presencial
    e1 = EstudiantePresencial()

    e1.establecer_nombres_estudiante("René Rolando")
    e1.establecer_apellido_estudiante("Elizalde Solano")
    e1.establecer_identificacion_estudiante("1104111111")
    e1.establecer_edad_estudiante(38)
    e1.establecer_numero_creditos(30)
    e1.establecer_costo_credito(15)
    e1.calcular_matricula_presencial()

    print(f"Nombres: {e1.obtener_nombres_estudiante()}\n"
          f"Apellidos: {e1.obtener_apellido_estudiante()}\n"
          f"Identificación: {e1.obtener_identificacion_estudiante()}\n"
          f"Edad: {e1.obtener_edad_estudiante()}\n"
          f"Número de crédito: {e1.obtener_numero_creditos()}\n"
          f"Costo Crédito: {e1.obtener_costo_credito():.1f}\n"
          f"Costo matrícula: {e1.obtener_matricula_presencial():.1f}\n")

if __name__ == "__main__":
    main()
