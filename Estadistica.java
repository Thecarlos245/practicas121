import java.util.Scanner;

public class Estadistica {

    // Método para calcular el promedio
    public static double promedio(double[] numeros) {
        double suma = 0;
        for (double num : numeros) {
            suma += num;
        }
        return suma / numeros.length;
    
    }

    // Método para calcular la desviación estándar
    public static double desviacion(double[] numeros) {
        double promedio = promedio(numeros);
        double sumaDiferenciasCuadradas = 0;
        for (double num : numeros) {
            sumaDiferenciasCuadradas += Math.pow(num - promedio, 2);
        }
        return Math.sqrt(sumaDiferenciasCuadradas / (numeros.length - 1));
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double[] numeros = new double[10];

        // Solicitar 10 números al usuario
        System.out.println(" " );
        String[] entrada = sc.nextLine().split(" ");
        for (int i = 0; i < 10; i++) {
            numeros[i] = Double.parseDouble(entrada[i]);
        }

        // Calcular y mostrar el promedio y la desviación estándar
        System.out.printf("El promedio es %.2f%n", promedio(numeros));
        System.out.printf("La desviación estándar es %.5f%n", desviacion(numeros));

        sc.close();
    }
}
