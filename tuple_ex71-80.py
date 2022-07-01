# python tuple ex71~80
# 파이썬 튜플은 순서가 있지만 수정 불가능한 자료구조입니다.

# 문1. my_variable 이름의 비어있는 튜플을 만들라.
my_variable =()
print('Ex1. 정답')
print(type(my_variable))
print('-'*50)

# 문2. 2016년 11월 영화 예매 순위 기준 top3는 다음과 같다.
# 영화 제목을 movie_rank 이름의 튜플에 저장하라. (순위 정보는 저장하지 않는다.)
# 순위	영화
# 1	닥터 스트레인지
# 2	스플릿
# 3	럭키

movie_rank = ('닥터 스트레인지','스플릿', '럭키')

print('Ex2. 정답')
print(movie_rank)
print('-'*50)

# 문3. 숫자 1 이 저장된 튜플을 생성하라.
# 아래와 같이 괄호와 함께 하나의 정숫값을 저장하면 튜플이 정의 될 것같지만 그렇지 않습니다.
# type()을 출력해보면 파이썬은 튜플이 아닌 정수로 인식합니다.
# >> my_tuple = (1)
# >> type (my_tuple)
# int
# 하나의 데이터가 저장되는 경우, 아래와 같이 쉼표를 입력해만 합니다.
# my_tuple = (1, )

my_num=(1,)
print('Ex3. 정답')
print(my_num)
print('-'*50)

# 문4. 다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.
#
# >> t = (1, 2, 3)
# >> t[0] = 'a'
# Traceback (most recent call last):
#   File "<pyshell#46>", line 1, in <module>
#     t[0] = 'a'
# TypeError: 'tuple' object does not support item assignment

print('Ex4. 정답')
print('tuple은 원소(element)의 값을 변경할 수 없습니다. ')
print('-'*50)












