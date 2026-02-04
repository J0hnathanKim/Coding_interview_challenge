array = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
case = int(input())
for i in range(case):
    n = int(input())
    while len(array) < n:
        array.append(array[-2] + array[-3])
    print(array[n-1])
    
