name = "쨈미"
age = 30
score = 80

# if문
if age >= 20:
    print("성인입니다")
else:
    print("미성년자입니다")

# for문
for i in range(5):
       print(i)

# while문
count = 0
while count < 3:
      print(count)
      count += 1

# 함수 정의
def great(name):
    return f"안녕하세요, {name}님"

# 리스트
fruits = ["사과", "딸기", "바나나"]
for fruits in fruits:
    print(fruits)

# try-except
try:
    result = 10 / 0
except ZeroDivisionError:
     print("0으로 나눌 수 없습니다")
    
# 딕셔너리
person = {
     "name" : "쨈미",
     "age" : 30
}
print(person["name"])