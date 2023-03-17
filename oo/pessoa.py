class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=32):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def comprimentar(self):
        return f'Olá id {id(self)} e o nome {self.nome}'


    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributo_de_classes(cls):
        return f'olhos {cls} e {cls.olhos}'


class Homem(Pessoa):
    def comprimentar(self):
        comprimentar_da_class = super().comprimentar() #super e o metudo utilizado para o python buscar da class pai
        return f'Apertar a mão somente class homem - {comprimentar_da_class}'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    rogerio = Homem(nome='Rogerio')
    dorival = Homem(rogerio, nome='dorival')
    joaquim = Mutante(nome='Joaquim')
    print(Homem.comprimentar(dorival))
    print(id(dorival))
    print(dorival.nome)
    print(dorival.idade)
    print(dorival.olhos)
    dorival.olhos = 1
    print(dorival.olhos)
    for filho in dorival.filhos:
        print(filho.nome)
    del dorival.filhos
    dorival.sobrenome = 'ponsoni'
    print(rogerio.__dict__)
    print(dorival.__dict__)
    print(id(Homem.olhos), id(dorival.olhos), id(rogerio.olhos))
    print(Pessoa.metodo_estatico(), dorival.metodo_estatico())
    print(Pessoa.nome_e_atributo_de_classes(), dorival.nome_e_atributo_de_classes())
    pessoa = Pessoa("Antonio")
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(rogerio, Pessoa))
    print(isinstance(rogerio, Homem))
    print(f'{joaquim.olhos} quantidade de olhos pega direto da classe Multante se não informado seria da class pai que e pessoas')
    print(f'Rogerio class homem : {rogerio.comprimentar()}')
    print(f'josquim class mutante {joaquim.comprimentar()}')