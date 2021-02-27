package tipados.instrumentos;

import java.util.Random;

public class Banda {
    private Instrumento[] instrumentos = new Instrumento[3];

    public Banda(){
        for(int i = 0; i < 3; i++)
            instrumentos[i] = generarInstrumento();
    }

    public void presentar(){
        for(int i = 0; i < 3; i++){
            instrumentos[i].afinar();
            instrumentos[i].tocar();
            instrumentos[i].tocar("Do");
        }
    }

    private static Instrumento generarInstrumento(){
        Random rn = new Random();
        Instrumento i;
        int a = rn.nextInt(10);
        if(a % 2 == 0)
            i = new Guitarra();
        else if(a % 3 == 0)
            i = new Viola();
        else if(a % 5 == 0)
            i = new Uquelele();
        else
            i = new Cuatro();

        return i;
    }
    
}
