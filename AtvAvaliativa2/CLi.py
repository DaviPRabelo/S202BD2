class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")

#e)
class profCLI(SimpleCLI):
    def __init__(self, teacher):
        super().__init__()
        self.teacher = teacher
        self.add_command("create", self.create_professor)
        self.add_command("read", self.read_professor)
        self.add_command("update cpf", self.update_cpf_prof)
        self.add_command("delete", self.delete_professor)

    def create_professor(self):
        nome = input("Coloque o nome do professor: ")
        ano_nasc = int(input("Coloque o ano de nascimento: "))
        cpf = input("Qual a nota do motorista: ")
        self.teacher.create(nome, ano_nasc, cpf)

    def read_professor(self):
        nome = input("Coloque o nome do professor ")
        a = self.teacher.read(nome)
        print(a)

    def update_cpf_prof(self):
        nome = input("Coloque o nome do professor que quer alterar: ")
        cpf = input("Coloque o novo cpf do professor: ")
        self.teacher.update(nome, cpf)

    def delete_professor(self):
        nome = input("Coloque o nome do professor que quer deletar: ")
        self.teacher.delete(nome)
        
    def run(self):
        print("Welcome to the Motorista CLI!")
        print("Available commands: create, read, update cpf, delete, quit")
        super().run()
    








    