import unittest
from typing import List

def assign_bikes(students, bikes):
    n = len(students)
    m = len(bikes)
    result = [-1] * n
    distances = []

    for i, (sx, sy) in enumerate(students):
        #print(i, (sx, sy))
        for j, (bx, by) in enumerate(bikes):
            distance = abs(sx - bx) + abs(sy - by)
            distances.append((distance, i, j))

    print("before:", distances)
    distances.sort(key=lambda x: (x[0], x[1], x[2]))
    print("after:", distances)

    bike_assigned = [False] * m
    student_assigned = [False] * n

    for _, student, bike in distances:
        if not student_assigned[student] and not bike_assigned[bike]:
            result[student] = bike
            student_assigned[student] = True
            bike_assigned[bike] = True

    for i in range(n):
        if not student_assigned[i]:
            result[i] = -1

    return result

data = assign_bikes([[0, 0], [1, 1]], [[0, 1], [4, 3], [2, 1]])
print(data)

class TestAssignBikes(unittest.TestCase):
    def test_example_case(self):
        students = [[0, 0], [1, 1]]
        bikes = [[0, 1], [4, 3], [2, 1]]
        self.assertEqual(assign_bikes(students, bikes), [0, 2]) 

    def test_one_student_one_bike(self):
        students = [[1, 1]]
        bikes = [[2, 2]]
        self.assertEqual(assign_bikes(students, bikes), [0])  #

    def test_multiple_students_one_bike(self):
        students = [[1, 1], [2, 2], [3, 3]]
        bikes = [[2, 2]]
        self.assertEqual(assign_bikes(students, bikes), [-1, 0, -1])  

    def test_multiple_bikes_one_student(self):
        students = [[0, 0]]
        bikes = [[1, 1], [0, 1], [2, 2]]
        self.assertEqual(assign_bikes(students, bikes), [1])  

    def test_tie_distance(self):
        students = [[0, 0], [0, 0]]
        bikes = [[1, 0], [0, 1]]
        self.assertEqual(assign_bikes(students, bikes), [0, 1])  

unittest.main()
