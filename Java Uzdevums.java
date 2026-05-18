class Main {
    public static void main(String[] args) {
        double x, y;
        x = -3.0;
        do {
            y = 2 * x - 1;
            System.out.println("x="+x +" y="+y);
            x = x + 0.5;
            
        } while(x <= 1);

 }
}