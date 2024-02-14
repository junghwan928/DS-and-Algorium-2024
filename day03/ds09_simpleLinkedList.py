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

# Node insert
def insertNode(find, data):


    global head, prev, curr # 전역 변수를 insertNode()에서 사용 하겠다고 사용
    if head.data == find: # 맨 첫번째 노드 
        node = Node()
        node.data = '화사'
        node.link = head 
        head = node 
        return # 함수 탈출

    curr = head
    while curr.link != None:
        prev = curr
        curr = curr.link
        if curr.data == find: # 데이터 찾았으면
            node = Node()
            node.data = data
            node.link = curr # 찾은 노드 앞에 새 노드 연결
            prev.link = node # 이전 노드 뒤에 새 노드 연결
            return # 함수 탈출

    node = Node() # 맨 마지막에 노드 삽입
    node.data = data
    curr.link = node
    return 


# 노드 삭제 함수
def deleteNode(data):
    global head, prev, curr

    if head.data == data: # 첫번째 노드 삭제면
        curr = head
        head = head.link
        del(curr)
        return # 함수 탈출
    
    curr = head
    while curr.link != None:
        prev = curr
        curr = curr.link

    if curr.data == data: # 다현 노드라면
        prev.link = curr.link
        # curr.link = None # 굳이 이부분은 필요 없음
        del(curr)


def findNode(find):
    global head, curr

    curr = head
    if curr.data == find:
        return curr
    while curr.link != None:
        curr = curr.link
        if curr.data == find:
            return curr
    
    return Node()


# 전역 변수
head, prev, curr = None, None, None
originData = ['가현', '나현', '다현', '라현', '마현']

# 메인코드 영역
if __name__ == '__main__':
    node = Node()
    node.data = originData[0] # '가현'
    head = node # head = node를 가리킴

    for name in originData[1:]: # 1번 인덱스 부터 리스트 끝까지 반복
        prev = node
        node = Node()
        node.data = name
        prev.link = node

        # 연결 리스트 구성완료
        print('최초 구성된 연결 리스트')
        printNodes(head) # 구성된 연결리스트가 맞는지 출력 확인

        # insert node
        print('맨 앞Node 추가')
        insertNode('가현', '정국')
        printNodes(head)

        print('중간 노드 삽입')
        insertNode('다현', '미미')
        printNodes(head)

        print('마지막 노드 삽입')
        insertNode('재남', 'RM')
        printNodes(head)
        
        # delete node
        print('맨 앞 노드 삭제')
        deleteNode('정국')
        printNodes(head)

        print('중간 노드 삭제')
        deleteNode('미미')
        printNodes(head)

         # 노드검색
        find = findNode('다현')
        printNodes(head)
        print(f'찾은 노드 :{fNode.data}')
        

        find = findNode('쯔위')
        printNodes(head)
        print(f'찾은 노드 :')