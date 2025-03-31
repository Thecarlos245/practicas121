import java.util.Scanner;

public class Ecuaciones {

    
    public double getDiscriminante(double a, double b, double c) {
        return (b * b) - 4 * a * c;
    }

    
    public double getRaiz1(double a, double b, double discriminante) {
        return (-b + Math.sqrt(discriminante)) / (2 * a);
    }

    
    public double getRaiz2(double a, double b, double discriminante) {
        return (-b - Math.sqrt(discriminante)) / (2 * a);
    }

    public static void main(String[] args) {
        Ecuaciones x = new Ecuaciones();
        Scanner sc = new Scanner(System.in);

    
        System.out.println("Ingrese a, b, c: ");
        String input = sc.nextLine();
        String[] valores = input.split(" ");
        double a = Double.parseDouble(valores[0]);
        double b = Double.parseDouble(valores[1]);
        double c = Double.parseDouble(valores[2]);

    
        double discriminante = x.getDiscriminante(a, b, c);

    
        if (discriminante > 0) {
            System.out.printf("La ecuación tiene dos raíces: %.6f y %.5f%n",
                    x.getRaiz1(a, b, discriminante), x.getRaiz2(a, b, discriminante));
        } else if (discriminante == 0) {
            System.out.printf("La ecuación tiene una raíz: %.5f%n", x.getRaiz1(a, b, discriminante));
        } else {
            System.out.println("La ecuación no tiene raíces reales.");
        }

        sc.close();
    }
}