package tipados.instrumentos;

public class Guitarra implements Instrumento{

    @Override
    public void afinar() {
        Afinador a = new Afinador();
        a.generarTono();
        System.out.println("afinando guitarra");

    }

    @Override
    public void tocar() {
        System.out.println("tocando guitarra");

    }

    @Override
    public void tocar(String nota) {
        System.out.println("tocando guitarra en " + nota);

    }
}
