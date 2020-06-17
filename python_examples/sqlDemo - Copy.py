import sqlite3

try:
    try:
        print("merhaba1")
        baglanti = sqlite3.connect('databases\chinook.db')
        print("merhaba2")
        c = baglanti.cursor()
        print("merhaba3")
    except ConnectionError as err:
        print(err)    
        
    print("merhaba4")
    command = c.execute("select * from customers")

    for satir in command:
        print(satir)
finally:
    c.close()

        


