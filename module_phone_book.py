from time import sleep

# 메뉴보기
def show_menu():
    print('===== 전화번호부 메뉴 =====')
    print('1. 전화번호 등록') 
    print('2. 전화번호 목록 조회')
    print('3. 전체 전화번호부 삭제')
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
        
        input_info = f'{name}, {phone_num}, {memo}\n'
        file.write(input_info)
    
    print('전화번호 등록이 완료되었습니다.')
    sleep(2)
    
# 2번 모든 목록 표시
def show_all_phone_num():
    
    with open('phone_book.txt', 'r') as file:
        
        all_info_list = file.readlines()
        
        for info in all_info_list:
                    
            info = info.strip()    
            print(info)
        
# 3번 모든 기록 삭제
def remove_all():
    
    input_answer = input('정말 삭제하시겠습니까? (Y/N) : ')
    
    if input_answer == 'Y':
            
        with open('phone_book.txt', 'w') as file:       
            pass
        print('모든 기록이 삭제되었습니다.')
        
    elif input_answer == 'N':
        print('전체 삭제가 취소되었습니다.')
        
    sleep(2)