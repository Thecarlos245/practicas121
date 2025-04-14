
public class D extends A {
    int y;
    public D(int x, int y, int z) {
        super(x, z);
        
        this.y = y;
        this.z = z;
    }
    public void incrementaXYZ() {
        this.x = x +1;
        this.y = y + 1;
        this.z = z + 1;
    }
}

