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
            Node reco = root;
            while (reco.next != null){
                reco = reco.next;
            }
            reco.next = nuevo;
        }
    }

    /*
    private void Imprimir(){
        Node reco = root;
        while (reco != null){
            System.out.println(reco.data);
            reco = reco.next;
        }
    }
    */
    
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        LinkedList ll = new LinkedList();
        ll.Ingresar("uno");
        ll.Ingresar("dos");
        ll.Ingresar("tres");
        ll.Ingresar("cuatro");
        //ll.Imprimir();
    }
}
