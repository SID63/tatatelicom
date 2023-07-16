from flask import Flask, render_template,request
import pymysql

studentdb = Flask(__name__)



def connection():
    s = 'localhost' 
    d = 'studentdb' 
    u = 'root' #Your login user
    p = 'Sidarth@63' #Your login password
    conn = pymysql.connect(host=s, user=u, password=p, database=d)
    return conn



conn = connection()
cursor = conn.cursor()


@studentdb.route("/")
def main():
    cursor.execute("SELECT * FROM stud")
    stu = []
    for row in cursor:
        stu.append({"name": row[0], "Rollno": row[1], "class": row[2], "section": row[3], "classteacher": row[4], "GPA": row[5], "Fee_status": row[6]})
    print(stu)
    return render_template("login.html", stu=stu)

@studentdb.route("/add",methods =["GET", "POST"])
def add():
    if request.method == "POST":
       name = request.form.get("name")
       rollno = request.form.get("rollno")
       clas = request.form.get("class")
       section = request.form.get("section")
       class_teacher = request.form.get("class_teacher")
       GPA = request.form.get("GPA")
       Fee_status = request.form.get("Fee_status")
      
       cursor.execute('INSERT INTO stud (name, rollno, CLASS, SECTION, CLASS_TEACH, GPA, FEE) VALUES (%s, %s, %s, %s, %s, %s, %s)',(name,rollno,clas,section,class_teacher,GPA,Fee_status))
       conn.commit()
    return render_template("add.html")

@studentdb.route("/deletebyname",methods =["GET", "POST"])
def deletebyname():
    if request.method == "POST":
       name = request.form.get("name")
       conn.commit()
       cursor.execute('DELETE FROM stud WHERE name=%s;',name)

    return render_template("deletebyname.html")

@studentdb.route("/sort",methods =["GET", "POST"])
def sort():
    if request.method == "POST":
       sort = request.form.get("sort")
       
       if sort =="accending":
           cursor.execute('ALTER TABLE stud ORDER BY name ASC;')
           

       elif sort =="decending":
           cursor.execute('ALTER TABLE stud ORDER BY name DESC;')
       conn.commit()

    return render_template("sort.html")

@studentdb.route("/filter",methods =["GET", "POST"])
def filter():
    stu=[]
    if request.method == "POST":
       name = request.form.get("name")
       def filt ():
               cursor.execute('SELECT * FROM stud WHERE CLASS_TEACH LIKE %s',name)
               stu = cursor.fetchall()
               conn.commit()
               return render_template("filterclassteacher.html", stu=stu)
       





if(__name__ == "__main__"):
    studentdb.run()