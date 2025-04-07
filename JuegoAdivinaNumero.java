import java.util.Scanner;

public class JuegoAdivinaNumero extends Juego{
    Scanner te = new Scanner(System.in);
    private int numeroAAdivinar;
    
    
    public JuegoAdivinaNumero(int numeroDeVidas){
        super(numeroDeVidas);
        this.numeroAAdivinar = (int)(Math.random() * 11);
    }
    public boolean validaNumero(int numero){
         if(numero >= 0 && numero <= 10){
            return true;
         }else{
            return false;
         }
    }

    public void juega(){
        super.reiniciarPartida();
        
        while(this.quitaVida()){
            //System.out.print(this.numeroAAdivinar);
            System.out.print("Ingresa un numeor del 0 al 10: ");
            int numero = te.nextInt();

            if(!validaNumero(numero)){
                System.out.println("El numero no es valido, ingresa un numero entre 0 y 10");
                

            }
            if(this.numeroAAdivinar == numero){
                System.out.println("Acertaste! (Record = "+this.record+")");
                this.numeroAAdivinar = (int)(Math.random() * 11);
            }
            else{
                if(numero >this.numeroAAdivinar){
                    System.out.println("el numero a adivinar es menor, vidas restantes: "+this.numeroDeVidas);
                }
                else{
                    System.out.println("el numero a adivinar es mayor, vidas restantes: "+this.numeroDeVidas);
                }
                this.numeroDeVidas = this.numeroDeVidas-1;
                this.record = this.record-1;
                      
                System.out.println("Intentalo de nuevo \n te quedan: "+this.numeroDeVidas+" vidas");
            }
        }
        System.out.println("---------------------------");
        System.out.println("Juego Terminado \n record: "+this.record);
    }
    public int getNumeroAAdivinar() {
        return numeroAAdivinar;
    }
    public void setNro(int x){
        this.numeroAAdivinar =x;
    } 
}       