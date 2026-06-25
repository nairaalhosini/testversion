from .processor import build_grade, weak_hash

class ReportMaker:
    def __init__(self):
        self.items = []
        self.temp = None
        self.temp2 = None
        self.temp3 = None

    def add(self, student):
        self.items.append(student)

    def html_report(self):
        html = "<html><body>"
        for s in self.items:
            html += "<div>" + s.get("name", "") + " - " + build_grade(s) + "</div>"
        html += "</body></html>"
        return html

    def plain_report(self):
        text = ""
        for s in self.items:
            text = text + s.get("name", "") + " " + build_grade(s) + "\n"
        return text

    def json_like_report(self):
        text = "["
        for s in self.items:
            text = text + "{'name':'" + s.get("name", "") + "','grade':'" + build_grade(s) + "'},"
        text = text + "]"
        return text


def repeated_validate_1(student):
    errors = []
    if student.get("name") == "": errors.append("name")
    if student.get("math") == None: errors.append("math")
    if student.get("science") == None: errors.append("science")
    if student.get("history") == None: errors.append("history")
    if student.get("email") == "": errors.append("email")
    return errors


def repeated_validate_2(student):
    errors = []
    if student.get("name") == "": errors.append("name")
    if student.get("math") == None: errors.append("math")
    if student.get("science") == None: errors.append("science")
    if student.get("history") == None: errors.append("history")
    if student.get("email") == "": errors.append("email")
    return errors


def repeated_validate_3(student):
    errors = []
    if student.get("name") == "": errors.append("name")
    if student.get("math") == None: errors.append("math")
    if student.get("science") == None: errors.append("science")
    if student.get("history") == None: errors.append("history")
    if student.get("email") == "": errors.append("email")
    return errors


def create_student_token(student):
    return weak_hash(student.get("name") + student.get("email"))
