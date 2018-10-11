import java.util.Scanner;

public class ColaCircular {
    //ATRIBUTOS
    private String[] cc = new String[5];
    private int root;
    private int front;

    ColaCircular(int root){
        this.root=root;
        this.front=root;
    }

    public void push(String item){
        if((cc[front] == null)){
            cc[front] =  item;
            if(front==4){
                front = 0;
            }else{
                front++;
            }
            imprimir();
        }else{
            System.out.println("Cola llena");
        }
    }

    public void pop(){
        if(!(cc[root] == null)){
            cc[root] =  null;
            if(root==4){
                root = 0;
            }else{
                root++;
            }
            imprimir();
        }else{
            System.out.println("Cola vacia");
        }
    }

    public void menu(){
        Scanner scn = new Scanner(System.in);
        String cmd = scn.nextLine();
        if (cmd.startsWith("push")){
            String item = cmd.substring(5);
            push(item);
            menu();
        }
        if (cmd.startsWith("pop")){
            pop();
            menu();
        }
        if (cmd == "exit"){
            //exit
        }

    }

    public void imprimir(){
        String salida = "";
        for(int i = 0;i<5;i++){
            //if(!(cc[i] == null)){
                salida = salida + " - " + cc[i];
            //}
        }
        System.out.println(salida);
    }

    boolean isNull(){
        boolean vacia = true;
        for(int i = 0;i<5;i++){
            // SI EL ELEMENTO i DEL ARREGLO NO ESTA VACIO
            if(!(cc[i] == null)){
                vacia = false;
            }
        }
        return vacia;
    }

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        System.out.print("Ingrese la posicion de inicio (1-5): ");
        int posicion = (scn.nextInt())-1;
        ColaCircular cc = new ColaCircular(posicion);
        cc.menu();
    }
}
