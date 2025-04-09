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


class motoritCLI(SimpleCLI):
    def __init__(self, person_model):
        super().__init__()
        self.person_model = person_model
        self.add_command("create", self.create_motorist)
        self.add_command("read", self.read_motorist)
        self.add_command("update name", self.update_name_motorist)
        self.add_command("update corrida", self.update_corrida)
        self.add_command("update age", self.update_age_motorist)
        self.add_command("delete", self.delete_motorist)

    def create_motorist(self):
        passa = input("Coloque o nome do passageiro: ")
        doc = input("Insira o documento deste passageiro: ")
        passageiro = {'Nome': passa, "Documento":doc}
        n = int(input("Quantas corridas deseja colocar: "))
        corridas=[]
        for i in range (n):
            nota = int(input("Qual a nota da corrida: "))
            dist =float(input("Qual a distancia (em km) da corrida: "))
            valor = float(input("Qual o valor da corrida: "))
            corrida={"Nota":nota, "Distância":dist,"Valor":valor, "Passageiro":passageiro}
            corridas.append(corrida)

        name = input("Nome do Motorista: ")
        age = int(input("Idade do Motorista: "))
        note = int(input("Qual a nota do motorista: "))
        self.person_model.create_motorist(name, age, note, corridas)

    def read_motorist(self):
        id = input("Coloque o id do motorista ")
        self.person_model.read_motorist(id)

    def update_corrida(self):
        passa = input("Coloque o nome do passageiro: ")
        doc = input("Insira o documento deste passageiro: ")
        passageiro = {'Nome': passa, "Documento":doc}
        n = int(input("Quantas corridas deseja colocar: "))
        corridas=[]
        for i in range (n):
            nota = int(input("Qual a nota da corrida: "))
            dist =float(input("Qual a distancia (em km) da corrida: "))
            valor = float(input("Qual o valor da corrida: "))
            corrida={"Nota":nota, "Distância":dist,"Valor":valor, "Passageiro":passageiro}
            corridas.append(corrida)

        id = input("Coloque o Id do motorista: ")
        self.person_model.update_corrida(id,corridas)



    def update_name_motorist(self):
        id = input("Coloque o Id do motorista: ")
        name = input("Coloque o novo nome do motorista: ")
        self.person_model.update_name_motorist(id, name)
    
    def update_age_motorist(self):
        id = input("Coloque o Id do motorista: ")
        age = int(input("Coloque a nova idade do motorista "))
        self.person_model.update_age_motorist(id, age)

    def delete_motorist(self):
        id = input("Enter the id: ")
        self.person_model.delete_motorist(id)
        
    def run(self):
        print("Welcome to the Motorista CLI!")
        print("Available commands: create, read, update name, update corrida, update age, delete, quit")
        super().run()
        