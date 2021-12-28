from time import sleep
from datas import ContactInfo

# 메뉴보기
def show_menu():
    print('===== 전화번호부 메뉴 =====')
    print('1. 전화번호 등록') 
    print('2. 전화번호 목록 조회')
    print('3. 모든 연락처 삭제')
    print('4. 사용자 상세 조회')
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
            # print(info)
            
            # line은 ,로 붙여진 여러정보를 split으로 분해해서 가공하자
            info_list = info.split(',')
            
            # 핸드폰 번호 표현하는 클래스 제작해서 , 가공해서 출력하는 기능으로 구현하기
            # 연락처 객체 생성 => 생성자 활용
            contact = ContactInfo(info_list[0], info_list[1], info_list[2])
            
            # 가공해서 출력해주는 기능을 활용해서, 클래스에 메쏘드를 추가하자
            contact.print_contact_info()
        sleep(2)
        
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
    
# 4번 상세조회    -> 나는 Contact클래스안에 왜 넣었을까..? 이름안에 contact가 들어갔다고해서 contact에 만들었나봄
# 기능추가니까 기능추가는 모듈에 !!! 
def search_and_view_contact():
        print('----- 사용자 검색 -----')
        search_name = input('조회할 사용자 이름 : ')
        
        with open('phone_book.txt', 'r') as file:
            line_list = file.readlines()

            for line in line_list:
                line = line.strip()  #  빼먹은 코드 한 줄
                
                if f'{search_name},' in line:
                    infos = line.split(',')
                    
                    contact = ContactInfo(infos[0], infos[1], infos[2])
                    
                    # 상세보기 기능 활용
                    contact.print_contact_info_detail()
                    sleep(2)