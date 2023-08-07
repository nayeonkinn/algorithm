import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] binary = new int[17];
        int idx = 0;

        while (n >= 2) {
            binary[idx++] = n % 2;
            n /= 2;
        }
        binary[idx] = n;
        
        for (int i = idx; i >= 0; i--)
            System.out.print(binary[i]);
    }
}