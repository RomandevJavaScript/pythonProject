# matrix_simetric = [
#     [0, 3, 10],
#     [4, 9, 3],
#     [7, 4, 0]
#
# ]
# matrix_not_simetric = [
#     [0, 1, 2],
#     [1, 2, 7],
#     [2, 3, 4]
#
# ]
#
#
# def f(m):
#     m1, m2, c, k = [], [], len(m) - 1, 0
#     for i in range(len(m)):
#         m1 += m[i][:c]
#         m2 += m[i][k:]
#         c -= 1
#         k -= 1
#         res = set(m1 + m2[len(m(0)):])
#     return "YES" if len(res) == m1 else "NO"
#
#
# print(f(matrix_simetric));
# print(f(matrix_not_simetric));
n = int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
    a[i][(n - 1)- i] = 1
    for j in range(n - i, n):
        a[i][j] = 2
for row in a:
    print(' '.join([str(elem) for elem in row]))