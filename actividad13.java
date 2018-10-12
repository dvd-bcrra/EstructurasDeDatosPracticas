import java.util.Scanner;

public class ColaCircular {
    //ATRIBUTOS
    private String[] cc = new String[5];
    private int root;
    private int front;
    final int INDICE;

    ColaCircular(int root){
        INDICE = root;
        this.root=INDICE;
        this.front=INDICE;
    }

    public void push(String item){
        if((cc[front] == null)){
            cc[front] =  item;
            if(front==4){
                front = 0;
            }else{
                front++;
            }
            peek_all();
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
            peek_all();
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
        else if (cmd.startsWith("pop")){
            pop();
            menu();
        }

        switch (cmd){
            case "exit":
                break;
            case "peek last":
                peek_last();
                menu();
                break;
            case "peek":
                peek();
                menu();
            case "peek all":
                peek();
                menu();
            case "vaciar":
                vaciar();
                menu();
            default:
                imprimir("Comando no identificado");
                menu();
                break;
        }
    }

    //metodo peek
    public void peek(){
        imprimir(Integer.toString(root));
    }

    public void peek_last(){
        imprimir(Integer.toString(front));
    }

    public void peek_all(){
        String salida = "";
        for(int i = 0;i<5;i++){
            if(!(cc[i] == null)){
                salida = salida + " " + cc[i];
            }else{
                salida = salida + " -";
            }
        }
        System.out.println(salida);
    }

    public void imprimir(String salida){
        System.out.println(salida);
    }

    public void vaciar(){
        for(int i = 0;i<5;i++) {
            cc[i] = null;
            root = INDICE;
            front = INDICE;
        }
        peek_all();
    }

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        System.out.print("Ingrese la posicion de inicio (1-5): ");
        int posicion = (scn.nextInt())-1;
        ColaCircular cc = new ColaCircular(posicion);
        cc.menu();
    }
}
