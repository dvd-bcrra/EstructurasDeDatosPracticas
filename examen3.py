#Examen

#Unidad 3

#EXAMEN David Enrique Becerra Ramírez

class Node:
    def __init__ (self): 
        self.data = None
        self.next = None
        self.prev = None

class LinkedList:
    def __init__ (self): 
        self.root = None 
        self.last = None
        
    def insertar(self,item): 
        nodo = Node()
        nodo.data = item
        if self.root is None: 
	    self.root = nodo 
	    self.last = nodo 
	    self.prev = None
	else:
	    pointer = self.root
	    while pointer.next is not None: 
		pointer = pointer.next
	    pointer.next = nodo 
	    pointer.next.prev = pointer 
	    self.last = pointer.next

    def lectura_raiz(self): 
	print(self.root.data)

    def lectura_right(self): 
	pointer = self.root
	while pointer.next is not None: 
	    pointer = pointer.next
	print(pointer.data)

    def lectura_left(self): 
	pointer = self.last
	while pointer.prev is not None: 
	    pointer = pointer.prev
	print(pointer.data)

    def lectura_next(self): 
	peek = ""
	pointer = self.root
	while pointer.next is not None:
	    peek = peek + pointer.data + " - " 
	    pointer = pointer.next
	peek = peek + pointer.data 
	print(peek)

    def lectura_prev(self): 
	peek = ""
	pointer = self.last
	while pointer.prev is not None:
	    peek = peek + pointer.data + " - "
	    pointer = pointer.prev
	peek = peek + pointer.data
	print (peek)

    def remover(self,item):
	if self.root is None:
	    print("Lista vacia") 
	else:
	    _continue = True 
	    pointer = self.root 
	    while _continue:
		#CASO 1 - CUANDO SE ELIMINA LA RAIZ
		if pointer == self.root and pointer.data == item: 
		    del self.root
		    self.root = pointer.next 
		    break
		else:
		    #CASO 2 - CUANDO SE ELIMINA CUALQUIER NODO
		    if pointer.next.next is not None and pointer.next.data == item: 
			r = pointer.next
			pointer.next = r.next 
			del r
			break 
		    else:
			#CASO 3 - CUANDO SE ELIMINA EL ULTIMO NODO
			if pointer.next == self.last and self.last.data == item: 
			    del self.last
			    self.last = None 
			    pointer.next = None 
			    break
			else:
			    pointer = pointer.next

    def busqueda(self,item): 
	pointer = self.root 
	error404 = True
	while pointer.next is not None: 
	    if pointer.data == item:
		print("Elemento " + item + " encontrado") 
		error404 = False
	    pointer = pointer.next 
	if error404:
	    print("Error 404")


#Programa
ll = LinkedList() 
ll.insertar('1')
ll.insertar('2')
ll.insertar('3')
ll.insertar('4')
ll.insertar('5')
ll.insertar('6')
ll.insertar('7')
ll.insertar('8')
ll.insertar('9') 
def menu():
    print("1) Insertar\n"
	  "2) Lectura izq - der\n" 
	  "3) Lectura der - izq\n" 
	  "4) Leer izq\n"
	  "5) Leer der\n"
          "6) Leer Raiz\n"
          "7) Buscar\n"
          "8) Remover\n"
          "9) Salida")
    enter = int(input("-> "))

    #INSERTAR
    if enter == 1:
	item = input("Ingrese el valor: ") 
	ll.insertar(item)
	menu()

    #LECTURA IZQ - DER
    elif enter == 2: 
	ll.lectura_next() 
	menu()

    #LECTURA DER - IZQ
    elif enter == 3: 
	ll.lectura_prev() 
	menu()

    #LEER IZQ
    elif enter == 4: 
	ll.lectura_left 
	menu()

    #LEER DER
    elif enter == 5: 
	ll.lectura_right() 
	menu()

    #LEER RAIZ
    elif enter == 6: 
	ll.lectura_raiz()
	menu()

    #BUSCAR
    elif enter == 7:
	item = input("Ingrese el valor: ") 
	ll.busqueda(item)
	menu()

    #REMOVER
    elif enter == 8:
	item = input("Ingrese el valor: ") 
	ll.remover(item)
	menu()

    #SALIR
    elif enter == 9:
	print("exit...")
    else:
	print("error") 
	menu()
