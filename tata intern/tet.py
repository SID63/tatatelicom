# Importing module
import mysql.connector

# Creating connection object
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "Sidarth@63",
    database = 'studentdb'
)

cursor = mydb.cursor()
 
# Creating a table called 'gfg' in the
# 'geeksforgeeks' database
#cursor.execute("CREATE TABLE stud (name VARCHAR(25) NOT NULL,  rollno VARCHAR(25) NOT NULL, CLASS VARCHAR(4) NOT NULL, SECTION CHAR(1) NOT NULL,CLASS_TEACH VARCHAR(25) NOT NULL,GPA FLOAT(3) CHECK (GPA<=5) NOT NULL,FEE CHAR(10) NOT NULL)")

cursor.execute('INSERT INTO stud (name, rollno, CLASS, SECTION, CLASS_TEACH, GPA, FEE) VALUES ("SANDY", "cb.en.u4cce21062", "CCE", "A", "Karthik", 4, "NOTPAID"),("JOHN","cb.en.u4cce21063","CSE","B","Ravi",3,"PAID"),("MARY","cb.en.u4cce21064","ECE","C","Suresh",2,"NOTPAID"),("ALEX","cb.en.u4cce21065","IT","D","Shankar",1,"PAID")')


def print_table():
    row=cursor.fetchall()
    for row in row:
        print(row)


def sort_by_name():
    cursor.execute('SELECT * from stud order by name')
    print_table()

def sort_by_rollno():
    cursor.execute('SELECT * from stud order by rollno')
    print_table()

def sort_by_gpa():
    cursor.execute('SELECT * from stud order by gpa')
    print_table()

def sort_by_section():
    cursor.execute('SELECT * from stud order by class,section')
    print_table()

def search_by_rollno(num):
    cursor.execute('select * from stud where rollno = num')
    rows = cursor.fetchall()
    print(rows)

def update_by_rollno(rollno):
    new_gpa=int(input())
    cursor.execute("update stud SET gpa=new_gpa where rollno=rollno")

def filter_above_gpa(v_gpa):
    cursor.execute("select * from stud where gpa>v_gpa")
    print_table()

def filter_below_gpa(v_gpa):
    cursor.execute("select * from stud where gpa<=v_gpa")
    print_table()

def filter_by_paid():
    cursor.execute("select * from stud where fee LIKE '%PAID%'")
    print_table()

def filter_by_not_paid():
    cursor.execute("select * from stud where fee LIKE '%NOTPAID%'")
    print_table()

filter_by_not_paid()