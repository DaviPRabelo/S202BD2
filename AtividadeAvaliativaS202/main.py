from database import Database
from MotoristaDAO import PersonModel
from MotoristaCLI import motoritCLI
db = Database(database="teste", collection="teste")
pm = PersonModel(database=db)


personCLI = motoritCLI(pm)
personCLI.run()