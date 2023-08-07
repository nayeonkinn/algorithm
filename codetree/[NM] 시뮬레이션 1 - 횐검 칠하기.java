import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();

        char[] tile = new char[200000];
        int[] whiteTile = new int[200000];
        int[] blackTile = new int[200000];

        int idx = 99999;
        int maxIdx = 99999;
        int minIdx = 99999;

        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            char order = sc.next().charAt(0);

            if (order == 'L') {
                for (int j = 0; j < x; j++) {
                    tile[idx] = 'w';
                    whiteTile[idx--] += 1;
                }
                if (++idx < minIdx) 
                    minIdx = idx;
            } else {
                for (int j = 0; j < x; j++) {
                    tile[idx] = 'b';
                    blackTile[idx++] += 1;
                }
                if (--idx > maxIdx) 
                    maxIdx = idx;
            }
        }

        int whiteCnt = 0;
        int blackCnt = 0;
        int grayCnt = 0;

        for (int i = minIdx; i <= maxIdx; i++) {
            if (whiteTile[i] >= 2 && blackTile[i] >= 2) {
                grayCnt += 1;
            } else {
                whiteCnt += (tile[i] == 'w') ? 1 : 0;
                blackCnt += (tile[i] == 'b') ? 1 : 0;
            }
        }

        System.out.print(whiteCnt + " " + blackCnt + " " + grayCnt);
    }
}