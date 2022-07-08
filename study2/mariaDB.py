import time
import sqlite3
import pymysql
import datetime

now = datetime.datetime.now()
config={
    'host' : hostnum,
    'user' : root,
    'password' : pwnum,
    'database' : 'dbwork',
    'port' : portnum,
    'charset' : 'utf8'
}

def dbConnect():
    CN = pymysql.connect(**config)
    cursor = CN.cursor()
    print('Connect : ', now.strftime('%Y-%m-%d %H:%M:%S'))
    print()

    sql = '''
    create table if not exists goods(
     code integer primary key,
     name text(20) not null,
     su integer default 0,
     dan real default 0.0
    );
    '''
    cursor.execute(sql)
    CN.commit()

    return CN,cursor

CN,CS = dbConnect()
def dbInsert():  # 저장처리

    print(f"{'* 1.신규등록 ':-<100}")
    ucode = int(input('code 입력>>> '))

    msg = f"select * from goods as code where code = '{ucode}'"
    CS.execute(msg)
    rows = CS.fetchall()

    if rows:
        print()
        print(f'{ucode} 동일한 code가 있어 신규등록 할 수 없습니다.')

    else:
        name = input('상품명 입력>>> ')
        su = input('su 입력>>> ')
        dan = input('dan 입력>>> ')
        msg = f"insert into goods values ({ucode},'{name}',{su},{dan})"
        CS.execute(msg)
        CN.commit()
        print(f'{ucode} 데이터 저장 성공')



def dbSelect():  # 전체출력
    #CN, CS = dbConnect()
    # print(f"{'* 2.데이터 출력 ':-<100}")
    time.sleep(1)
    msg = f"select * from goods order by code asc"
    CS.execute(msg)
    rows = CS.fetchall()

    if rows:
        print()
        print(f"{' 전체 데이터 출력 ':=^100}")
        print(f'코드\t  이름\t  수량\t   금액\t')
        for row in rows:
            print(f'{row[0]}\t  {row[1]}\t  {row[2]}\t   {row[3]}')
        print(f'goods 상품 총 등록 데이터 : {len(rows)}')
    else:
        print()
        print('데이터가 없습니다.')

def dbSherchName():
    #CN,CS = dbConnect()
    print(f"{'* 5.상품 검색 ':-<100}")
    sherch = input('검색 상품명 입력>>> ')

    msg = f"select * from goods where name like '%{sherch}%'"
    CS.execute(msg)
    rows =CS.fetchall()
    print()

    if rows:
        print(f"{'검색 데이터 출력':=^100}")
        print(f'코드\t  이름\t  수량\t   금액\t')
        for row in rows:
            print(f'{row[0]}\t  {row[1]}\t  {row[2]}\t   {row[3]}')
        print(f'goods 상품 총 등록 데이터 : {len(rows)}')
    else:
        print(f'{sherch} 해당 데이터가 없습니다.')



def dbUpdate():
    #CN,CS = dbConnect()
    print(f"{'* 4.수정 ':-<100}")
    uCode = input('수정 상품 코드>>> ')

    msg = f"select * from goods where code = '{uCode}'"
    CS.execute(msg)
    rows = CS.fetchall()

    if rows:
        name = input('상품명 입력>>> ')
        su = input('su 입력>>> ')
        dan = input('dan 입력>>> ')
        msg = f"update goods set name = '{name}',su = '{su}',dan ='{dan}' where code = '{uCode}'"
        CS.execute(msg)
        CN.commit()
        print(f"수정 전 데이터 : {rows}")
        print(f'{uCode} 데이터 저장 성공!')
    else:
        print()
        print(f'{uCode} 해당 데이터가 없습니다.')



def dbDelete():
    #CN, CS = dbConnect()
    print(f"{'* 3.삭제 ':-<100}")
    delData = input('삭제 코드 입력>>> ')

    msg = f"select * from goods where code = '{delData}'"
    CS.execute(msg)
    rows = CS.fetchall()
    print()

    if rows:
        msg=f"delete from goods where code ='{delData}'"
        CS.execute(msg)
        CN.commit()
        print(f'{delData} 데이터 삭제 성공!')
    else:
        print(f'{delData} 해당 데이터가 없습니다.')



dbSelect()
print('- ' * 50)
while True:
    print()
    print(f'{" 프로그램 시작 ":*^100}')
    print('1.신규 등록  2.전체 출력  3.삭제  4.수정  5.상품 검색  9.프로그램 종료!')
    sel = int(input('번호 선택 >>> '))
    if sel == 9:
        print('프로그램을 종료합니다')
        print()
        break

    if sel == 1:
        dbInsert()
    elif sel == 2:
        dbSelect()
    elif sel == 3:
        dbDelete()
    elif sel == 4:
        dbUpdate()
    elif sel == 5:
        dbSherchName()
    else:
        print(f'{sel} 번호를 잘못 입력 했습니다. 다시 입력 하세요.')
        print()
CS.close()
CN.close()
