from time import sleep

# 메뉴보기
def show_menu():
    print('===== 전화번호부 메뉴 =====')
    print('1. 전화번호 등록') 
    print('2. 전화번호 목록 조회')
    print('0. 프로그램 종료')
    print('==========================')  
    
    input_num = int(input('원하는 메뉴 선택 : '))
    return input_num

# 1번 전화번호 등록
def add_phone_num():
    name = input('이름 : ')
    phone_num = input('연락처 : ')
    memo = input('특이사항 : ')
    
    with open('phone_book.txt', 'a') as file:
        
        input_info = f'{name}, {phone_num}, {memo}'
        file.write(input_info)
    
    print('전화번호 등록이 완료되었습니다.')
    sleep(2)