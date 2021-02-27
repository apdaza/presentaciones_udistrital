package tipados.instrumentos;

public class Viola implements Instrumento{

    @Override
    public void afinar() {
        System.out.println("afinando viola");

    }

    @Override
    public void tocar() {
        System.out.println("tocando viola");

    }

    @Override
    public void tocar(String nota) {
        System.out.println("tocando viola en " + nota);

    }
    
}
