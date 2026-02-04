array = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

case = int(input())
for i in range(case):
    n = int(input())
    if n > 10:
        for i in range(10, n):
            array.append(array[i-2] + array[i-3])
    print(array[n-1])
