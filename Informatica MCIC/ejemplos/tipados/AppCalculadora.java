package tipados;

public class AppCalculadora {
    public static void main(String[] args) {
        Calculadora c = new Calculadora();
        c.setValor1(5);
        c.setValor2(3);
        c.sumar();
        System.out.println(c.getResultado());
    }

}
