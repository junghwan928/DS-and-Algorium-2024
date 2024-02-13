# file: ds07_simpleLinkedList.py
# desc: 단순 연결 리스트 학습

memory = [] # 컴퓨터 메모리를 유사 구성
# head , curr, prev 일반 변수
# head = node
head, curr, prev = None, None, None

class Node():
    # data, link 두개의 멤버변수 존재
    # 생성자 추가
    def __init__(self, name) -> None:
        self.data = name
        self.link = None


# 클래스 끝        
def printNodes(start): # 클래스의 멤버 함수 x
    curr = start
    if curr == None: return # 함수를 빠져나감
    print(curr.data, end = ' -> ')
    while curr.link != None:
        curr = curr.link # 내 노드 다음 노드가 current가 됨
        print(curr.data, end=' -> ') # end -> 로 해서 enter가 없음
    print() # enter추가

dataArray = ['가현', '나현','다현', '라연', '마현']

# 메인시작
if __name__ == '__main__':
    node = Node(dataArray[0]) # '가현' 이라는 데이터를 담은 노드 생성
    head = node # 첫번째 값을 head 가 가리킴
    memory.append(node) # 가짜 메모리에 집어 넣음

    for data in dataArray[1:]:
        prev = node
        node = Node(data) #나현
        prev.link = node
        memory.append(node)

    printNodes(head)