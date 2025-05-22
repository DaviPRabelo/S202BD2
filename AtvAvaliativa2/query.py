from database import Database

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://52.90.199.226:7687", "neo4j", "transmitters-slate-root")

def questao1A(self, name:str):
        query = """MATCH (t:Teacher{name:"""f"'{name}'""""}) RETURN t.ano_nasc as Ano, t.cpf as CPF"""
        results = self.execute_query(query)
        return results

def questao1B(self):
        query = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name as Nome, t.cpf as CPF"
        results = self.execute_query(query)
        return results

def questao1C(self):
        query = "MATCH (c:City) RETURN c.name AS Nome"
        results = self.execute_query(query)
        return results

def questao1D(self):
        query = "MATCH (s:School) WHERE s.number>=150 AND s.number <=550 RETURN s.name as Nome, s.address as Endereco, s.number as Numero"
        results = self.execute_query(query)
        return results

def questao2A(self):
        query = """MATCH (t:Teacher) RETURN MIN(t.ano_nasc) as MaisVelho, MAX(t.ano_nasc) as MaisNovo"""
        results = self.execute_query(query)
        return results

def questao2B(self):
        query = """MATCH (c:City) RETURN AVG(c.population) as Media"""
        results = self.execute_query(query)
        return results

def questao2C(self):
        query = "MATCH (c:City) WHERE c.cep = '37540-000' RETURN REPLACE(c.name, 'a', 'A') as NomeAlterado"
        results = self.execute_query(query)
        return results

def questao2D(self):
        query = "MATCH (t:Teacher) RETURN SUBSTRING(t.name, 2) as Nomes3Caracter"
        results = self.execute_query(query)
        return results

#1 a)
q1 = questao1A(db,"Renzo")
print(q1)
#b)
print(questao1B(db))
#c)
print(questao1C(db))
#d)
print(questao1D(db))

#2  a)
print(questao2A(db))
#b)
print(questao2B(db))
#c)
print(questao2C(db))
#d)
print(questao2D(db))