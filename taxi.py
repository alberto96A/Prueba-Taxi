def calcular_tarifa():
    pass

def iniciar_carrera():
    pass

def parar_carrera():
    pass

def finalizar_carrera():
    pass

def main():
    print("Bienvenido al programa de cálculo de tarifa del taxi.")
    print("Instrucciones: ...")  # Explica aquí el funcionamiento del programa
    while True:
        instruccion = input("Ingrese una instrucción: ")
        if instruccion == "empezar":
            iniciar_carrera()
        elif instruccion == "parar":
            parar_carrera()
        elif instruccion == "finalizar":
            precio_total = finalizar_carrera()
            print("El precio total es:", precio_total, "euros.")
        elif instruccion == "salir":
            break
        else:
            print("Instrucción inválida.")


            import time

def calcular_tarifa(taxi_en_movimiento):
    tarifa_por_segundo = 0.02 if not taxi_en_movimiento else 0.05
    tiempo_inicio = time.time()  # Obtiene el tiempo de inicio en segundos
    tiempo_actual = time.time()

    while True:
        tiempo_transcurrido = tiempo_actual - tiempo_inicio
        tarifa_actual = tiempo_transcurrido * tarifa_por_segundo
        print(f'Tarifa actual: {tarifa_actual:.2f} euros')

        # Puedes agregar aquí lógica adicional si necesitas detener el cálculo en ciertas condiciones

        tiempo_actual = time.time()
        time.sleep(1)  # Pausa por 1 segundo antes de la siguiente iteración

# Ejemplo de uso
taxi_movimiento = False  # Cambia esto a True o False según corresponda

calcular_tarifa(taxi_movimiento)

if __name__ == "__main__":
    main()
