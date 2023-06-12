import time

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
    print("Instrucciones: ...")  # Explica aquí el funcionamiento del programa
    taxi_movimiento = False 

    while True:
        instruccion = input("Ingrese una instrucción: ")

        if instruccion == "empezar":
            taxi_movimiento = True
            calcular_tarifa(taxi_movimiento)
        elif instruccion == "parar":
            taxi_movimiento = False
        elif instruccion == "finalizar":
            # Lógica para finalizar la carrera y devolver el precio total en euros
            pass
        elif instruccion == "salir":
            break
        else:
            print("Instrucción inválida.")

if __name__ == "__main__":
    main()
