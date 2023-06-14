import time
import logging

logging.basicConfig(filename='registro.log', level=logging.INFO)

def calcular_tarifa(taxi_en_movimiento):
    tarifa_por_segundo = 0.02 if not taxi_en_movimiento else 0.05
    tiempo_inicio = time.time()
    tiempo_actual = time.time()

    while True:
        tiempo_transcurrido = tiempo_actual - tiempo_inicio
        tarifa_actual = tiempo_transcurrido * tarifa_por_segundo
        print(f'Tarifa actual: {tarifa_actual:.2f} euros')

        tiempo_actual = time.time()
        time.sleep(1)

def main():
    print("Bienvenido al programa de cálculo de tarifa del taxi.")
    print("Instrucciones:")
    print("- Para iniciar una carrera, ingrese 'empezar'")
    print("- Para indicar que el taxi está en movimiento, ingrese 'movimiento'")
    print("- Para indicar que el taxi se queda quieto, ingrese 'parado'")
    print("- Para finalizar la carrera y obtener el precio total, ingrese 'finalizar'")
    print("- Para salir del programa, ingrese 'salir'")

    taxi_en_movimiento = False
    carrera_iniciada = False
    tiempo_inicio = 0

    while True:
        instruccion = input("Ingrese una instrucción: ")
        logging.debug('depuración')
        logging.info('información')
        logging.warning('advertencia')
        logging.error('error')
        if instruccion == "empezar":
            if not carrera_iniciada:
                carrera_iniciada = True
                tiempo_inicio = time.time()
                print("Carrera iniciada.")
            else:
                print("La carrera ya ha sido iniciada.")
        elif instruccion == "movimiento":
            if carrera_iniciada:
                taxi_en_movimiento = True
                print("El taxi está en movimiento.")
            else:
                print("Por favor, inicie la carrera primero.")
        elif instruccion == "parado":
            if carrera_iniciada:
                taxi_en_movimiento = False
                print("El taxi se encuentra parado.")
            else:
                print("Por favor, inicie la carrera primero.")
        elif instruccion == "finalizar":
            if carrera_iniciada:
                tiempo_transcurrido = time.time() - tiempo_inicio
                precio_total = tiempo_transcurrido * 0.05
                print(f"El precio total es: {precio_total:.2f} euros.")
                carrera_iniciada = False
            else:
                print("Por favor, inicie la carrera primero.")
        elif instruccion == "salir":
            print("¡Gracias por utilizar nuestro servicio de cálculo de tarifa!")
            break
        else:
            print("Instrucción inválida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    main()
