## file: ds24_forFactorial.py
# desc: 반복문으로 팩토리얼 구하기 fact(n)
# n! = 1×2×3×⋯⋯×(n−1)×n

n = 30
factValue = 1 # 곱셈으로 1부터

for i in range(n, 0, -1): # n ~ 1까지 역순
    factValue *= i

print(f'{n}! = {factValue}')

# 재귀호출 factorial
def factorial(num):
    if num <= 1: 
        return 1

    return num * factorial(num - 1)

print(f'{n}! = {factValue}')

# 10 = 3628800, 20 = 2432902008176640000
# 재귀호출 1000 -> RecursionError: maximum recursion depth exceeded => 재귀호출 최고 깊이를 초과
