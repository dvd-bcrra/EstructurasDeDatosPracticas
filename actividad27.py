#Arboles Binarios - Recorrido inorden

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
    def ingresar(self,item):
        
        nodo = Node()
        nodo.data = item
        
        #si esta vacia
        if self.root is None:
            self.root = nodo
        else:
            recorrer = True
            subarbol = self.root
            
            while recorrer:

                print("subraiz: " + subarbol.data)
                
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

    def inorden(self,subarbol):
        if subarbol is not None:
            self.inorden(subarbol.left)
            print(subarbol.data, end = " ")
            self.inorden(subarbol.right)
                

#programa
bt = BinaryTree()
def menu():
    print("\n1) Agregar nodo\n2) Inorden\n3) Salir")
    enter = int(input("-> "))
    if enter == 1:
        item = input("Ingrese el valor: ")
        bt.ingresar(item)
        menu()
    elif enter == 2:
        bt.inorden(bt.root)
        menu()
    elif enter == 3:
        print("Fin")
    else:
        print("error")
        menu()
menu()
