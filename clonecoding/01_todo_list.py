# Todo List 2026. 02. 11

def show_menu():
    """메뉴 출력 함수"""
    print("\n===== Todo List =====")
    print("01. 할 일 추가")
    print("02. 할 일 목록 보기")
    print("03. 할 일 완료")
    print("04. 할 일 삭제")
    print("05. 종료")
    print("====================")

def add_todo(todos):
    """할 일 추가 함수"""
    task = input("추가할 할 일: ")
    todos.append({"task": task, "done": False})
    print(f"'{task}'이(가) 추가되었습니다.")

def show_todos(todos):
    """할 일 목록 출력 함수"""
    if not todos: # 리스트가 비어있으면
        print("할 일이 없습니다.")
        return
    
    print("\n----- 할 일 목록 -----")
    for i, todo in enumerate(todos, 1): # enumerate(): 인덱스와 값을 함께 반환
        status = "✓" if todo["done"] else " " # 완료 여부 표시
        print(f"{i}. [{status}] {todo['task']}")

def complete_todo(todos):
    """할 일 완료 처리 함수"""
    show_todos(todos)
    if not todos:
        return

    try:
        num = int(input("\n완료한 할 일 번호: "))
        if 1 <= num <= len(todos):
            todos[num - 1]["done"] = True
            print(f"'{todos[num-1]['task']}'을(를) 완료했습니다.")

        else:
            print("잘못된 번호입니다.")
    except ValueError: # 숫자가 아닌 입력 처리
        print("숫자를 입력해주세요.")

def delete_todo(todos):
    """할 일 삭제 함수"""
    show_todos(todos)
    if not todos:
        return
    
    try:
        num = int(input("\n삭제할 할 일 번호:"))
        if 1 <= num <= len(todos):
            deleted = todos.pop(num - 1) # pop(): 리스트에서 항목 제거하고 반환
            print(f"'{deleted['task']}'이(가) 삭제되었습니다.")
        else:
            print("잘못된 번호입니다.")
    except ValueError:
        print("숫자를 입력해주세요.")

def main():
    """메인 실행 함수"""
    todos = [] # 할 일을 저장할 리스트

    print("Todo List를 시작합니다.")

    while True: # 무한 반복
        show_menu()
        chice = input("\n선택: ")

        if chice == "1":
            add_todo(todos)      # 추가
        elif chice == "2":
            show_todos(todos)    # 목록 보기
        elif chice == "3":
            complete_todo(todos) # 완료
        elif chice == "4":
            delete_todo(todos)   # 삭제
        elif chice == "5":       # 종료
            print("프로그램을 종료합니다.")
            break # 반복문 탈출

        else:
            print("1에서 5 사이의 숫자만 입력하세요.")

# 프로그램 시작
if __name__ == "__main__": # 이 파일이 직접 실행될 때만 main() 실행
    main()