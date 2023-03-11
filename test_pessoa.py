import unittest
from unittest.mock import patch
from pessoa import Pessoa


class TestePessoa(unittest.TestCase):
    def setUp(self) -> None:
        self.p1 = Pessoa('Fernando', 'Mendes')
        self.p2 = Pessoa('Maria', 'Joaquina')

    def test_attr_nome_tem_valor_correto(self):
        self.assertEqual(self.p1.nome, 'Fernando')
        self.assertEqual(self.p2.nome, 'Maria')

    def test_attr_sobrenome_tem_valor_correto(self):
        self.assertEqual(self.p1.sobrenome, 'Mendes')
        self.assertEqual(self.p2.sobrenome, 'Joaquina')

    def test_attr_nome_str(self):
        self.assertIsInstance(self.p1.nome, str)
        self.assertIsInstance(self.p2.nome, str)

    def test_attr_sobrenome_str(self):
        self.assertIsInstance(self.p1.sobrenome, str)
        self.assertIsInstance(self.p2.sobrenome, str)

    def test_attr_dadosObtidos_inica_False(self):
        self.assertFalse(self.p1.dadosObtidos)
        self.assertFalse(self.p2.dadosObtidos)

    def test_obterdados_sucesso_OK(self):
        with patch('requests.get') as conectar:
            conectar.return_value.ok = True
            self.assertEqual(self.p1.obterDados(), 'Conectado')
            self.assertTrue(self.p1.dadosObtidos)

    def test_obterdados_falha_erro404(self):
        with patch('requests.get') as conectar:
            conectar.return_value.ok = False
            self.assertEqual(self.p1.obterDados(), 'Erro 404')
            self.assertFalse(self.p1.dadosObtidos)

    def test_obterdados_sucesso_e_falha_sequencial(self):
        with patch('requests.get') as conectar:
            conectar.return_value.ok = True
            self.assertEqual(self.p1.obterDados(), 'Conectado')
            self.assertTrue(self.p1.dadosObtidos)

            conectar.return_value.ok = False
            self.assertEqual(self.p1.obterDados(), 'Erro 404')
            self.assertFalse(self.p1.dadosObtidos)


if __name__ == '__main__':
    unittest.main(verbosity=2)
