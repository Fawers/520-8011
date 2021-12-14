import unittest
from unittest import result

def soma(a, b):
    return a + b

class TestSoma(unittest.TestCase):
    def test_soma_dois_positivos(self):
        resultado = soma(2, 3)
        esperado = 5
        self.assertEqual(esperado, resultado)
        self.assertEqual(resultado, esperado)

    @unittest.skip('igual ao de cima')
    def test_soma_pos_neg(self):
        resultado = soma(10, -2)
        esperado = 8
        self.assertEqual(esperado, resultado)

    def test_soma_varios(self):
        # [((entradas), esperado)]
        dados = [
            ((2, 3), 5),
            ((3, 7), 10),
            ((-5, 5), 0)
        ]

        for ((a, b), esperado) in dados:
            with self.subTest(a=a, b=b, esperado=esperado):
                self.assertEqual(esperado, soma(a, b))

if __name__ == '__main__':
    unittest.main()
