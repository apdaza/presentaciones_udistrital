package tipados;

public class Rutinas {
    
    public static void main(String[] args) {
        Valor v = new Valor();
        incremento(v);
        System.out.println(v.valor);
    }

    public static void incremento(Valor x){
        x.valor++;
    }

}

class Valor{
    public int valor = 5;
}

