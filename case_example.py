class AlgumaCoisa:
    def __enter__(self):
        print('Entrando no bloco with')

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('Saindo do bloco with')

with AlgumaCoisa() as something:
    print('Dentro do bloco with')
