from database import Database
from teacher_crud import Teacher_crud
from CLi import profCLI

db = Database("bolt://52.90.199.226:7687", "neo4j", "transmitters-slate-root")

teacher = Teacher_crud(db)


#3 b) 
teacher.create("Chris Lima", 1956,'189.052.396-66')

#c)
print(teacher.read("Chris Lima"))

#d)
teacher.update("Chris Lima", "162.052.777-77")
#Mostrando a mudança
print(teacher.read("Chris Lima"))

professor = profCLI(teacher)
professor.run()

