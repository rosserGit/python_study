# conditional statement - if elif else ex101 -120
print(f'{" Conditional Example":=^50}')

# 문01. 파이썬에서 True 혹은 False를 갖는 데이터 타입은 무엇인가?
print('Ex01. 정답')
print(f'{type(True)} 타입입니다. ')
print('-'*50)

# 문02. 아래 코드의 출력 결과를 예상하라
# print(3 == 5)
print('Ex02. 정답')
print(3==5)
print(f'3 == 5 는 False 입니다.')
print('-'*50)

# 문03. 아래 코드의 출력 결과를 예상하라
# print(3 < 5)
print('Ex03. 정답')
print(3<5)
print(f'3<5는 True 입니다.')
print('-'*50)

# 문04. 아래 코드의 결과를 예상하라.#
# x = 4
# print(1 < x < 5)
print('Ex04. 정답')
x = 4
print(1 < x < 5)
print(f'x=4일때, 1 < x < 5는 True 입니다.')
print('-'*50)

# 문05. 아래 코드의 결과를 예상하라.
# print ((3 == 3) and (4 != 3))
print('Ex05. 정답')
print ((3 == 3) and (4 != 3))
print(f'(3 == 3) and (4 != 3)는 True 입니다.')
print('-'*50)

# 문06. 아래 코드에서 에러가 발생하는 원인에 대해 설명하라.
# print(3 => 4)
print('Ex06. 정답')
print(f'(3 => 4)는 지원하지 않는 연산자임. 3 >= 4로 바꿔줘야 함.(False) ')
print('-'*50)

# 문07. 아래 코드의 출력 결과를 예상하라#
if 4 < 3:
    print("Hello World")

print('Ex07. 정답')
print(f'조건에 만족하지 않기 때문에 출력값이 없음. ')
print('-'*50)

# 문08. 아래 코드의 출력 결과를 예상하라
if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.")

print('Ex08. 정답')
print(f'else 조건에 만족하기 때문에 출력값은 Hi, there. 임. ')
print('-'*50)

# 문09. 아래 코드의 출력 결과를 예상하라

if True :
    print ("1")
    print ("2")
else :
    print("3")
print("4")

print('Ex09. 정답')
print(f'출력값은 1,2,4임. ')
print('-'*50)

# 문10. 아래 코드의 출력 결과를 예상하라

if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")

print('Ex10. 정답')
print(f'출력값은 3,5임. ')
print('-'*50)

# 문11.사용자로부터 입력받은 문자열을 두 번 출력하라. 아래는 사용자가 "안녕하세요"를 입력한 경우의 출력 결과이다.
# >> 안녕하세요
# 안녕하세요안녕하세요
print('Ex11. 정답')
inData = input('>>> ')
print(inData*2)
print('-'*50)

# 문12. 사용자로부터 하나의 숫자를 입력받고, 입력 받은 숫자에 10을 더해 출력하라.
# >> 숫자를 입력하세요: 30
# 40
print('Ex12. 정답')
inNum = input('>> 숫자를 입력하세요.(덧셈) : ')
print(int(inNum)+10)
print('-'*50)

# 문13. 사용자로부터 하나의 숫자를 입력 받고 짝수/홀수를 판별하라.
# >> 30
# 짝수
print('Ex13. 정답')
inNum = int(input('>> 숫자 입력하세요.(홀/짝) : '))
if inNum % 2 == 0:
    print('짝수')
else:
    print('홀수')
print('-'*50)

# 문14. 사용자로부터 값을 입력받은 후 해당 값에 20을 더한 값을 출력하라.
# 단 사용자가 입력한 값과 20을 더한 계산 값이 255를 초과하는 경우 255를 출력해야 한다.
# >> 입력값: 200
# 출력값: 220
# >> 입력값: 240
# 출력값: 255

print('Ex14. 정답')
inNum = int(input('>> 숫자입력 하세요. (덧셈) : '))
num = inNum + 20
if num > 255:
    print('출력값 : 255')
else:
    print(f'출력값 : {num}')
print('-'*50)

# 문15. 사용자로부터 하나의 값을 입력받은 후 해당 값에 20을 뺀 값을 출력하라.
# 단 출력 값의 범위는 0~255이다.
# 예를 들어 결괏값이 0보다 작은 값이되는 경우 0을 출력하고 255보다 큰 값이 되는 경우 255를 출력해야 한다.
#
# >> 입력값: 200
# 출력값: 180
# >> 입력값: 15
# 출력값: 0

print('Ex15. 정답')
inNum = int(input('>> 숫자입력값 (뺄셈): '))
num = inNum - 20
if num > 255:
    print('출력값 : 255')
elif num < 0:
    print(f'출력값 : 0')
else:
    print(f'출력값 : {num}')
print('-'*50)

# 문16. 사용자로부터 입력 받은 시간이 정각인지 판별하라.
# >> 현재시간:02:00
# 정각 입니다.
# >> 현재시간:03:10
# 정각이 아닙니다

print('Ex16. 정답')
inTime = input('>> 현재시간 : ')

if inTime[-2:] == '00':
    print(f'{inTime} - 정각입니다. ')
else:
    print(f'{inTime}- 정각이 아닙니다.')
print('-'*50)

# 문17. 사용자로 입력받은 단어가 아래 fruit 리스트에 포함되어 있는지를 확인하라.
# 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.

print('Ex17. 정답')
fruit = ["사과", "포도", "홍시"]
inFru = input(">> 좋아하는 과일은? ")

if inFru in fruit:
    print(f'{inFru} - 정답입니다.')
else:
    print(f'{inFru} - 오답입니다.')
print('-'*50)

# 문.18.투자 경고 종목 리스트가 있을 때 사용자로부터 종목명을 입력 받은 후
# 해당 종목이 투자 경고 종목이라면 # '투자 경고 종목입니다'를
# 아니면 "투자 경고 종목이 아닙니다."를 출력하는 프로그램을 작성하라.

print('Ex18. 정답')
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
inComp = input(">> 종목명? ")
if inComp in warn_investment_list:
    print(f'{inComp}는 투자경고 종목입니다.')
else :
    print(f'{inComp}는 투자경고 종목이 아닙니다.')
print('-'*50)

# 문19. 아래와 같이 fruit 딕셔너리가 정의되어 있다.
# 사용자가 입력한 값이 딕셔너리 키 (key) 값에 포함되었다면 "정답입니다"를
# 아닐 경우 "오답입니다" 출력하라.
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# >> 제가좋아하는계절은: 봄
# 정답입니다.

print('Ex19. 정답')
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
inSson = input(">> 제가 좋아하는 계절은 :  ")
if inSson in fruit:
    print(f'{inSson} - 정답니다.')
else :
    print(f'{inSson} - 오답입니다.')
print('-'*50)

# 문20. 아래와 같이 fruit 딕셔너리가 정의되어 있다.
# 사용자가 입력한 값이 딕셔너리 값 (value)에 포함되었다면 "정답입니다"를
# 아닐 경우 "오답입니다" 출력하라.
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# >> 좋아하는과일은? 한라봉
# 오답입니다.

print('Ex20. 정답')
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
inFruit = input(">> 좋아하는 과일은 :  ")
if inFruit in fruit.values():
    print(f'{inFruit} - 정답니다.')
else :
    print(f'{inFruit} - 오답입니다.')
print('-'*50)
