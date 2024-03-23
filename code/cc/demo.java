public class demo {
    public static void main(String[] args) {
        long count = 0;
        while (true) {
            count++;
            if (count % 1000000000 == 0) {
                System.out.printf("" + count + "\r");
            }
        }
    }
}