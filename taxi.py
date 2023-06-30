import time
import logging

# Configuración básica del registro de eventos
logging.basicConfig(filename='registro.log', level=logging.INFO)

def calcular_tarifa(taxi_en_movimiento, tiempo_inicio):
    """Calcula la tarifa por segundo dependiendo si el taxi está en movimiento o no."""
    # Calcula la tarifa por segundo dependiendo si el taxi está en movimiento o no
    tarifa_por_segundo = 0.02 if not taxi_en_movimiento else 0.05
    tiempo_actual = time.time()
    tiempo_transcurrido = tiempo_actual - tiempo_inicio
    tarifa_actual = tiempo_transcurrido * tarifa_por_segundo
    print(f'Tarifa actual: {tarifa_actual:.2f} euros')

def guardar_registro(registro):
    """Guarda el registro de la carrera en un archivo de texto."""
    # Abre el archivo "registro.txt" en modo de escritura y agrega el registro al final
    with open('registro.txt', 'a') as file:
        file.write(registro + '\n')

def consultar_registro():
    """Consulta y muestra el registro histórico de carreras desde un archivo de texto."""
    # Abre el archivo "registro.txt" en modo de lectura y muestra su contenido
    with open('registro.txt', 'r') as file:
        registros = file.read()
        print(registros)

def mostrar_instrucciones():
    """Muestra las instrucciones del programa."""
    print("Instrucciones:")
    print("- Para iniciar una carrera, ingrese 'empezar'")
    print("- Para indicar que el taxi está en movimiento, ingrese 'movimiento'")
    print("- Para indicar que el taxi se queda quieto, ingrese 'parado'")
    print("- Para finalizar la carrera y obtener el precio total, ingrese 'finalizar'")
    print("- Para consultar el registro histórico de carreras, ingrese 'registro'")
    print("- Para salir del programa, ingrese 'salir'")

def main():
    # Mensaje de bienvenida
    print("Bienvenido al programa de cálculo de tarifa del taxi.")

    mostrar_instrucciones()

    taxi_en_movimiento = False
    carrera_iniciada = False
    tiempo_inicio = 0
    tarifa_actual = 0

    while True:
        instruccion = input("Ingrese una instrucción: ")

        if instruccion == "empezar":
            if not carrera_iniciada:
                carrera_iniciada = True
                tiempo_inicio = time.time()
                tarifa_actual = 0
                print("Carrera iniciada.")
            else:
                print("La carrera ya ha sido iniciada.")
        elif instruccion == "movimiento":
            if carrera_iniciada:
                taxi_en_movimiento = True
                tarifa_actual = 0.05
                print("El taxi está en movimiento.")
            else:
                print("Por favor, inicie la carrera primero.")
        elif instruccion == "parado":
            if carrera_iniciada:
                taxi_en_movimiento = False
                tarifa_actual = 0.02
                print("El taxi se encuentra parado.")
            else:
                print("Por favor, inicie la carrera primero.")
        elif instruccion == "finalizar":
            if carrera_iniciada:
                tiempo_transcurrido = time.time() - tiempo_inicio
                precio_total = tiempo_transcurrido * tarifa_actual
                print(f"El precio total es: {precio_total:.2f} euros.")
                guardar_registro(f"Duración: {tiempo_transcurrido:.2f} segundos, Precio: {precio_total:.2f} euros")
                carrera_iniciada = False
            else:
                print("Por favor, inicie la carrera primero.")
        elif instruccion == "registro":
            print("Registro histórico de carreras:")
            consultar_registro()
        elif instruccion == "salir":
            print("¡Gracias por utilizar nuestro servicio de cálculo de tarifa!")
            break
        else:
            print("Instrucción inválida. Por favor, intente nuevamente.")

        # Registro de eventos utilizando logging
        logging.debug('depuración')
        logging.info('información')
        logging.warning('advertencia')
        logging.error('error')

if __name__ == "__main__":
    main()
