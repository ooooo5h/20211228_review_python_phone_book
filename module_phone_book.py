# 메뉴보기
def show_menu():
    print('===== 전화번호부 메뉴 =====')
    print('1. 전화번호 등록') 
    print('2. 전화번호 목록 조회')
    print('0. 프로그램 종료')
    print('==========================')  
    
    input_num = int(input('원하는 메뉴 선택 : '))
    return input_num