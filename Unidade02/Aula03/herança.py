class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def fazer_barulho(self):
        pass

class Cachorro(Animal):
    def fazer_barulho(self):
        return 'Latir'
    
class Gato(Animal):
    def fazer_barulho(self):
        return 'Miar'
    
#criando ojetos de classes-filhas

rex = Cachorro('Rex')
afonsinho = Gato('Afonsinho')

#chamando método

print(f'{rex.nome} faz: {rex.fazer_barulho()}')
print(f'{afonsinho.nome} faz: {afonsinho.fazer_barulho()}')