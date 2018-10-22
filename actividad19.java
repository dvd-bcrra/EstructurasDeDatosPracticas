import java.util.Scanner;

public class LinkedList {

    class Node{
        String data;
        Node next;
    }

    private Node root;

    LinkedList(){
        root = null;
    }

    private void Ingresar(String item){
        Node nuevo = new Node();
        nuevo.data = item;

        //SI LA LISTA ESTA VACIA...
        if(root == null){
            root = nuevo;
        }else{
            Node pointer = root;
            while (pointer.next != null){
                pointer = pointer.next;
            }
            pointer.next = nuevo;
        }
    }

    private void pop(String item){

        //CASO 1 - DESTRUIR LA RAIZ
        if(root.data == item){
            root = root.next;
        }

        //CASO 2 - DESTRUIR EL DATO PEDIDO
        else{
            Node pointer = root;
            while (pointer != null){
                if(pointer.next.data == item){
                    pointer = pointer.next.next;
                }
                pointer = pointer.next;
            }
        }
    }

    //CASO 3 - DESTRUIR EL ULTIMO NODO
    private void pop(){


    }

    private void peek(String item){
        Node pointer = root;
        boolean found = false;
        while (pointer != null){
            if(pointer.data == item){
                found = true;
            }
            pointer = pointer.next;
        }
        if (found)
            System.out.println("Elemento encontrado");
        else
            System.out.println("Elemento no encontrado");

    }

    private void Imprimir(){
        Node pointer = root;
        String salida = "";
        while (pointer != null){
            salida = salida + pointer.data + " - ";
            pointer = pointer.next;
        }
        System.out.println(salida);
    }

    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        LinkedList ll = new LinkedList();
        ll.Ingresar("uno");
        ll.Ingresar("dos");
        ll.Ingresar("tres");
        ll.Ingresar("cuatro");
        ll.Imprimir();
        ll.Ingresar("cinco");
        ll.Ingresar("seis");
        ll.peek("dos");
        ll.peek("uno");
        ll.peek("cinco");
        ll.Imprimir();
        ll.pop("uno");
        ll.Imprimir();
        ll.pop("cuatro");
        ll.Imprimir();
    }
}
