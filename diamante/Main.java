

public class Main {
    public static void main(String[] args) {
       
        D objeto = new D(5,10,3);
        System.out.println("----------------------------");
        objeto.x += 1;
        objeto.z += 1;
        System.out.println("IncrementaXZ:");
        System.out.println("x: " + objeto.x + ", y: " + objeto.y + ", z: " + objeto.z);
        System.out.println("----------------------------");
        objeto.y += 1;
        objeto.z += 1;
        System.out.println("IncrementaYZ:");
        System.out.println("x: " + objeto.x + ", y: " + objeto.y + ", z: " + objeto.z);
        objeto.incrementaXYZ();
        System.out.println("----------------------------");
        System.out.println("IncrementaXYZ:");
        System.out.println("x: " + objeto.x + ", y: " + objeto.y + ", z: " + objeto.z);
    }
}



