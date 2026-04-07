from flask import Flask, render_template, request

app = Flask(__name__)

# ---------------- BUBBLE SORT ----------------
def bubble_sort(students):

    n = len(students)

    for i in range(n):

        for j in range(0, n-i-1):

            # Compare USN strings
            if students[j] > students[j+1]:

                students[j], students[j+1] = students[j+1], students[j]

    return students


# ---------------- GREEDY ALGORITHM ----------------
def greedy_allocation(students, rooms):

    allocation = []
    student_index = 0

    for capacity in rooms:

        room_students = []

        while capacity > 0 and student_index < len(students):

            room_students.append(students[student_index])
            student_index += 1
            capacity -= 1

        allocation.append(room_students)

    return allocation


# ---------------- INDEX PAGE ----------------
@app.route('/')
def index():
    return render_template("index.html")


# ---------------- ALLOCATION ----------------
@app.route('/allocate', methods=['POST'])
def allocate():

    program = request.form.get("program")
    section = request.form.get("section")
    year = request.form.get("year")
    semester = request.form.get("semester")

    usn_list = request.form.getlist("usn[]")
    name_list = request.form.getlist("name[]")

    students = []

    for usn, name in zip(usn_list, name_list):

        if usn.strip() != "" and name.strip() != "":
            students.append(usn + " - " + name)

    students.sort()

    rooms_input = request.form["rooms"]
    rooms = [int(r.strip()) for r in rooms_input.split(",") if r.strip() != ""]

    result = greedy_allocation(students, rooms)

    return render_template(
        "result.html",
        result=result,
        program=program,
        section=section,
        year=year,
        semester=semester
    )


if __name__ == "__main__":
    app.run(debug=True)