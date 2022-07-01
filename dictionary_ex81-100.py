# python dictionary 081~100
# 파이썬 딕셔너리는 순서는 없지만 key와 value 형태로 데이터를 저장합니다.
# 특히 key는 데이터의 레이블(label)을 지정하는 용도로 자주 사용됩니다.

# 별 표현식
# 기본적으로 데이터 언패킹은 좌변의 변수와 우변 데이터 개수가 같아야 합니다.
# 하지만 star expression을 사용하면 변수의 개수가 달라도 데이터 언패킹을 할 수 있습니다.
# 튜플에 저장된 데이터 중에서 앞에 있는 두 개의 데이터만 필요할 경우 나머지 데이터의 언패킹
# 코드를 작성할 필요가 없습니다.
#
# >> a, b, *c = (0, 1, 2, 3, 4, 5)
# >> a
# 0
# >> b
# 1
# >> c
# [2, 3, 4, 5]
#===================================================================================

# 문1. 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여
# 좌측 8개의 값을 valid_score 변수에 바인딩하여라.

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, a, b=scores
print('Ex1. 정답')
print('좌측 8개의 값 :',valid_score)
print(a)
print(b)
print('-'*50)

# 문2. 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을
# 사용하여 우측 8개의 값을 valid_score 변수에 바인딩하여라.

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
c,d,*valid_score1= scores
print('Ex2. 정답')
print(c)
print(d)
print('우측 8개의 값 :',valid_score1)
print('-'*50)

# 문3. 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을
# 사용하여 가운데 있는 8개의 값을 valid_score 변수에 바인딩하여라.

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
e,*valid_score2,f = scores

print('Ex3. 정답')
print(e)
print('가운데 8개의 값 :',valid_score2)
print(f)
print('-'*50)

# 문4. 비어있는 딕셔너리
# temp 이름의 비어있는 딕셔너리를 만들라.
temp={ }
print('Ex4. 정답')
print(temp)
print('-'*50)

# 문5. 다음 아이스크림 이름과 희망 가격을 딕셔너리로 구성하라.
#
# 이름	희망가격
# 메로나	1000
# 폴라포	1200
# 빵빠레	1800

ice_cream ={"메로나":1000,"폴라포":1200,"빵빠레":1800}
print('Ex5. 정답')
print(ice_cream)
print('-'*50)

# 문6. 5번의 딕셔너리에 아래 아이스크림 가격정보를 추가하라.
#
#이름	희망 가격
#죠스바	1200
#월드콘	1500

ice_cream ={"메로나":1000,"폴라포":1200,"빵빠레":1800}
ice_cream['죠스바'] =1200
ice_cream['월드콘'] =1500
print('Ex6. 정답')
print(ice_cream)
print('-'*50)

# 문7. 다음 딕셔너리를 사용하여 메로나 가격을 출력하라.
#
# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}
# 실행 예:
# 메로나 가격: 1000

#ice_cream ={"메로나":1000,"폴라포":1200,"빵빠레":1800,'죠스바': 1200, '월드콘': 1500}
print('Ex7. 정답')
print('메로나 가격 : ',ice_cream['메로나'],'원',sep='')
print('-'*50)

# 문8. 다음 딕셔너리에서 메로나의 가격을 1300으로 수정하라.
#
# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}

#ice_cream ={"메로나":1000,"폴라포":1200,"빵빠레":1800,'죠스바': 1200, '월드콘': 1500}
print('Ex8. 정답')
ice_cream['메로나'] =1300
print('메로나 가격 : ',ice_cream['메로나'],'원',sep='')
print('-'*50)

# 문9. 다음 딕셔너리에서 메로나를 삭제하라.
#ice_cream ={"메로나":1000,"폴라포":1200,"빵빠레":1800,'죠스바': 1200, '월드콘': 1500}
print('Ex9. 정답')
del ice_cream['메로나']
print(ice_cream)
print('-'*50)

# 문10. 다음 코드에서 에러가 발생한 원인을 설명하라.
#
# >> icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# >> icecream['누가바']
# Traceback (most recent call last):
#   File "<pyshell#69>", line 1, in <module>
#     icecream['누가바']
# KeyError: '누가바'

