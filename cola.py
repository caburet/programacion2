# Inicializar una cola vacía como una lista
cola = []
# Función para agregar un elemento a la cola (encolar)
def encolar(elemento):
    cola.append(elemento)
# Función para eliminar y retornar el elemento más antiguo de la cola 
def desencolar():
    if not is_empty():
        return cola.pop(0)
    else:
        return "La cola está vacía"
# Función para verificar si la cola está vacía
def is_empty():
    return len(cola) == 0
# Función para obtener el tamaño de la cola
def size():
    return len(cola)

encolar("Tarea 1")
encolar("Tarea 2")
encolar("Tarea 3")

print("Tamaño de la cola:", size())

print("Elementos de la cola (desde la cima hacia abajo):")
while not is_empty():
    print(desencolar())

print("Tamaño de la cola después de hacer pop:", size())