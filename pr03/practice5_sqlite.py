import sqlite3

# 데이터 베이스 연결하기
con = sqlite3.connect("practice.db")
cur = con.cursor()

# 테이블 생성하기
cur.execute("""
    create table if not exists person(
        id integer primary key autoincrement,
        name text not null,
        age integer not null)
""")
# if not exists: 를 붙이면 해당 테이블이 이미 존재한다면
# 테이블을 더 이상 생성하지 않는다
# -> 오류 방지

# 값 추가하기 (insert)
# cur.execute("insert into person(name, age) values (?, ?)", ("gaeun", 18))
# name = "eunbb" ; age = 22
# cur.execute(f'insert into person(name, age) values ("{name}", {age})')
# con.commit()

# # 값 확인하기 (select)
# cur.execute("select * from person")
# rows = cur.fetchall()
# # rows 의 타입: list
# print(type(rows))
# for row in rows:
#     print(row)

# # 값 수정하기 (update)
# query = "update person set name = :name, age = :age where id = :id"
# param = {"id": 2, "name": "gyul", "age": 16}
# cur.execute(query, param)
# con.commit()

cur.execute("delete from person where name = :name", {"name": "gyul"})
con.commit()