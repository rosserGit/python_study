# python string ex21~30
# 파이썬 문자열은 인덱싱, 슬라이싱 기능과 다양한 메서드를 제공합니다.

# 문1. 문자열 인덱싱
# letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
# >> letters = 'python'
# 실행 예 : p t

letters = 'python'
print('Ex1. 정답')
print(letters[0],letters[2],sep='\t')
print('-'*50)

# 문2. 문자열 슬라이싱
# 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
# >> license_plate = "24가 2210"
# 실행 예: 2210

license_plate = "24가 2210"
print('Ex2. 정답')
print(license_plate[4:])
print(license_plate[-4:])
print('-'*50)

# 문3. 문자열 인덱싱
# 아래의 문자열에서 '홀' 만 출력하세요.
# >> string = "홀짝홀짝홀짝"
# 실행 예: 홀홀홀

string = "홀짝홀짝홀짝"
print('Ex3. 정답')
print('슬라이싱할 때 시작인덱스:끝인덱스:오프셋을 지정할 수 있습니다.')
print(string[::2])

# 문4. 문자열 슬라이싱
# 문자열을 거꾸로 뒤집어 출력하세요.
# >> string = "PYTHON"
# 실행 예: NOHTYP

string1 = "PYTHON"
print('Ex4. 정답')
print(string1[::-1])
print('-'*50)

# 문5. 문자열 치환
# 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
#----------------------------------------------------------------
# 파이썬 문자열에서 replace 메서드를 사용하면 문자열을 일부를 치환할 수 있습니다.
# 문자열은 수정할 수 없는 자료형이므로 기존 문자열은 그대로 두고 치환된
# 새로운 문자열이 리턴됩니다.
#----------------------------------------------------------------
# >> phone_number = "010-1111-2222"
# 실행 예 010 1111 2222

phone_number = "010-1111-2222"
phone_number1 = phone_number.replace('-',' ')

print('Ex5. 정답')
print('원본:',phone_number)
print('replace로 "-"를 공백을 치환')
print(phone_number1)
print('-'*50)

# 문6. 문자열 다루기
# 5번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
# 실행 예: 01011112222

phone_number2=phone_number.replace('-','')
print('Ex6. 정답')
print(phone_number2)
print('-'*50)

# 문7. 문자열 다루기
# url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
#----------------------------------------------------------
# 문자열로 표현된 url에서 .을 기준으로 분리합니다.
# 분리된 url 중 마지막을 인덱싱하면 도메인만 출력할 수 있습니다.
#----------------------------------------------------------
# >> url = "http://sharebook.kr"
# 실행 예: kr

url = "http://sharebook.kr"
url_split = url.split('.')
print('Ex7. 정답')
print(url[-2::1])
print(url_split[-1])
print('-'*50)

# 문8. 문자열은 immutable
# 아래 코드의 실행 결과를 예상해보세요.
#
# >> lang = 'python'
# >> lang[0] = 'P'
# >> print(lang)


print('Ex8. 정답')
print("문자열은 수정할 수 없습니다. 실행 결과를 확인해보면 문자열이 할당(assignment) 메서드를 지원하지 않음을 알 수 있습니다.")
print('-'*50)

# 문9. replace 메서드
# 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
# >> string = 'abcdfe2a354a32a'
# 실행 예: Abcdfe2A354A32A
string = 'abcdfe2a354a32a'
print('Ex9. 정답')
print(string)
print(string.upper())
print('-'*50)


# 문10. replace 메서드
# 아래 코드의 실행 결과를 예상해보세요.
string = 'abcd'
string.replace('b', 'B')
print(string)
# abcd가 그대로 출력됩니다.
# 왜냐하면 문자열은 변경할 수 없는 자료형이기 때문입니다.
# replace 메서드를 사용하면 원본은 그대로 둔채로 변경된 새로운 문자열 객체를 리턴해줍니다.
print('Ex10. 정답')
print('문자열은 바뀌지 않음')
print(string.replace('b', 'B'))
print('-'*50)


print(f'{" $ ":=^50}') # 50만큼 공간에 중간값을 $ 로 하고 빈공간을 =로 채움.
print(f'{"$ ":=<50}') # 50만큼 공간에 왼쪽값을 $ 로 하고 빈공간을 =로 채움.
print(f'{" $":=>50}') # 50만큼 공간에 오른쪽값을 $ 로 하고 빈공간을 =로 채움.






