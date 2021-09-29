class Buah:
    def intro(self):
        print("Memakan buah-buahan sangat baik untuk kesehatan tubuh")
    
    def CaraMakan_buah(self):
        print("Cara memakan buah-buahan ada yang harus di kupas,  dan ada yang bisa langsung dimakan ")

class Strawberry(Buah):
    def CaraMakan_buah(self):
        print("Buah strawberry bisa langsung di makan")

class Mangga(Buah):
    def CaraMakan_buah(self):
        print("Cara makan buah mangga harus di kupas terlebih dahulu ")

obj_Buah = Buah()
obj_Mangga = Mangga()
obj_Strawberry = Strawberry()

obj_Strawberry.intro()
obj_Strawberry.CaraMakan_buah()

print("\n")

obj_Mangga.intro()
obj_Mangga.CaraMakan_buah()
