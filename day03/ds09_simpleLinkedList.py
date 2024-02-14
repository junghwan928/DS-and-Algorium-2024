## file : ds09_simpleLinkedList.ipynb
# desc : 다시 연결리스트 전체 구현 

class Node():
    data = None # 설계 데이터 변수
    link = None # Next Node를 지정하는 변수
    
    def __init__(self) -> None:
        self.data = None # 클래스 자신이 self이므로 클래스의 변수에 접근 할려면 반드시 self.
        self.link = None 
    
    def printNodes(start): # start부터 시작해서 끝까지 노드.data 출력
        curr = start # start == head
        if curr == None: return # break, countinue는 반복문 없으면 안됨
        while True:
            if curr.link == None: # 연결할 노드 더이상 없으면
                print(curr.data) # 자기 데이터만 출력
                break # 반복문 출력
            else: 
                print(curr.data, end=' -> ') # 연결할 노드가 있으니까 연결표시 -> 를 해줌
                curr = curr.link # 자기 뒤의 데이터 curr로 변경