import static org.junit.jupiter.api.Assertions.assertArrayEquals;

import org.junit.jupiter.api.Test;

class CampusBikesTest {

    @Test
    void testExampleCase() {
        int[][] students = {{0, 0}, {1, 1}};
        int[][] bikes = {{0, 1}, {4, 3}, {2, 1}};
        int[] expected = {0, 2};
        assertArrayEquals(expected, CampusBikes.assignBikes(students, bikes));
    }

    @Test
    void testSingleStudentAndBike() {
        int[][] students = {{1, 1}};
        int[][] bikes = {{2, 2}};
        int[] expected = {0};
        assertArrayEquals(expected, CampusBikes.assignBikes(students, bikes));
    }

    @Test
    void testMultipleStudentsOneBike() {
        int[][] students = {{1, 1}, {2, 2}, {3, 3}};
        int[][] bikes = {{2, 2}};
        int[] expected = {-1, 0, -1};
        assertArrayEquals(expected, CampusBikes.assignBikes(students, bikes));
    }

    @Test
    void testMultipleBikesOneStudent() {
        int[][] students = {{0, 0}};
        int[][] bikes = {{1, 1}, {0, 1}, {2, 2}};
        int[] expected = {1};
        assertArrayEquals(expected, CampusBikes.assignBikes(students, bikes));
    }

    @Test
    void testTieDistances() {
        int[][] students = {{0, 0}, {0, 0}};
        int[][] bikes = {{1, 0}, {0, 1}};
        int[] expected = {0, 1};
        assertArrayEquals(expected, CampusBikes.assignBikes(students, bikes));
    }

    @Test
    void testEmptyInput() {
        int[][] students = {};
        int[][] bikes = {};
        int[] expected = {};
        assertArrayEquals(expected, CampusBikes.assignBikes(students, bikes));
    }

    @Test
    void testMoreBikesThanStudents() {
        int[][] students = {{0, 0}, {1, 1}};
        int[][] bikes = {{0, 1}, {4, 3}, {2, 1}, {1, 2}};
        int[] expected = {0, 2};
        assertArrayEquals(expected, CampusBikes.assignBikes(students, bikes));
    }
}
