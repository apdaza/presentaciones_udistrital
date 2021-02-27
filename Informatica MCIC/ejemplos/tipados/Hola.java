package tipados;
import java.util.Scanner;

public class Hola{
    public static void main(String[] args){
        String nombre = "";
        Scanner sc = new Scanner(System.in);

        System.out.print("Ingrese su nombre: ");
        nombre = sc.next();

        System.out.println("Hola " + nombre);
        sc.close();
    }
}