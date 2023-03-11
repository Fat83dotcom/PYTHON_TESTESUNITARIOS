import unittest
from assertions import soma, subtracao


class TesteFuncoes(unittest.TestCase):
    def test_soma_5_e_5_retorna_10(self):
        self.assertEqual(soma(5, 5), 10)

    def test_subtracao_10_E_10_retorna_0(self):
        self.assertEqual(subtracao(10, 10), 0)

    def test_varias_entradas_soma(self):
        x_y_saida = (
            (-1, -1, -2),
            (1.89, 1.11, 3.0),
            (4, 4, 8),
            (-10, -20, -30),
            (1, 1, 2),
        )

        for x_y_s in x_y_saida:
            with self.subTest(x_y_s=x_y_s):
                x, y, saida = x_y_s
                self.assertEqual(soma(x, y), saida)

    def test_varias_entradas_subtracao(self):
        x_y_saida = (
            (2, 3, -1),
            (10, 10, 0),
            (-3, -7, 4),
            (0, 0, 0),
            (1, 2, -1),
        )

        for x_y_s in x_y_saida:
            with self.subTest(x_y_s=x_y_s):
                x, y, saida = x_y_s
                self.assertEqual(subtracao(x, y), saida)


unittest.main(verbosity=2)
