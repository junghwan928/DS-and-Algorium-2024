# file : ds04_orderedList.ipynb
# desc : 선형리스트 프로그램

kakaotalk = [] # 빈 배열 생성

# 데이터 추가 함수
def add_data(friend):
    kakaotalk.append(None) # 배열 빈자를 생성
    size = len(kakaotalk) # 배열 전체 크기
    kakaotalk[size - 1] = friend

# 데이터 삽입 함수
def insert_data(pos, friend):
    if pos < 0 or pos > len(kakaotalk):
        print('data insert 초과')
        return # 함수를 빠져 나감
    
    # 정상적인 처리 시작
    kakaotalk.append(None) # 빈칸 추가
    size = len(kakaotalk)
    # 삽입위치까지 데이터를 하나씩 뒤로 보냄
    for i in range(size-1, pos, -1): #역순으로 맨뒤에서 부터
        kakaotalk[i] = kakaotalk[i - 1]
        kakaotalk[i - 1] = None

    kakaotalk[pos] = friend

# 데이터 함수 삭제 
def delete_data(pos): # 데이터 삭제시 위치값만
    if pos < 0 or pos > len(kakaotalk):
        print('data 삭제범위 초과')
        return
    

    size = len(kakaotalk)
    kakaotalk[pos] = None # data delete

    for i in range(pos+1, size):
        kakaotalk[i-1] = kakaotalk[i] # 뒤에 값을 앞으로
        kakaotalk[i] = None

    del(kakaotalk[size-1]) # 배열의 맨 마지막 값 삭제 

    kakaotalk = []
    select = -1

if __name__ == '__main__':
    select = -1
    while (select != 4):
        select = int(input('select(1. add, 2.insert, 3.delet, 4.exit >)'))

        if select == 1 :
                data = input('add data --> ')
                add_data(data)
                print(kakaotalk)

        elif select == 2:
                pos = int(input('insert_data -->'))
                data = input('add data -->')
                insert_data(pos, data)
                print(kakaotalk)

        elif select == 3:
            pos = int(input('delete_data -->'))
            delete_data(pos, data)
            print(kakaotalk)

        elif select == 4:
            exit(0)

        else:
            print('1~4 중 하나 입력')
            continue