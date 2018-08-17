import sqlite3
c = 'y'
conn = sqlite3.connect('test.db')
conn.execute("create table if not exists Bot(Query text,Answer text)")

while(c == 'y' or c=='Y' ) :
    conn.execute("insert into Bot(Query,Answer) values(?,?)",(input(),input()))
    conn.commit()
    print("Do you want continue:(y/n)")
    c=input()

