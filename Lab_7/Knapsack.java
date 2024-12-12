import java.util.Arrays;
import java.util.Comparator;

class Knapsack {
    static class Item {
        double valuePerWeight;
        int weight;
        int value;

        Item(double valuePerWeight, int weight, int value) {
            this.valuePerWeight = valuePerWeight;
            this.weight = weight;
            this.value = value;
        }
    }

    public static double bag(int w, int[] weights, int[] values) {
        int n = weights.length;
        Item[] items = new Item[n];

        // Create an array of items with value-to-weight ratio
        for (int i = 0; i < n; i++) {
            items[i] = new Item((double) values[i] / weights[i], weights[i], values[i]);
        }

        // Sort items by value-to-weight ratio in descending order
        Arrays.sort(items, Comparator.comparingDouble((Item item) -> item.valuePerWeight).reversed());

        double totalProfit = 0;
        int remainingCapacity = w;

        for (Item item : items) {
            if (remainingCapacity >= item.weight) {
                totalProfit += item.value;
                remainingCapacity -= item.weight;
            } else {
                totalProfit += item.value * ((double) remainingCapacity / item.weight);
                break;
            }
        }

        return totalProfit;
    }

    public static void main(String[] args) {
        int[] weights = {10, 20, 30};
        int[] values = {60, 100, 120};
        int w = 50;

        System.out.println("Үүргэвчинд цуглуулсан хамгийн их нийлбэр : " + bag(w, weights, values));
    }
}
