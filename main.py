from module_phone_book import show_menu, add_phone_num,show_all_phone_num
from time import sleep 

while True:
    menu_num = show_menu()
    
    if menu_num == 0:
        print('프로그램을 종료합니다.')
        break
    elif menu_num == 1:
        add_phone_num()
        
    elif menu_num == 2:
        show_all_phone_num()
    else:
        print('잘못된 입력입니다. 다시 입력해주세요.')
        sleep(2)
        