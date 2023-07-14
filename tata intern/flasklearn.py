from flask import Flask, render_template
import pymysql

studentdb = Flask(__name__)


def connection():
    s = 'localhost' 
    d = 'studentdb' 
    u = 'root' #Your login user
    p = 'Sidarth@63' #Your login password
    conn = pymysql.connect(host=s, user=u, password=p, database=d)
    return conn

@studentdb.route("/")
def main():
    stu = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO stud (name, rollno, CLASS, SECTION, CLASS_TEACH, GPA, FEE) VALUES ("SANDY", "cb.en.u4cce21062", "CCE", "A", "Karthik", 4, "NOTPAID"),("JOHN","cb.en.u4cce21063","CSE","B","Ravi",3,"PAID"),("MARY","cb.en.u4cce21064","ECE","C","Suresh",2,"NOTPAID"),("ALEX","cb.en.u4cce21065","IT","D","Shankar",1,"PAID")')
    cursor.execute("SELECT * FROM stud")
    for row in cursor.fetchall():
        stu.append({"name": row[0], "Rollno": row[1], "class": row[2], "section": row[3], "classteacher": row[4], "GPA": row[5], "Fee_status": row[6]})
    conn.close()
    print(stu)
    print(len(stu))
    return render_template("login.html", stu = stu)



if(__name__ == "__main__"):
    studentdb.run()

