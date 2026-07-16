def solution(n):
    answer = 0
    if n % 2 == 0 and n % 3 != 0:
        answer = n / 2
    elif n % 2 != 0 and n % 3 == 0:
        answer = n / 3
    elif n % 2 == 0 and n % 3 == 0:
        answer = n / 6
    else:
        answer = n
    return answer