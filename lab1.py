N = int(input("N = "))
M = int(input("M = "))
matrix = []
for i in range(N):
        matrix.append([])
        for j in range(M):
            matrix[i].append(int(input()))
        print(matrix)
# сумма
s = [0]*M
for j in range(M):
    for i in range(N):
        s[j] += matrix[i][j]
    print('\n' + "Сумма столбца: " + '%1d' % s[j], end='')
print()
# произведение
p = [1]*M
for j in range(M):
    for i in range(N):
        p[j] *= matrix[i][j]
    print('\n' + "Произведение столбца: " + '%1d' % p[j], end='')
print()
# максимальное
maxi = [0]*M
for j in range(M):
    for i in range(N):
        if maxi[j] < matrix[i][j]:
            maxi[j] = matrix[i][j]
    print('\n' + "Максимальное значение столбца: " + '%1d' % maxi[j], end='')
print()
# минимальное
mini = maxi
for j in range(M):
    for i in range(N):
        if mini[j] > matrix[i][j]:
            mini[j] = matrix[i][j]
    print('\n' + "Минимальное значение столбца: " + '%1d' % mini[j], end='')
print()
input()






