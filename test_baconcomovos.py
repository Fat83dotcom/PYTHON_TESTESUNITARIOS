'''
TDD - Test Driven Development (Desenvolvimento Dirigido a Testes)

Red
Parte 1 -> Criar o teste e ve-lo falhar

Green
Parte 2 -> Criar o código e ver o teste passar

Refactor
Parte 3 -> Melhorar o código
'''

import unittest
from baconcomovos import baconComOvos


class TestBaconOvos(unittest.TestCase):
    def test_bacon_com_ovos_retorna_assertionErros_se_n_nao_for_int(self):
        with self.assertRaises(AssertionError):
            baconComOvos('42')

    def test_bancon_com_ovos_return_baconcomovos_entrada_for_mult_5_3(self):
        saida = "Bacon Com Ovos"
        n_saida = (15, 30, 60, 90, 120)
        for n_s in n_saida:
            with self.subTest(n_saida=n_saida):
                self.assertEqual(
                    baconComOvos(n_s),
                    saida,
                    msg=f'{n_s} não retornou {saida}'
                )

    def test_bancon_com_ovos_return_passarfome_entrada_nao_for_mult_5_3(self):
        saida = "Passar fome"
        n_saida = (2, 4, 7, 8, 11, 14)
        for n_s in n_saida:
            with self.subTest(n_saida=n_saida):
                self.assertEqual(
                    baconComOvos(n_s),
                    saida,
                    msg=f'{n_s} não retornou {saida}'
                )

    def test_bancon_com_ovos_return_bacon_entrada_nao_for_mult_3(self):
        saida = "Bacon"
        n_saida = (3, 6, 9, 18, 21, 24)
        for n_s in n_saida:
            with self.subTest(n_saida=n_saida):
                self.assertEqual(
                    baconComOvos(n_s),
                    saida,
                    msg=f'{n_s} não retornou {saida}'
                )

    def test_bancon_com_ovos_return_ovos_entrada_nao_for_mult_5(self):
        saida = "Ovos"
        n_saida = (5, 10, 20, 25, 35)
        for n_s in n_saida:
            with self.subTest(n_saida=n_saida):
                self.assertEqual(
                    baconComOvos(n_s),
                    saida,
                    msg=f'{n_s} não retornou {saida}'
                )


if __name__ == '__main__':
    unittest.main(verbosity=2)
