public class CampusBikes {
    public static int[] assignBikes(int[][] students, int[][] bikes) {
        if (students == null || bikes == null) return new int[0];

        int n = students.length; 
        int m = bikes.length;  
        int[] result = new int[n];  // songoson duguig hadgalah

        for (int i = 0; i < n; i++) {
            result[i] = -1;
        }

        boolean[] bikeAssigned = new boolean[m]; 

        for (int i = 0; i < n; i++) {
            int hamginOirDugui = -1;
            int minDistance = Integer.MAX_VALUE;

            for (int j = 0; j < m; j++) {
                if (!bikeAssigned[j]) {
                // хамгийн ойр зайг тооцохдоо |d1.x−d2.x|+|d1.y−d2.y| томьёог ашиглана.
                    int distance = Math.abs(students[i][0] - bikes[j][0]) + Math.abs(students[i][1] - bikes[j][1]);

                    // hamgiin oir dugui songon
                    if (distance < minDistance) {
                        minDistance = distance;
                        hamginOirDugui = j;
                    } else if (distance == minDistance && hamginOirDugui > j) {
                        hamginOirDugui = j;
                    }
                }
            }

            if (hamginOirDugui != -1) {
                result[i] = hamginOirDugui;
                bikeAssigned[hamginOirDugui] = true; 
            }
        }

        return result;
    }


    public static void main(String[] args) {
        int[][] students = {{0, 0}, {1, 1}};
        int[][] bikes = {{0, 1}, {4, 3}, {2, 1}};
        int[] assignedBikes = assignBikes(students, bikes);

        System.out.print("Result: ");
        for (int bike : assignedBikes) {
            System.out.print(bike + " ");
        }
    }
}
// mvn test 