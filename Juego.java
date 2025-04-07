public class Juego {
	protected int numeroDeVidas;
    protected int record;
    
    public Juego(int vidas){
        this.numeroDeVidas = vidas;
        this.record = vidas;
    }
    public void reiniciarPartida(){
        this.record = this.numeroDeVidas;
    }
    public void actualizaRecord(){
        this.record= this.record-1;
    }
    public boolean quitaVida(){
        //this.nroVidas = this.nroVidas-1;
        if(this.numeroDeVidas == 0 ){
            return false;
        }
        else{
            return true;
        }
    }

    public int getNumeroDeVidas() {
        return numeroDeVidas;
    }

    public int getRecord() {
        return record;
    }

    public void setNumeroDeVidas(int numeroDeVidas) {
        this.numeroDeVidas = numeroDeVidas;
    }

    public void setRecord(int record) {
        this.record = record;
    }

}



