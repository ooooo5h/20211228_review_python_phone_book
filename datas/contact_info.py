class ContactInfo():
    def __init__(self, name, phone_num, memo):
        self.name = name
        self.phone_num = phone_num
        self.memo = memo
    
    # 항목들을 가공해서 출력해주는 기능 추가
    def print_contact_info(self):
        print(f'{self.name} : {self.phone_num} - {self.memo}')
        
    # 상세보기 기능 추가 - 여러줄로 나열
    def print_contact_info_detail(self):
        print('----- 연락처 정보 상세 조회 -----')
        print(f'이름 : {self.name}')
        print(f'연락처 : {self.phone_num}')
        print(f'특이사항 : {self.memo}')