# 고객서비스의 부가세를  빠르게 출력하는 간단 프로그램.
# 부가세 10 % 기준
# 소비자 가격 = 물건 가격 X 1.1
# 물건 가격 = 소비자 가격 X 1/1.1
# 부가세 = 물건 가격 X 0.1 = 소비자 가격 X 1/11


pPrice = int(input('소비자 가격(원) : '))
vAnser = input('부가세 포함입니까? (y/n) : ')

if vAnser == 'y' and pPrice > 0:
    pValue = int(input('부가세(%) : '))
    print(f'Total : {round(pPrice +(pPrice * pValue/100))}원')

elif vAnser == 'n' and pPrice > 0:
    print(f'Total : {pPrice}원')

else :
    print('가격 또는 부가세 질문에 잘못 입력 하셨습니다.')
