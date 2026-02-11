people = 3
apple = 20

# 01. if: if 조건문의 시작
# 02. people < apple / 5: 실행 여부를 결정하는 조건
if people < apple / 5: # 03. 조건식 끝에 콜론 기호
    print("사과가 많아") # 04. 들여쓰기 후 조건이 참이면 실행할 코드

if people % apple > 0:
    print("사과가 적어")

if people > apple:
    print("몇 명은 굶어라")