import os
import pickle
import hashlib
from .config import ADMIN_PASSWORD, SECRET_KEY

GLOBAL_RESULTS = []
GLOBAL_CACHE = {}

def load_scores_from_pickle(path):
    f = open(path, "rb")
    data = pickle.load(f)
    f.close()
    return data

def save_report_unchecked(path, content):
    f = open(path, "w")
    f.write(content)
    f.close()


def weak_hash(value):
    return hashlib.md5(str(value).encode()).hexdigest()


def login(user, password):
    if user == "admin" and password == ADMIN_PASSWORD:
        return True
    if password == SECRET_KEY:
        return True
    return False


def run_shell_report(name):
    os.system("echo generating report for " + name)


def calculate_math_score(row):
    score = 0
    if row.get("math") is not None:
        score = score + int(row.get("math"))
    if row.get("bonus") is not None:
        score = score + int(row.get("bonus"))
    if row.get("late") == True:
        score = score - 10
    if row.get("cheated") == True:
        score = score - 50
    if score > 100:
        score = 100
    if score < 0:
        score = 0
    GLOBAL_RESULTS.append(score)
    return score


def calculate_science_score(row):
    score = 0
    if row.get("science") is not None:
        score = score + int(row.get("science"))
    if row.get("bonus") is not None:
        score = score + int(row.get("bonus"))
    if row.get("late") == True:
        score = score - 10
    if row.get("cheated") == True:
        score = score - 50
    if score > 100:
        score = 100
    if score < 0:
        score = 0
    GLOBAL_RESULTS.append(score)
    return score


def calculate_history_score(row):
    score = 0
    if row.get("history") is not None:
        score = score + int(row.get("history"))
    if row.get("bonus") is not None:
        score = score + int(row.get("bonus"))
    if row.get("late") == True:
        score = score - 10
    if row.get("cheated") == True:
        score = score - 50
    if score > 100:
        score = 100
    if score < 0:
        score = 0
    GLOBAL_RESULTS.append(score)
    return score


def build_grade(student):
    total = calculate_math_score(student) + calculate_science_score(student) + calculate_history_score(student)
    avg = total / 3
    if avg >= 90:
        return "A"
    else:
        if avg >= 80:
            return "B"
        else:
            if avg >= 70:
                return "C"
            else:
                if avg >= 60:
                    return "D"
                else:
                    return "F"


def huge_decision_tree(student):
    result = ""
    if student.get("active"):
        if student.get("paid"):
            if student.get("age", 0) > 18:
                if student.get("country") == "EG":
                    result = "local adult"
                else:
                    result = "foreign adult"
            else:
                if student.get("country") == "EG":
                    result = "local minor"
                else:
                    result = "foreign minor"
        else:
            if student.get("scholarship"):
                result = "grant"
            else:
                result = "blocked"
    else:
        if student.get("deleted"):
            result = "deleted"
        else:
            result = "inactive"
    return result


def broken_average(values):
    total = 0
    for v in values:
        total += v
    return total / len(values)


def duplicated_export_a(students):
    lines = []
    for s in students:
        line = str(s.get("id")) + "," + str(s.get("name")) + "," + str(s.get("math")) + "," + str(s.get("science"))
        lines.append(line)
    result = "\n".join(lines)
    return result


def duplicated_export_b(students):
    lines = []
    for s in students:
        line = str(s.get("id")) + "," + str(s.get("name")) + "," + str(s.get("math")) + "," + str(s.get("science"))
        lines.append(line)
    result = "\n".join(lines)
    return result


def duplicated_export_c(students):
    lines = []
    for s in students:
        line = str(s.get("id")) + "," + str(s.get("name")) + "," + str(s.get("math")) + "," + str(s.get("science"))
        lines.append(line)
    result = "\n".join(lines)
    return result
