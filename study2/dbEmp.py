import time
import sqlite3


def dbConnect():
    conn = sqlite3.connect('./data/test.db') # print(conn) #<sqlite3.Connection object at 0x000001E33B92C4E0>
    cursor = conn.cursor()

    sql = 'create table if not exists emp( name text(10), pay text(4), phone text(10) )' #문자열->객체화
    cursor.execute(sql)
    conn.commit()
    print('test.db 데이터 베이스가 생성되었습니다.')
    return conn,cursor



def dbInsert(CN,cursor):
    user = input('이름입력 >>> ')
    b = input('급여입력 >>> ')
    c = input('번호입력 >>> ')

    msg = "insert into emp values( '" + user + "', '" + b + "', '" + c + "')"
    cursor.execute(msg)
    CN.commit()
    print(user , '님 데이터 저장 성공했습니다')
    # cursor.colse()
    # CN.colse()


def dbSelect(_,cursor):
    time.sleep(1)
    cursor.execute("select name, pay, phone from emp  order by name asc ")
    rows = cursor.fetchall()
    print()
    print('-------- 데이터출력 --------')
    print('이름\t 급여\t 번호')
    for row in rows:
        print(row[0] +'\t' + row[1] +'\t' + row[2])
    print('-'*50 )

    # cursor.close()
    # CN.close()


# 전역변수
CN,cursor = dbConnect()
while True:
    print()
    print(f'{" 프로그램 시작 ":*^100}')
    print('1.신규 등록  2.전체 출력  9.프로그램 종료!')
    sel = int(input('번호 선택 >>> '))
    if sel == 9:

        print('프로그램을 종료합니다')
        print()
        break

    if sel == 1:
        dbInsert(CN,cursor)
    elif sel == 2:
        dbSelect(CN,cursor)
    else:
        print(f'{sel} 번호를 잘못 입력 했습니다. 다시 입력 하세요.')
        print()
        break

cursor.close()
CN.close()
