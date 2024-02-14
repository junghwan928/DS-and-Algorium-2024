# date : 20240214
# file : ds14_blacelet.py
# desc : 스택 전체 구현

# 스택 Full 확인 함수
def isStackFull():
    global SIZE, stack, top
    if top == (SIZE-1):
        return True # 스택이 꽉 찼음
    else:
        return False

# 스택 push 함수
def push(data):
    global SIZE, stack, top
    if isStackFull() == True: # 데이터를 넣을 수 없다.
        print('스택이 꽉 찼습니다.')
        return
    else:
        top += 1
        stack[top] = data

# 스택 Empty 확인 함수
def isStackEmpty():
    global SIZE, stack, top
    if top <= -1 :
        return True # 스택이 비었음
    else:
        return False
    
# 스택 pop 함수
def pop():
    global SIZE, stack, top
    if isStackEmpty() == True:
        print('스택이 비었습니다.')
        return None
    else:
        data = stack[top]
        stack[top] = None
        top -= 1
        return data
    
# 스택 최종 데이터 확인 함수
def peek():
    global stack, top
    if isStackEmpty() == True:
        print('스택이 비었습니다.')
        return None
    else:
        return stack[top]

# 수식괄호 판단 함수
def checkBracket(expr): # '(a + b)'
    for ch in expr: # '(' 'a' '+' 'b' ')'
        if ch in '({[<':  # 여는 괄호
            push(ch)
        elif ch in '>]})': # 닫는 괄호
            out = pop()
            if ch == ')' and out == '(':
                pass
            elif ch == ']' and out == '[':
                pass
            elif ch == '}' and out == '{':
                pass
            if ch == '>' and out == '<':
                pass
            else:
                return False

        else:
            pass
    
    if isStackEmpty() == True:
        return True
    else:
        return False

# 전역 변수 선언
SIZE = 5 # 5칸짜리 스택
stack = [None for _ in range(SIZE)]
top = -1

# 메인 코드
if __name__ == '__main__':
    arr = ['(a+b)',')a*b(', '((a+b)-c', '(a+b]', '(<a+{b+c})']

    for expr in arr:
        top =-1
        print(f'{expr} ==> {checkBracket(expr)}')
        