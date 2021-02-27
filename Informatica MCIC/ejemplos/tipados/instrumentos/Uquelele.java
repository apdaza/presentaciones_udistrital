package tipados.instrumentos;

public class Uquelele implements Instrumento{

    @Override
    public void afinar() {
        Afinador a = new Afinador();
        a.generarTono();
        System.out.println("afinando uquelele");

    }

    @Override
    public void tocar() {
        System.out.println("tocando uquelele");
    }

    @Override
    public void tocar(String nota) {
        System.out.println("tocando uquelele en " + nota);

    }
    
}
