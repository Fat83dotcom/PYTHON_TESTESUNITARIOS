import requests


class Pessoa:
    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.dadosObtidos = False

    def obterDados(self):
        resposta = requests.get('www.loko.com')
        if resposta.ok:
            self.dadosObtidos = True
            return 'Conectado'
        else:
            self.dadosObtidos = False
            return 'Erro 404'
