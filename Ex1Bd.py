class Professor:
    def __init__(self, nome):
        self.nome = nome

class Aluno:
    def __init__(self, nome):
        self.nome = nome

class Aula:

    def __init__(self, Professor, nome_aula):
        self.Professor = Professor
        self.nome = nome_aula
    def adicionar_aluno(self, Aluno):
        self.aluno = Aluno
        lista.append(self.aluno.nome)
    def listar_presenca(self):
        print("Presença na aula sobre",self.nome,", ministrada pelo professor Lucas:")
        for x in range (2):
            print("O aluno", lista[x], "Está presente")

lista = []
professor = Professor("Lucas")
aluno1 = Aluno("Maria")
aluno2 = Aluno("Pedro")
aula = Aula(professor, "Programação Orientada a Objetos")
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)
print(aula.listar_presenca())

