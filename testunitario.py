import unittest
from io import StringIO
from contextlib import redirect_stdout
from taxi import calcular_tarifa
import time

class TestCalcularTarifa(unittest.TestCase):
    def test_calcular_tarifa(self):
        taxi_en_movimiento = False
        tiempo_inicio = time.time() - 10  # Utilizar un tiempo de inicio válido (10 segundos atrás)

        # Capturar la salida de la función calcular_tarifa
        with StringIO() as output:
            with redirect_stdout(output):
                calcular_tarifa(taxi_en_movimiento, tiempo_inicio)
                output_str = output.getvalue().strip()

        # Verificar si la salida es correcta
        self.assertEqual(output_str, "Tarifa actual: 0.20 euros")

if __name__ == '__main__':
    unittest.main()
