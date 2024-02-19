## file: ds23_rcSum.py
## desc: 재귀호출 합산함수

def addNum(num):
    if num <= 1:
        return 1
    
    return num + addNum(num-1) # 5 + addNum(4) + addNum(3) + addNum(2) + addNum(1)
     # 5 + addNumber(4)[4 + addNumber(3)[3 + addNumber(2)[2 + addNumber(1)]]]

sum = addNum(5) # 15(5+4+3+2+1)
print(sum)
