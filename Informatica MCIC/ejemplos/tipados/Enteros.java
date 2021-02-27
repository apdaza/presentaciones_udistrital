package tipados;

import java.util.Scanner;

public class Enteros {
    public static void main(String[] args) {
        int valor = -1;
        Scanner sc = new Scanner(System.in);
        String[] dias = {"Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"};

        while(valor<0 || valor>6){
            System.out.print("Ingrese un entero: ");
            valor = sc.nextInt();
        }
        sc.close();
        

        


        System.out.println(dias[valor]);
        /*
        for(int i = 0; i < valor; i++){
            System.out.println(i);
        }
        

        switch(valor){
            case 1:
                System.out.println("Domingo");
                break;
            case 2:
                System.out.println("Lunes");
                break;
            case 3:
                System.out.println("Martes");
                break;
            case 4:
                System.out.println("Miercoles");
                break;
            default:
                System.out.println("No valido");
        }
        */
    }
    
}
