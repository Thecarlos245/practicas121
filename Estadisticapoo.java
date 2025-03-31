import java.util.Scanner;

class Estadisticapoo {
    private double[] numeros;

    // Constructor
    public Estadisticapoo (double[] numeros) {
        this.numeros = numeros;
    }

    // Método para calcular el promedio
    public double promedio() {
        double suma = 0;
        for (double num : numeros) {
            suma += num;
        }
        return suma / numeros.length;
    }

    // Método para calcular la desviación estándar
    public double desviacion() {
        double prom = promedio();
        double suma = 0;
        for (double num : numeros) {
            suma += Math.pow(num - prom, 2);
        }
        return Math.sqrt(suma / (numeros.length - 1));
    }



    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double[] numeros = new double[10];

        System.out.println("");

        for (int i = 0; i < 10; i++) {
            if (scanner.hasNextDouble()) {
                numeros[i] = scanner.nextDouble();
            } else {
                System.out.println("Error: Debe ingresar 10 números válidos.");
                scanner.close();
                return;
            }
        }

        Estadisticapoo stats = new Estadisticapoo(numeros);
        System.out.printf("El promedio es %.2f%n", stats.promedio());
        System.out.printf("La desviación es %.6f%n", stats.desviacion());

        scanner.close();
    }
}

