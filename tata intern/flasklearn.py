from flask import Flask, render_template, request, redirect
import pymysql

studentdb = Flask(__name__)

def connection():
    s = 'localhost' 
    d = 'studentdb' 
    u = 'root' # Your login user
    p = 'Sidarth@63' # Your login password
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

@studentdb.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form.get("name")
        rollno = request.form.get("rollno")
        clas = request.form.get("class")
        section = request.form.get("section")
        class_teacher = request.form.get("class_teacher")
        GPA = request.form.get("GPA")
        Fee_status = request.form.get("Fee_status")

        cursor.execute('INSERT INTO stud (name, rollno, CLASS, SECTION, CLASS_TEACH, GPA, FEE) VALUES (%s, %s, %s, %s, %s, %s, %s)', (name, rollno, clas, section, class_teacher, GPA, Fee_status))
        conn.commit()
    return render_template("add.html")

@studentdb.route("/delete", methods=["GET", "POST"])
def delete():
    message = None

    if request.method == "POST":
        criteria = request.form.get("criteria")
        value = request.form.get("value")

        if criteria == "name":
            cursor.execute('DELETE FROM stud WHERE name=%s;', (value,))
        elif criteria == "rollno":
            cursor.execute('DELETE FROM stud WHERE rollno=%s;', (value,))

        conn.commit()

        if cursor.rowcount == 0:
            message = f"No records found with {criteria} '{value}'."
        else:
            message = f"Deleted records with {criteria} '{value}'."

    return render_template("delete.html", message=message)

@studentdb.route("/sort", methods=["GET", "POST"])
def sort():
    if request.method == "POST":
        sort_order = request.form.get("sort")
        if sort_order == "ascending":
            cursor.execute("SELECT * FROM stud ORDER BY name ASC;")
        elif sort_order == "descending":
            cursor.execute("SELECT * FROM stud ORDER BY name DESC;")
        sorted_stu = []
        for row in cursor:
            sorted_stu.append({
                "name": row[0],
                "Rollno": row[1],
                "class": row[2],
                "section": row[3],
                "classteacher": row[4],
                "GPA": row[5],
                "Fee_status": row[6]
            })
        return render_template("sort_results.html", sorted_stu=sorted_stu)
    return render_template("sort.html")

@studentdb.route("/filter", methods=["GET", "POST"])
def filter():
    if request.method == "POST":
        criteria = request.form.get("criteria")
        value = request.form.get("value")

        try:
            if criteria == "class_section":
                class_name, section = value.split('_')
                cursor.execute("SELECT * FROM stud WHERE CLASS=%s AND SECTION=%s", (class_name, section))
            elif criteria == "above_gpa":
                cursor.execute("SELECT * FROM stud WHERE GPA >= %s", value)
            elif criteria == "below_gpa":
                cursor.execute("SELECT * FROM stud WHERE GPA < %s", value)
            elif criteria == "fee_paid":
                cursor.execute("SELECT * FROM stud WHERE Fee_status = 'Paid'")
            elif criteria == "fee_not_paid":
                cursor.execute("SELECT * FROM stud WHERE Fee_status = 'Not Paid'")

            filtered_stu = []
            for row in cursor:
                filtered_stu.append({
                    "name": row[0],
                    "Rollno": row[1],
                    "class": row[2],
                    "section": row[3],
                    "classteacher": row[4],
                    "GPA": row[5],
                    "Fee_status": row[6]
                })

            return render_template("filter_results.html", filtered_stu=filtered_stu)

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return render_template("filter_error.html", error_message=error_message)

    return render_template("filter.html")

@studentdb.route('/update', methods=['GET','POST'])
def update_student():
    if request.method=="POST":
        rollno=request.form['rollno']
        criteria = request.form.get("criteria")
        value = request.form.get("value")
        
        try:
            if criteria == "gpa":
                 
                cursor.execute("UPDATE stud SET GPA=%s where rollno=%s", (value, rollno))
            elif criteria == "Fee_status":
                cursor.execute("UPDATE stud SET FEE=%s where rollno=%s", (value,rollno))
            conn.commit()
            
            return redirect('/')
        
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return render_template("update_error.html", error_message=error_message)
        
    else:
        return render_template('update.html')


if __name__ == "__main__":
    studentdb.run()
