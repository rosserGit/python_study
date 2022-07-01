# python variable 문제 풀기 10문제
# 변수variable은  자주 사용되는 값을 바인딩 합니다.

# Ex1.변수 사용하기
# 삼성전자라는 변수로 50,000원을 바인딩해보세요. 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.

samsung = 50000
stock = 10
total = samsung * stock
print('Ex1 정답')
print('Total valuation Amount : ',total,'원',sep='')
print('='*50)

# Ex2.변수 사용하기
# 다음 표는 삼성전자의 일부 투자정보입니다. 변수를 사용해서 시가총액, 현재가, PER 등을 바인딩해보세요.
#
# 항목   	값
# 시가총액	298조
# 현재가     50,000원
# PER	    15.79

total_val = 2980000000000000
pre_val = 50000
per = 15.79
print('Ex2 정답')
print(total_val,type(total_val))
print(pre_val, type(pre_val))
print(per,type(per))
print('='*50)

# Ex3. 문자열 출력
# 변수 s와 t에는 각각 문자열이 바인딩 되어있습니다.
# >> s = "hello"
# >> t = "python"
# 두 변수를 이용하여 아래와 같이 출력해보세요.
# 실행 예: # hello! python
print('Ex3 정답')
s = "hello"
t = "python"
print(s+"!",t)
print('='*50)

# Ex4. 파이썬을 이용한 값 계산
# 아래 코드의 실행 결과를 예상해보세요.
# 2 + 2 * 3

print('Ex4 정답')
print('2*3을 먼저 계산하고 2를 더함. 답은 8')
print(2 + 2 * 3 )
print('='*50)

#Ex5.type 함수
# type() 함수는 데이터 타입을 판별합니다.
# 변수 a에는 128 숫자가 바인딩 돼 있어 type 함수가 int (정수)형임을 알려줍니다.
# a = 128
# print (type(a))
# <class 'int'>
# 아래 변수에 바인딩된 값의 타입을 판별해보세요.

a = "132"

print('Ex5 정답')
print('a = "132"는 문자열"str"로 나옴.')
print(type(a))
print('='*50)


# Ex6. 문자열을 정수로 변환
# 문자열 '720'를 정수형으로 변환해보세요.

num_str = "720"
num_int = int(num_str)
print('Ex6 정답')
print(num_str,type(num_str))
print('int(num_str)해서 형변환 함.')
print(num_int,type(num_int))
print('='*50)

# Ex7. 정수를 문자열 100으로 변환
# 정수 100을 문자열 '100'으로 변환해보세요.
num = 100
str = str(num)

print('Ex7 정답')
print(num,type(num))
print('str(num)해서 형변환 함.')
print(str,type(str))
print('='*50)

# Ex8. 문자열을 실수로 변환
# 문자열 "15.79"를 실수(float) 타입으로 변환해보세요.

str = "15.79"
flt = float(str)
print('Ex8 정답')
print(str,type(str))
print('float(str)해서 형변환 함.')
print(flt,type(flt))
print('='*50)

# Ex9. 문자열을 정수로 변환
# year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다.
# 이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.

year = "2020"
year = int(year)

print('Ex9 정답')
print('int(year)해서 형변환 함.')
print(year,'년\t',type(year),sep='')
print(year-1,'년',sep='')
print(year-2,'년',sep='')
print(year-3,'년',sep='')
print('='*50)


# Ex10. 파이썬 계산
# 에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다.
# 총 금액은 계산한 후 이를 화면에 출력해보세요. (변수사용하기)

mon = 48548
m_div = 36
total = mon * m_div
print('Ex10 정답')
print('총금액 : ',total,'원',sep='')
print('='*50)










