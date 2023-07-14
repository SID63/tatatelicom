def print_table():
    row=cursor.fetchall()
    for row in row:
        print(row)