## file: ds24_forFactorila.py
## desc: 반복문으로 팩토리얼 구하기

n = 30
factValue = 1 # 곱셈으로 1부터

for i in range(n, 0, -1): # n ~ 1 역순
    factValue *= i

print(f'{n}! = {factValue}')

# 재귀호출 factorial
def factorial(num):
    if num <= 1: 
        return 1

    return num * factorial(num - 1)

print(f'{n}! = {factValue}')

# 10 = 362880
# 재귀 호출 1000 하면 RecursionError : Maximum recursion depth exceeded 재귀호출 최고 깊이를 초과 