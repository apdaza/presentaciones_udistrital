package tipados.instrumentos;

public class Cuatro implements Instrumento{

    @Override
    public void afinar() {
        Afinador a = new Afinador();
        a.generarTono();
        System.out.println("afinando cuatro");

    }

    @Override
    public void tocar() {
        System.out.println("tocando cuatro");

    }

    @Override
    public void tocar(String nota) {
        System.out.println("tocando cuatro en " + nota);

    }
    
}
