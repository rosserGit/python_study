# python function ex211~220
print(f'{" function Example":=^50}')

# 문1. 함수의 호출 결과를 예측하라.
# def 함수(문자열) :
#     print(문자열)
# 함수("안녕")
# 함수("Hi")

print('Ex1. 정답')
print('안녕')
print('Hi')
print('-'*50)

# 문2. 함수의 호출 결과를 예측하라.
# def 함수(a, b) :
#     print(a + b)
# 함수(3, 4)
# 함수(7, 8)

print('Ex2. 정답')
print('7')
print('15')
print('-'*50)

# 문3. 아래와 같은 에러가 발생하는 원인을 설명하라.
# def 함수(문자열) :
#     print(문자열)
# 함수()
# TypeError: 함수() missing 1 required positional argument: '문자열'

print('Ex3. 정답')
print('함수에 정의와 다르게 함수를 호출하고 있다. 함수를 호출할 때 하나의 파라미터를 입력해야한다.')
print('-'*50)

# 문4. 아래와 같은 에러가 발생하는 원인을 설명하라.
# def 함수(a, b) :
#     print(a + b)
# 함수("안녕", 3)
# TypeError: must be str, not int

print('Ex4. 정답')
print('str type과 int type 연산은 안되기 때문')
print('정의된 함수는 같은 타입의 두 개의 값을 입력 받아 덧셈 연산을 적용하려는 의도로 설계됐습니다.\n'
      '하지만 함수를 호출 할때 문자열과 숫자를 입력해서 문자열과 숫자는 더할 수 없다는'
      '에러가 발생합니다.')
print('-'*50)

# 문5. 하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는
# print_with_smile 함수를 정의하라.

def print_with_smile(str):
    print(str,':D')

# 문6. 문5에서 정의한 함수를 호출하라. 파라미터는 "안녕하세요"로 입력하라.

print('Ex5, Ex6 정답')
print_with_smile("안녕하세요")
print('-'*50)

# 문7. 현재 가격을 입력 받아 상한가 (30%)를 출력하는 print_upper_price 함수를 정의하라.

def print_upper_price(price):
    uPrice=price * 1.3
    return uPrice

print('Ex7. 정답')
#print(print_upper_price(int(input('입력>>>'))))
print(print_upper_price(3000))
print('-'*50)

# 문8. 두 개의 숫자를 입력받아 두 수의 합을 출력하는 print_sum 함수를 정의하라.
num1,num2=0,0
def print_sum(num1,num2):
    hab = num1+num2
    return hab

print('Ex8. 정답')
n1=3 #int(input('숫자를 입력하시요>>>'))
n2=4 #int(input('숫자를 입력하시요>>>'))
print(print_sum(n1,n2))
print('-'*50)

# 문9. 두 개의 숫자를 입력받아 합/차/곱/나눗셈을 출력하는
# print_arithmetic_operation 함수를 작성하라.

a,b=0,0
def print_arithmetic_operation(a,b):
    hab = a+b
    cha = a-b
    gob = a*b
    div = a/b
    return hab,cha,gob,div

print('Ex9. 정답')
n3=3 #int(input('숫자를 입력하시요>>>'))
n4=4 #int(input('숫자를 입력하시요>>>'))
dab = print_arithmetic_operation(n3,n4)
print(f'{n3}+{n4}={dab[0]}')
print(f'{n3}-{n4}={dab[1]}')
print(f'{n3}x{n4}={dab[2]}')
print(f'{n3}/{n4}={dab[3]}')
print('-'*50)

# 문10.세 개의 숫자를 입력받아 가장 큰수를 출력하는 print_max 함수를 정의하라.
# 단 if 문을 사용해서 수를 비교하라.
def print_max(i,j,k):
    max_val = 0
    if i>max_val:
        max_val =i
    if j>max_val:
        max_val = j
    if k>max_val:
        max_val = k

    return max_val

n5=int(input('숫자를 입력하시요>>>'))
n6=int(input('숫자를 입력하시요>>>'))
n7=int(input('숫자를 입력하시요>>>'))
maxVal = print_max(n5,n6,n7)
print('Ex10. 정답')
print(f'숫자 {n5},{n6},{n7} 중 큰 수는 {maxVal}이다.')
print('-'*50)
