## file: ds23_rcSum.py
## desc: 재귀호출 합산함수

def addNum(num):
    if num <= 1:
        return 1
    
    return num + addNum(num-1) # 5 + addNum(4) + addNum(3) + addNum(2) + addNum(1)

sum = addNum(5) # 15
print(sum)
