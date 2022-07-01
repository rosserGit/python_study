# python function 201~210

# 문1. "비트코인" 문자열을 화면에 출력하는 print_coin() 함수를 정의하라.
def print_coin():
    print('"비트코인"')

print('Ex1 정답')
print_coin()
print("-"*50)

# 문2. 1번에서 정의한 함수를 호출하라.
print('Ex2 정답')
print_coin()
print("-"*50)

# 문3. 1번에서 정의한 print_coin 함수를 100번호출하라.
print('Ex3 정답')
for i in range(100):
    print(i + 1, end=" ")
    print_coin()

print("-"*50)

# 문4. "비트코인" 문자열을 100번 화면에 출력하는 print_coins() 함수를 정의하라.
print('Ex4 정답')
def print_coins():
    for j in range(100):
        print(j+1,end=' ')
        print("'비트코인'")

print_coins()
print("-"*50)


# 문5. 아래의 에러가 발생하는 이유에 대해 설명하라.
#
# hello()
# def hello():
#     print("Hi")
# 실행 예
#
# NameError: name 'hello' is not defined
print('Ex5 정답')
print('NameError: name "hello" is not defined')
print('error이유는 def hello() 앞에서 함수가 호출됐기 때문')
print("-"*50)

# 문6. 아래 코드의 실행 결과를 예측하라.
#
# def message() :
#     print("A")
#     print("B")
#
# message()
# print("C")
# message()
print('Ex6 정답')
print("A, B, C, A, B 가 한 라인씩 출력")
print("-"*50)

# 문7. 아래 코드의 실행 결과를 예측하라. (읽기 어려운 코드의 예입니다.)
#
# print("A")
#
# def message() :
#     print("B")
#
# print("C")
# message()
print('Ex7 정답')
print("A, C, B 가 한 라인씩 출력")
print("-"*50)


# 문8.아래 코드의 실행 결과를 예측하라. (읽기 어려운 코드의 예입니다.)
#
# print("A")
# def message1() :
#     print("B")
# print("C")
# def message2() :
#     print("D")
# message1()
# print("E")
# message2()
print('Ex8 정답')
print("A, C, B, E, D 가 한 라인씩 출력")
print("-"*50)

# 문9. 아래 코드의 실행 결과를 예측하라.
#
# def message1():
#     print("A")
#
# def message2():
#     print("B")
#     message1()
#
# message2()
print('Ex9 정답')
print("B,A 가 한 라인씩 출력")
print("-"*50)

# 문10. 아래 코드의 실행 결과를 예측하라.
#
# def message1():
#     print("A")
#
# def message2():
#     print("B")
#
# def message3():
#     for i in range (3) :
#         message2()
#         print("C")
#     message1()
#
# message3()
print('Ex10 정답')
print("B,C,B,C,B,C,A 가 한 라인씩 출력")
print("-"*50)





