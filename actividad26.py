#Arboles Binarios

#clase nodo
class Node:

    #contructor
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

#clase arbol binario
class BinaryTree():
    
    #constructor
    def __init__(self):
        self.root = None

    #metodo push
    def push(self,item):
        
        nodo = Node()
        nodo.data = item
        
        #si esta vacia
        if self.root is None:
            self.root = nodo
        else:
            recorrer = True
            subarbol = self.root
            
            while recorrer:

                print("Subraiz: " + subarbol.data)
                
                if subarbol.left is None:
                    #si la rama izquierda esta vacia...
                    print("1) Insertar en la rama izquierda")
                    izquierda = False
                else:
                    #si tiene un valor
                    print("1) Viajar la rama izquierda")
                    izquierda = True

                if subarbol.right is None:
                    #si la rama derecha esta vacia...
                    print("2) Insertar en la rama derecha")
                    derecha = False
                else:
                    #si tiene un valor
                    print("2) Viajar a la rama derecha")
                    derecha = True

                enter = int(input("-> "))

                if enter == 1 and izquierda == False:
                    #push en izquierda
                    subarbol.left = nodo
                    recorrer = False
                elif enter == 1 and izquierda == True:
                    #recorrer en izquierda
                    subarbol = subarbol.left
                elif enter == 2 and derecha == False:
                    #push en derecha
                    subarbol.right = nodo
                    recorrer = False
                else:
                    #recorrer en derecha
                    subarbol = subarbol.right

#programa
bt = BinaryTree()
def menu():
    print("1) Agregar nodo\n2) Irse")
    enter = int(input("-> "))
    if enter == 1:
        item = input("Ingrese el valor: ")
        bt.push(item)
        menu()
    else:
        print("bye")
menu()
