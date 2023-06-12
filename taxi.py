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

if __name__ == "__main__":
    main()
