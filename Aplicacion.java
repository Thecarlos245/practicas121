public class Aplicacion {
    public static void main(String[] args) {
        JuegoAdivinaNumero juego1 = new JuegoAdivinaNumero(3);
        JuegoAdivinaPar juego2 = new JuegoAdivinaPar(3);
        JuegoAdivinaImpar juego3 = new JuegoAdivinaImpar(3);

    
        System.out.println("Juego Adivina Número:");
        juego1.juega();

        System.out.println("\nJuego Adivina Número Par:");
        juego2.juega();

        System.out.println("\nJuego Adivina Número Impar:");
        juego3.juega();
    }
}



