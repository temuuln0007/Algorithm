import java.util.Arrays;
import java.util.Collections;

public class MinimumCost {
    public static int findMinimumCost(int[] k, Integer[] f) {
        int n = k.length;
        int greTrue = 0;
        int greFalse = 0;

        for (int i = 0; i < n; i++) {
            greFalse += f[i] * (i + 1);
        }

        Arrays.sort(f, Collections.reverseOrder());

        for (int i = 0; i < n; i++) {
            greTrue += f[i] * (i + 1);
        }
        
        return Math.min(greTrue, greFalse);
    }

    public static void main(String[] args) {
        int[] k = {5, 6};
        Integer[] f = {17, 25};

        int minCost = findMinimumCost(k, f);
        System.out.println("Хамгийн бага өртөг: " + minCost);
    }
}
