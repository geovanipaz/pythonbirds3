class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - {cls.olhos}'
class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe} aperto de mão'


class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':

    renzo = Mutante(nome='Renzo')
    luciano = Homem(renzo,nome='Luciano')

    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)

    luciano.sobrenome = 'Ramalho'
    print(luciano.sobrenome)
    del luciano.filhos
    print(luciano.__dict__)
    print(renzo.__dict__)
    luciano.olhos = 1
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(Pessoa.olhos)
    print(id(Pessoa.olhos),id(luciano.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(renzo.olhos)
    print(luciano.cumprimentar())
    print(renzo.cumprimentar())