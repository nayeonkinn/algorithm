import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        int minutes = (((a * 24) + b) * 60 + c) - (((11 * 24) + 11) * 60 + 11);
        
        System.out.println(minutes >= 0 ? minutes : -1);
    }
}