from tienda import *

t= Tienda()
t.agregar_animal(Perro("boxer",2,5))
t.agregar_animal(Perro("pitbull",2,10))
t.agregar_animal(Gato("angora",2,0.5))
t.agregar_animal(Gato("persa",2,0.7))
t.agregar_animal(Gato("criollo",12,3.5))
t.agregar_animal(Pez("golden",0.5,0.6))
t.agregar_animal(Pez("telescopio",0.4,0.25))
t.agregar_animal(Pez("golden",1,1))
t.agregar_animal(Ave("loro",1,0.5))
t.agregar_animal(Ave("perico",1,0.5))
t.agregar_animal(Ave("cacatua",1,0.5))

for i in range(5):
    a = t.entregar_animal()
    print(a.saludar(), a.mostrar_informacion())
