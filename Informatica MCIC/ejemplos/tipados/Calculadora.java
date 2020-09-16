package tipados;

public class Calculadora {
    private int valor1;
    private int valor2;
    private int resultado;

    public void setValor1(int val){
        this.valor1 = val;
    }
    
    public void setValor2(int val){
        this.valor2 = val;
    }

    public int getResultado(){
        return this.resultado;
    }

    public void sumar(){
        this.resultado = this.valor1 + this.valor2;
    }
}
