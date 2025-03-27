from database import Database
from PersonalModel import PersonModel
db = Database(database="Aula5Lab", collection="Livros")
pm = PersonModel(database=db)

pm.create_book("Diário de um banana","Jeff Kinney", 2000, 45)
pm.create_book("Democracia Palmeirense","Ricardo Gozzi e Dr Sócrates", 2002, 60)
pm.update_book_titulo('67e5b613dcf5662035a62f6c',"Democracia Corinthiana")
#pm.update_book_ano("67e5b613dcf5662035a62f6b",2007)
#pm.delete_book('67e5b613dcf5662035a62f6b')