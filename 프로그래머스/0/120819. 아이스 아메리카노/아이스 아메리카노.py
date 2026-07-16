def solution(money):
    answer = []
    num = money // 5500
    left = money - num * 5500
    answer.extend([num,left])
    return answer