print('Ex10. 정답')
print('ice_cream dictionary에는 누가바가 없음. ')
print('딕셔너리에 없는 키를 사용해서 인덱싱하면 에러가 발생. ')
print('-'*50)

# 문11. 딕셔너리 생성
# 아래의 표에서, 아이스크림 이름을 키값으로, (가격, 재고) 리스트를 딕셔너리의 값으로
# 저장하라. 딕셔너리의 이름은 inventory로 한다.
#
# 이름	가격	재고
# 메로나	300	20
# 비비빅	400	3
# 죠스바	250	100

inventory = {'메로나':[300,20], '비비빅':[400,3], '죠스바':[250,100]}
print('Ex11. 정답')
print(inventory)
print('-'*50)

# 문12. 딕셔너리 인덱싱
# inventory 딕셔너리에서 메로나의 가격을 화면에 출력하라.

print('Ex12. 정답')
print(inventory['메로나'][0],'원',sep='')
print('-'*50)

# 문13.딕셔너리 인덱싱
# inventory 딕셔너리에서 메로나의 재고를 화면에 출력하라.

print('Ex13. 정답')
print(inventory['메로나'][1],'개',sep='')
print('-'*50)

# 문14. 딕셔너리 추가
# inventory 딕셔너리에 아래 데이터를 추가하라.
# 이름	가격	재고
# 월드콘	500	7
# 실행 예시:
# >> print(inventory)
# {'메로나': [300, 20], '비비빅': [400, 3], '죠스바': [250, 100], '월드콘': [500, 7]}

inventory['월드콘'] = [500,7]
print('Ex14. 정답')
print(inventory)
print('-'*50)

# 문15. 딕셔너리 keys() 메서드
# 다음의 딕셔너리로부터 key 값으로만 구성된 리스트를 생성하라.
#
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice = list(icecream.keys())

print('Ex15. 정답')
print(ice)
print('-'*50)

# 문16. 딕셔너리 values() 메서드
# 다음의 딕셔너리에서 values 값으로만 구성된 리스트를 생성하라.
ice_val = list(icecream.values())
print('Ex16. 정답')
print(ice_val)
print('-'*50)

# 문17. 딕셔너리 values() 메서드
# icecream 딕셔너리에서 아이스크림 판매 금액의 총합을 출력하라.
hap = sum(icecream.values())
print('Ex17. 정답')
print(hap,'원',sep='')
print('-'*50)

# 문18. 딕셔너리 update 메서드
# 아래의 new_product 딕셔너리를 다음 icecream 딕셔너리에 추가하라.
#
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# new_product = {'팥빙수':2700, '아맛나':1000}
# 실행 예시:
# >> print(icecream)
# {'탱크보이': 1200,  '폴라포': 1200,  '빵빠레': 1800,  '월드콘': 1500,  '메로나': 1000,  '팥빙수':2700, '아맛나':1000}

new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print('Ex18. 정답')
print(icecream)
print('-'*50)

# 문19. zip과 dict
# 아래 두 개의 튜플을 하나의 딕셔너리로 변환하라. keys를 키로, vals를 값으로
# result 이름의 딕셔너리로 저장한다.
#
# keys = ("apple", "pear", "peach")
# vals = (300, 250, 400)
# 실행 예시:
# >> print(result)
# {'apple': 300, 'pear': 250, 'peach': 400}

keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys,vals))
print('문19. 정답')
print(result)
print('-'*50)

# 문20. zip과 dict
# date와 close_price 두 개의 리스트를 close_table 이름의 딕셔너리로 생성하라.
#
# date = ['09/05', '09/06', '09/07', '09/08', '09/09']
# close_price = [10500, 10300, 10100, 10800, 11000]
# 실행 예시:
# >> print(close_table)
# {'09/05': 10500, '09/06': 10300, '09/07': 10100, '09/08': 10800, '09/09': 11000}

date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

close_table = dict(zip(date,close_price))
print('문20. 정답')
print(close_table)
print('-'*50)




