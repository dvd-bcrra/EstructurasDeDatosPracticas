#Listas Enlazadas

class Node:
    def __init__(self):
        self.data = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.root = None
        self.q = None

    def push(self,item):
        nodo = Node()
        nodo.data = item
        if self.root is None:
            self.root = nodo
            self.q = nodo
        else:
            pointer = self.root
            while pointer.next is not None:
                pointer = pointer.next
            pointer.next = nodo
            self.q = pointer.next

    def peek(self):
        pointer = self.root
        while pointer.next is not None:
            print (pointer.data)
            pointer = pointer.next
        print (pointer.data)

    def pop(self,item):
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
                        if pointer.next == self.q and self.q.data == item:
                            del self.q
                            self.q = None
                            pointer.next = None
                            break
                        else:
                            pointer = pointer.next

                    
#Programa
ll = LinkedList()
def menu():
    print("1) Push\n2) Peek\n3) Pop\n4) Exit")
    enter = int(input("-> "))
    if enter == 1:
        item = input("Ingrese el valor: ")
        ll.push(item)
        menu()
    elif enter == 2:
        ll.peek()
        menu()
    elif enter == 3:
        item = input("Ingrese el valor: ")
        ll.pop(item)
        menu()
    else:
        print("exit...")
menu()
