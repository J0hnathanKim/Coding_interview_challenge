ans = 0
def DFS(n, total, numbers, target):
    global ans
    if n == len(numbers):
        if total == target:
            ans += 1
        return
    DFS(n+1, total + numbers[n], numbers, target)
    DFS(n+1, total - numbers[n], numbers, target)


def solution(numbers, target):
    DFS(0, 0, numbers, target)
    return ans
