from module_phone_book import search_and_view_contact, show_menu, add_phone_num,show_all_phone_num, remove_all
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
        
    elif menu_num == 3:
        remove_all()
        
    elif menu_num == 4:
        search_and_view_contact()
        
    else:
        print('잘못된 입력입니다. 다시 입력해주세요.')
        sleep(2)
        