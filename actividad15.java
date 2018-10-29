import java.util.Scanner;

class DoubleQueue {
    //ATRIBUTOS
    private String[] cc = new String[10];
    private int root;
    private int front;

    DoubleQueue(){
        this.root=0;
        this.front=9;
    }

    //metodo push por izquierda
    public void push_left(String item){
        if((cc[front] == null)) {
            cc[front] = item;
            front--;
            peek_all();
        } else{
            imprimir("Cola llena");
        }
    }

    //metodo push por derecha
    public void push_right(String item){
        if((cc[root] == null)) {
            cc[root] = item;
            root++;
            peek_all();
        }else{
            imprimir("Cola llena");
        }
    }

    //metodo pop
    public void pop(){
        if(!(cc[root] == null)){
            cc[root] =  null;
            if(root==9){
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
        if (cmd.startsWith("left ")){
            String item = cmd.substring(5);
            push_left(item);
            menu();
        } else if (cmd.startsWith("right ")){
            String item = cmd.substring(5);
            push_right(item);
            menu();
        } else if (cmd.startsWith("pop")){
            pop();
            menu();
        }
        else{
            switch (cmd){
                case "exit":
                    imprimir("ya me boi");
                    break;
                case "peek last":
                    peek_last();
                    menu();
                    break;
                case "peek":
                    peek();
                    menu();
                case "peek all":
                    peek_all();
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

    }

    //metodo peek
    public void peek(){
        imprimir(cc[root]);
    }

    public void peek_last(){
        imprimir(cc[front]);
    }

    public void peek_all(){
        String salida = "";
        for(int i = 0;i<10;i++){
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
            root = 0;
            front = 9;
        }
        peek_all();
    }

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        DoubleQueue cc = new DoubleQueue();
        cc.menu();
    }
}
