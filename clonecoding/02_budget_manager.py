def show_menu():
    """메뉴 출력 함수"""
    print("\n===== 가계부 =====")
    print("01. 수입 추가")
    print("02. 지출 추가")
    print("03. 내역 보기")
    print("04. 항목 삭제")
    print("05. 잔액 확인")
    print("06. 종료")
    print("====================")

def add_income(records):
        """수입 추가 함수"""
        try:
            amount = int(input("수입 금액: "))
            memo = input("내용: ")
            records.append({
                "type" : "수입",
                "amount" : amount,
                "memo" : memo
            })
            print(f"{amount: ,}원 수입이 추가되었습니다.") # :, 천 단위 콤마
        except ValueError: # 숫자가 아닌 입력 처리
            print("올바른 금액을 입력해 주세요.")

def add_expense(records):
        """지출 추가 함수"""
        try:
            amount = int(input("지출 금액: "))
            memo = input("내용: ")
            records.append({
                "type" : "지출",
                "amount" : amount,
                "memo" : memo
            })
            print(f"{amount: ,}원 지출이 추가되었습니다.")
        except ValueError :
            print("올바른 금액을 입력해 주세요.")

def show_records(records):
    """내역 보기 함수"""
    if not records: # 리스트가 비어있으면
        print("기록된 내역이 없습니다.")
        return
    
    print("\n----- 거래 내역 -----")
    for i, record in enumerate(records, 1) : # enumerate(): 인덱스와 값을 함께 반환
        print(f"{i}. [{record['type']}] {record['amount']:,}원 - {record['memo']}")

def delete_record(records):
    """항목 삭제 함수"""
    show_records(records)
    if not records:
        return
    
    try:
        num = int(input("\n삭제할 항목 번호: "))
        if 1 <= num <= len(records):
            deleted = records.pop(num - 1) # pop(): 리스트에서 항목 제거하고 반환
            print(f"{deleted['type']} {deleted['amount']:,}원이 삭제되었습니다.")
        else:
             print("잘못된 번호입니다.")
    except ValueError:
        print("숫자를 입력해주세요.")

def show_balance(records):
    """잔액 확인 함수"""
    total_income = 0 # 총 수입
    total_expense = 0 # 총 지출

    for record in records: # 모든 기록을 순회       
        if record["type" == "수입"]:
            total_income += record["amount"] # 수입 누적
        else: # 지출
            total_expense += record["amount"] # 지출 누적

    balance = total_income - total_expense # 잔액 계산

    print("\n----- 잔액 현황 -----")
    print(f"총 수입: {total_income:,}원")
    print(f"총 지출: {total_expense:,}원")
    print(f"잔액: {balance:,}원")

    if balance < 0: # 잔액이 마이너스면
        print("⚠️ 지출이 수입보다 많습니다.")

def main():
    """메인 실행 함수"""
    records = [] # 거래 내역을 저장할 리스트

    print("가계부를 시작합니다.")

    while True: # 무한 반복
        show_menu()
        choice = input("\n선택: ")

        if choice == "1":
            add_income(records)
        elif choice == "2":
         add_expense(records)
        elif choice == "3":
          show_records(records)
        elif choice == "4":
           delete_record(records)
        elif choice == "5":
           show_balance(records)
        elif choice == "6":
            print("가계부를 종료합니다.")
            break # 반복문 탈출
        else:
            print("잘못된 선택입니다. 1~6 사이의 숫자를 입력하세요.")

# 프로그램 시작
if __name__ == "__main__": # 이 파일이 직접 실행될 때만 main() 실행
    main()