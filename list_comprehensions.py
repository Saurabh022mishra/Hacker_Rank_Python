"""You are given three integers a, Y and z representing the dimensions of a cuboid along with an integer n.
 Print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i + j + k is not equal to n. 
 Here,
0 SiS«;0 < jSy;0 < k ≤ z. Please use list comprehensions rather than multiple loops, as a learning exercise.
Example
7 = 1
y = 1
z = 2
n = 3
All permutations of (i, j, k] are:
[10, 0, 01, [0, 0, 11, (0, 0, 21, (0, 1, 0), (0, 1, 1], (0, 1, 2], [1, 0, 01, (1, 0, 1],
.
Print an array of the elements that do not sum to n. = 3.
[f0, 0, 0], (0, 0, 1], [0, 0, 2], (0, 1, 0], [0, 1, 1], [1, 0, 0], (1, 0, 1], (1, 1, 0].
Input Format
Four integers a, y, z and n, each on a separate line."""
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    print(coordinates)