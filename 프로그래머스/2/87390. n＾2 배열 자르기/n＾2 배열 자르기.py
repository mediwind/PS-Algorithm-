def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        a, b = i // n, i % n
        answer.append(max(a, b) + 1)
    return answer