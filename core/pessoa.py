class Pessoa():
    def __init__(self, nome="", idade=0):
        self.__nome = nome
        self.__idade = idade

    def dados(self):
        return f"{self.__nome} {self.__idade}"

    @property
    def nome(self):
        return self.__nome 

    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome, str):
            self.__nome = novo_nome
    
    @property
    def idade(self):
        return self.__idade

    @nome.setter
    def nome(self, nova_idade):
         if isinstance(nova_idade, int):
            self.__idade = nova_idade

p1 = Pessoa("Jose", 63)
x = p1.dados()
print(p1.nome)
print(p1.idade)
print(x)