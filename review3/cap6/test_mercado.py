import unittest
from mercado import Caixa

class TestCaixa(unittest.TestCase):
    def test_caixa_nao_possui_compra_antes_de_processar(self):
        caixa = Caixa(0)
        self.assertFalse(hasattr(caixa, 'compra'))

    def test_caixa_possui_compra_apos_processar(self):
        caixa = Caixa(1)
        self.assertFalse(hasattr(caixa, 'compra'))
        caixa.processar_carrinho([])
        self.assertTrue(hasattr(caixa, 'compra'))


if __name__ == '__main__':
    unittest.main()
