'''
1 - Receber um núemro inteiro

2 - Saber se o úmero é multiplo de 3 e 5
retorna: Bacon com ovos

3 - Saber se o número é multiplo somente de 3
retorna: Bacon

4 - Saber se o npumero é multiplo somente de 5
retorna: Ovos

5 - Saber se o número não é multiplo de 3 e 5
retona : Passa fome
'''


def baconComOvos(n):
    try:
        assert isinstance(n, int), "n deve ser 'int'"
        if n % 3 == 0 and n % 5 == 0:
            return "Bacon Com Ovos"
        if n % 3 == 0:
            return "Bacon"
        if n % 5 == 0:
            return "Ovos"
        return "Passar fome"
    except AssertionError as e:
        raise e
