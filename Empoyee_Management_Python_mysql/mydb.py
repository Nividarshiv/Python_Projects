import mysql.connector

class Database:
    def __init__(self,db):
        self.mydb=mysql.connector.connect(host='localhost',user='root',password='*********',database=db)
        print(self.mydb)
        self.cur=self.mydb.cursor()
        sql='''
          CREATE TABLE IF NOT EXISTS employee(
          id int Primary Key AUTO_INCREMENT,
          name varchar(25),
          age int,
          doj varchar(15),
          email varchar(25),
          gender varchar(7),
          contact varchar(13),
          address varchar(50)
          )'''
        self.cur.execute(sql)
        self.mydb.commit()

    def insert(self,name,age,dob,email,gender,contact,address):
        insert="INSERT INTO employee(name,age,doj,email,gender,contact,address) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        data=(name,age,dob,email,gender,contact,address)
        self.cur.execute(insert,data)   
        self.mydb.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM EMPLOYEE")
        record=self.cur.fetchall()
        return record
    
    def remove(self,id):
        self.cur.execute("DELETE FROM employee WHERE id=%s",(id,))
        self.mydb.commit()

    def update(self,name,age,dob,email,gender,contact,address,id):
        update="UPDATE employee SET name=%s,age=%s,doj=%s,email=%s,gender=%s,contact=%s,address=%s WHERE id=%s"
        toupdate=(name,age,dob,email,gender,contact,address,id)
        self.cur.execute(update,toupdate)
        self.mydb.commit()
