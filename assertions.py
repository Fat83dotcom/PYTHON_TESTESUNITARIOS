def soma(x, y):
    '''
    Soma dois números

    >>> soma(10, 10)
    20

    '''
    try:
        assert isinstance(x, (int, float)), "x precisa ser int ou float"
        assert isinstance(y, (int, float)), "y precisa ser int ou float"
        return x + y
    except AssertionError as e:
        raise e

def subtracao(x, y):
    '''
    Subtrai 2 números

    >>> subtracao(20, 10)
    10
    '''
    try:
        assert isinstance(x, (int, float)), "x precisa ser int ou float"
        assert isinstance(y, (int, float)), "y precisa ser int ou float"
        return x - y
    except AssertionError as e:
        raise e


# try:
#     print(soma(23, 452))
#     print(soma('34', 12))
# except Exception as e:
#     print(e)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