menu()


##Output
##1) Insertar
##2) Lectura izq - der
##3) Lectura der - izq
##4) Leer izq
##5) Leer der
##6) Leer Raiz
##7) Buscar
##8) Remover
##9) Salida
##-> 2
##1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9
##1) Insertar
##2) Lectura izq - der
##3) Lectura der - izq
##4) Leer izq
##5) Leer der
##6) Leer Raiz
##7) Buscar
##8) Remover
##9) Salida
##-> 3
##9 - 8 - 7 - 6 - 5 - 4 - 3 - 2 - 1

##1) Insertar
##2) Lectura izq - der
##3) Lectura der - izq
##4) Leer izq
##5) Leer der
##6) Leer Raiz
##7) Buscar
##8) Remover
##9) Salida
##-> 1
##Ingrese el valor: 10
##1) Insertar
##2) Lectura izq - der
##3) Lectura der - izq
##4) Leer izq
##5) Leer der
##6) Leer Raiz
##7) Buscar
##8) Remover
##9) Salida
##-> 1
##Ingrese el valor: 11
##1) Insertar
##2) Lectura izq - der
##3) Lectura der - izq
##4) Leer izq
##5) Leer der
##6) Leer Raiz
##7) Buscar
##8) Remover
##9) Salida
##-> 1
##Ingrese el valor: 13
##1) Insertar
##2) Lectura izq - der
##3) Lectura der - izq
##4) Leer izq
##5) Leer der
##6) Leer Raiz
##7) Buscar
##8) Remover
##9) Salida
##-> 8
##Ingrese el valor: 8
##1) Insertar
##2) Lectura izq - der
##3) Lectura der - izq
##4) Leer izq
##5) Leer der
##6) Leer Raiz
##7) Buscar
##8) Remover
##9) Salida
##-> 8
##Ingrese el valor: 1
##1) Insertar
##2) Lectura izq - der
##3) Lectura der - izq
##4) Leer izq
##5) Leer der
##6) Leer Raiz
##7) Buscar
##8) Remover
##9) Salida
##-> 6
##2
##1) Insertar
##2) Lectura izq - der
##3) Lectura der - izq
##4) Leer izq
##5) Leer der
##6) Leer Raiz
##7) Buscar
##8) Remover
##9) Salida
##-> 5
##13
##1) Insertar
##2) Lectura izq - der
##3) Lectura der - izq
##4) Leer izq
##5) Leer der
##6) Leer Raiz
##7) Buscar
##8) Remover
##9) Salida
##-> 6
##2
##1) Insertar
##2) Lectura izq - der
##3) Lectura der - izq
##4) Leer izq
##5) Leer der
##6) Leer Raiz
##7) Buscar
##8) Remover
##9) Salida
##-> 7
##Ingrese el valor: 0
##Error 404
##1) Insertar
##2) Lectura izq - der
##3) Lectura der - izq
##4) Leer izq
##5) Leer der
##6) Leer Raiz
##7) Buscar
##8) Remover
##9) Salida
##-> 7
##Ingrese el valor: 7
##Elemento 7 encontrado
##1) Insertar
##2) Lectura izq - der
##3) Lectura der - izq
##4) Leer izq
##5) Leer der
##6) Leer Raiz
##7) Buscar
##8) Remover
##9) Salida
##-> 7
##Ingrese el valor: 8
##Error 404
##1) Insertar
##2) Lectura izq - der
##3) Lectura der - izq
##4) Leer izq
##5) Leer der
##6) Leer Raiz
##7) Buscar
##8) Remover
##9) Salida
##-> 7
##Ingrese el valor: 1
##Error 404
##1) Insertar
##2) Lectura izq - der
##3) Lectura der - izq
##4) Leer izq
##5) Leer der
##6) Leer Raiz
##7) Buscar
##8) Remover
##9) Salida
##->
