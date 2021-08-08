import sqlite3
def MyApp():

    myname=input('Name : ')
    
    conn = None
    try:
        print("connecting... 🛰🛰🛰 ")
        conn = sqlite3.connect('xyz.db')
        print(" connected 😎 ")
    except Error as e:
        print(" ❌😜 "+ e)

    cur = conn.cursor()
        
    sql = "SELECT * FROM MyData WHERE name LIKE '%"+myname+"%'"

    cur.execute(sql)

    rows = cur.fetchall()

    if len(rows)==0:
        print("Data Not Found  🙄 ")
    else:
        for row in rows:
            print('''\nName : '''+row[0]+'''\nEmail : '''+row[1]+'''\nPhone Number : '''+str(row[2])+'''
Age : '''+str(row[3])+'''\nDate of birth : '''+str(row[4])+'''\n''')

    conn.commit()
MyApp()
