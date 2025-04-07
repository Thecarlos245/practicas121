public class JuegoAdivinaImpar extends JuegoAdivinaNumero {

    public JuegoAdivinaImpar(int numeroDeVidas) {
        super(numeroDeVidas);
    }

    
    public boolean validaNumero(int numero) {
        if (numero >= 0 && numero <= 10 && numero % 2 != 0) {
            return true;
        } else {
            System.out.println("El numero no es valido, ingresa un numero impar entre 0 y 10");
            return false;
        }
    }
    
}

