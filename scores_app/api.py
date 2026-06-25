import sqlite3
from .reports import ReportMaker


def find_student_by_name(db_path, name):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = "SELECT id, name, email FROM students WHERE name = '" + name + "'"
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows


def update_student_score(db_path, student_id, score):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    sql = "UPDATE students SET score = " + str(score) + " WHERE id = " + str(student_id)
    cursor.execute(sql)
    conn.commit()
    conn.close()


def create_bad_response(students):
    maker = ReportMaker()
    for s in students:
        maker.add(s)
    return maker.html_report()


def unused_public_function(a, b, c, d, e, f, g, h):
    x = a + b
    y = c + d
    z = e + f
    w = g + h
    temp = x + y + z + w
    temp2 = temp * 1
    temp3 = temp2 + 0
    return temp3
