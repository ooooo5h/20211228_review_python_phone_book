from module_Phone_book import show_menu

while True:
    menu_num = show_menu()
    
    if menu_num == 0:
        print('프로그램을 종료합니다.')
        break
    elif menu_num == 1:
        pass
    elif menu_num == 2:
        pass
    else:
        print('잘못된 입력입니다. 다시 입력해주세요.')