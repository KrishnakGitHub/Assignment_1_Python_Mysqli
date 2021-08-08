import sqlite3

def MyApp():

    my_name = input("Name : ")
    my_email = input("Email : ")
    my_phone_number = input("Phone Number : ")
    my_age = input("age : ")
    my_date_of_birth = input("Date of birth : ")

    conn = None
    try:
        print("connecting... 🛰🛰🛰 ")
        conn = sqlite3.connect('xyz.db')
        print(" :) connected 😎 ")
    except Error as e:
        print(" :(  ❌😜 "+ e)

    cur = conn.cursor()
    cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='MyData' ''')
    #if the count is 1, then table exists
    if cur.fetchone()[0]==1:
        print('Table exists.')
    else:
        cur.execute("CREATE TABLE MyData (course_title TEXT, author TEXT, course_rating FLOAT, course_price FLOAT)")
        print(":)...  Table is created")

    sql = '''INSERT INTO MyData (name, email, phone_number, age, date_of_birth)
            VALUES(?, ?, ?, ?, ?)'''
    val = (my_name, my_email, my_phone_number, my_age, my_date_of_birth)
   
    cur.execute(sql,val)

    print('Detail Inserted  😎 ')

    sql1= "SELECT * FROM MyData"

    cur.execute(sql1)

    rows = cur.fetchall()

    for row in rows:
        print(row)
    
    conn.commit()
MyApp()
