class Teacher_crud:
    def __init__(self, database):
        self.db = database

    def create(self, name:str, ano_nasc:int, cpf:str):
        query = """CREATE (t:Teacher{name:"""f"'{name}',""ano_nasc:"f"{ano_nasc}"",cpf:"f"'{cpf}'""""})"""
        self.db.execute_query(query)
        print("Professor Adicionado")

    def read(self,name:str):
        query = "MATCH (t:Teacher) WHERE t.name ="f"'{name}'"" RETURN t.name as Nome, t.ano_nasc as AnoNascimento, t.cpf as CPF"
        result = self.db.execute_query(query)
        return result
    
    def delete(self,name:str):
        query = "MATCH(t:Teacher{name:"f"'{name}'""}) DETACH DELETE t"
        self.db.execute_query(query)
        print("Professor deletado.")

    def update(self,name:str,cpf:str):
        query = "MATCH (t:Teacher{name:"f"'{name}'""}) SET t.cpf = "f"'{cpf}' RETURN t"
        self.db.execute_query(query)
        print("CPF alterado com sucesso")