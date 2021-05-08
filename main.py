from datetime import datetime
from flask import Flask, request, abort, render_template, redirect, url_for, jsonify
from models import CoursesTable, InstructorsTable, SpecialtyInCollegeTable, HallsTable, \
    WorkTimeTable, StudentPlanTable, StudentPlanCoursesTable, StudentPlanCoursesTable, TimetableTable, session
from timetable_queries import CS, COE, IT
from generation import createGeneration
from database_oparations import addGenerationToDatabase

app = Flask(__name__)

'''
ROUTES                         
'''


@app.route('/')
@app.route('/home')
def home():
    return render_template('pages/home.html')

#---------------------------------------#
#            timtables                  #
#---------------------------------------#

@app.route('/timetables_cs')
def timetablesCS():
    level1, level2, level3, level4, level5, level6, level7, level8 = CS()
    return render_template('pages/timetables_cs.html', level1=level1, level2=level2, level3=level3, level4=level4,
        level5=level5, level6=level6, level7=level7, level8=level8)

@app.route('/timetables_coe')
def timetablesCOE():
    level1, level2, level3, level4, level5, level6, level7, level8 = COE()
    return render_template('pages/timetables_coe.html', level1=level1, level2=level2, level3=level3, level4=level4,
        level5=level5, level6=level6, level7=level7, level8=level8)

@app.route('/timetables_it')
def timetablesIT():
    level1, level2, level3, level4, level5, level6, level7, level8 = IT()
    return render_template('pages/timetables_it.html', level1=level1, level2=level2, level3=level3, level4=level4,
        level5=level5, level6=level6, level7=level7, level8=level8)

@app.route('/regenerate_timetables_cs')
def regenerateTimetablesCS():
    try:
        timetables_data = session.query(TimetableTable).filter_by(specialty_id=1).all()

        for data in timetables_data:
            session.delete(data)
            session.commit()

        tables = createGeneration(1)
        addGenerationToDatabase(tables)

        return redirect(url_for("timetablesCS"))

    except:
        session.rollback()
        abort(422)

@app.route('/regenerate_timetables_coe')
def regenerateTimetablesCOE():
    try:
        timetables_data = session.query(TimetableTable).filter_by(specialty_id=2).all()

        for data in timetables_data:
            session.delete(data)
            session.commit()

        tables = createGeneration(2)
        addGenerationToDatabase(tables)

        return redirect(url_for("timetablesCOE"))

    except:
        session.rollback()
        abort(422)

@app.route('/regenerate_timetables_it')
def regenerateTimetablesIT():
    try:
        timetables_data = session.query(TimetableTable).filter_by(specialty_id=3).all()

        for data in timetables_data:
            session.delete(data)
            session.commit()

        tables = createGeneration(3)
        addGenerationToDatabase(tables)

        return redirect(url_for("timetablesIT"))

    except:
        session.rollback()
        abort(422)

#---------------------------------------#
#             courses                   #
#---------------------------------------#


@app.route('/courses')
def courses():
    courses_list = session.query(CoursesTable).join(InstructorsTable).filter(
        CoursesTable.instructor_id == InstructorsTable.id).all()
    courses = []

    for course in courses_list:
        courses.append({
            "id": course.id,
            "name": course.name,
            "credit": course.credit,
            "instructor": course.instructor.name,
            "pre_req": course.pre_req,
            "co_req": course.co_req,
            "is_lab": course.is_lab
        })

    return render_template('pages/courses.html', courses=courses)


@app.route('/add_course', methods=['GET', 'POST'])
def addCourse():

    if request.method == 'POST':
        try:
            name = request.form["name"]
            credit = request.form["credit"]
            instructor_id = request.form["instructor_id"]
            pre_req = request.form["pre_req"]
            co_req = request.form["co_req"]
            if request.form["is_lab"] == "True":
                is_lab = True
            elif request.form["is_lab"] == "False":
                is_lab = False
            common = request.form.getlist("common")
            priority = request.form["priority"]
            course_data = CoursesTable(name=name, credit=credit, instructor_id=instructor_id,
                                       pre_req=pre_req, co_req=co_req, is_lab=is_lab,
                                       common=common, priority=priority)
            session.add(course_data)
            session.commit()

            return redirect(url_for("courses"))

        except:
            session.rollback()
            abort(422)
    else:
        instructors = session.query(InstructorsTable).all()
        courses = session.query(CoursesTable).all()
        departments = session.query(SpecialtyInCollegeTable).all()
        return render_template('new_forms/new_course.html', instructors=instructors,
                               courses=courses, departments=departments)


@app.route('/courses/<id>/edit', methods=['GET', 'POST'])
def editCourse(id):

    if request.method == 'POST':
        name = request.form["name"]
        credit = request.form["credit"]
        instructor_id = request.form["instructor_id"]
        pre_req = request.form["pre_req"]
        co_req = request.form["co_req"]
        if request.form["is_lab"] == "True":
            is_lab = True
        elif request.form["is_lab"] == "False":
            is_lab = False
        common = request.form.getlist("common")
        priority = request.form["priority"]
        try:
            course_data = session.query(
                CoursesTable).filter_by(id=id).one_or_none()

            course_data.name = name
            course_data.credit = credit
            course_data.instructor_id = instructor_id
            course_data.pre_req = pre_req
            course_data.co_req = co_req
            course_data.is_lab = is_lab
            if common:
                course_data.common = common
            course_data.priority = priority

            session.commit()

            return redirect(url_for("courses"))

        except:
            session.rollback()
            abort(422)
    else:
        course_data = session.query(CoursesTable).filter_by(id=id).join(InstructorsTable).filter(
            CoursesTable.instructor_id == InstructorsTable.id).one_or_none()
        instructors = session.query(InstructorsTable).all()
        courses = session.query(CoursesTable).all()
        departments = session.query(SpecialtyInCollegeTable).all()
        return render_template('edit_forms/edit_course.html', course_data=course_data, instructors=instructors, courses=courses, departments=departments)


@app.route('/courses/<id>/delete')
def deleteCourse(id):

    try:
        course_data = session.query(
            CoursesTable).filter_by(id=id).one_or_none()

        session.delete(course_data)
        session.commit()

        return redirect(url_for("courses"))

    except:
        session.rollback()
        abort(422)

#---------------------------------------#
#          instructors                  #
#---------------------------------------#


@app.route('/instructors')
def instructors():
    instructors_list = session.query(InstructorsTable).join(SpecialtyInCollegeTable).filter(
        InstructorsTable.specialty == SpecialtyInCollegeTable.id).all()
    instructors = []

    for instructor in instructors_list:
        instructors.append({
            "id": instructor.id,
            "name": instructor.name,
            "specialty": instructor.specialtyInCollege.name
        })

    return render_template('pages/instructors.html', instructors=instructors)


@app.route('/add_instructor', methods=['GET', 'POST'])
def addInstructor():

    if request.method == 'POST':
        try:
            name = request.form["name"]
            specialty = request.form["specialty"]
            instructor_data = InstructorsTable(name=name, specialty=specialty)
            session.add(instructor_data)
            session.commit()

            return redirect(url_for("instructors"))

        except:
            session.rollback()
            abort(422)
    else:
        departments = session.query(SpecialtyInCollegeTable).all()
        return render_template('new_forms/new_instructor.html', departments=departments)


@app.route('/instructors/<id>/edit', methods=['GET', 'POST'])
def editInstructor(id):

    if request.method == 'POST':
        name = request.form["name"]
        specialty = request.form["specialty"]
        try:
            instructor_data = session.query(
                InstructorsTable).filter_by(id=id).one_or_none()

            instructor_data.name = name
            instructor_data.specialty = specialty

            session.commit()

            return redirect(url_for("instructors"))

        except:
            session.rollback()
            abort(422)
    else:
        instructor_data = session.query(InstructorsTable).filter_by(id=id).join(SpecialtyInCollegeTable).filter(
            InstructorsTable.specialty == SpecialtyInCollegeTable.id).one_or_none()
        departments = session.query(SpecialtyInCollegeTable).all()
        return render_template('edit_forms/edit_instructor.html', instructor_data=instructor_data, departments=departments)


@app.route('/instructors/<id>/delete')
def deleteInstructor(id):

    try:
        instructor_data = session.query(
            InstructorsTable).filter_by(id=id).one_or_none()

        session.delete(instructor_data)
        session.commit()

        return redirect(url_for("instructors"))

    except:
        session.rollback()
        abort(422)

#---------------------------------------#
#                halls                  #
#---------------------------------------#


@app.route('/halls')
def halls():
    halls_list = session.query(HallsTable).join(SpecialtyInCollegeTable).filter(
        HallsTable.specialty_id == SpecialtyInCollegeTable.id).all()
    halls = []

    for hall in halls_list:
        halls.append({
            "id": hall.id,
            "specialty": hall.specialtyInCollege.name,
            "is_lab": hall.is_lab,
            "building": hall.building
        })

    return render_template('pages/halls.html', halls=halls)


@app.route('/add_hall', methods=['GET', 'POST'])
def addHall():

    if request.method == 'POST':
        try:
            id = request.form["id"]
            specialty_id = request.form["specialty_id"]
            if request.form["is_lab"] == "True":
                is_lab = True
            elif request.form["is_lab"] == "False":
                is_lab = False
            building = request.form["building"]
            hall_data = HallsTable(
                id=id, specialty_id=specialty_id, is_lab=is_lab, building=building)
            session.add(hall_data)
            session.commit()

            return redirect(url_for("halls"))

        except:
            session.rollback()
            abort(422)
    else:
        departments = session.query(SpecialtyInCollegeTable).all()
        return render_template('new_forms/new_hall.html', departments=departments)


@app.route('/halls/<id>/edit', methods=['GET', 'POST'])
def editHalls(id):

    if request.method == 'POST':
        hall_id = request.form["id"]
        specialty_id = request.form["specialty_id"]
        if request.form["is_lab"] == "True":
            is_lab = True
        elif request.form["is_lab"] == "False":
            is_lab = False
        building = request.form["building"]
        try:
            hall_data = session.query(
                HallsTable).filter_by(id=id).one_or_none()

            hall_data.id = hall_id
            hall_data.specialty_id = specialty_id
            hall_data.is_lab = is_lab
            hall_data.building = building

            session.commit()

            return redirect(url_for("halls"))

        except:
            session.rollback()
            abort(422)
    else:
        hall_data = session.query(HallsTable).filter_by(id=id).join(SpecialtyInCollegeTable).filter(
            HallsTable.specialty_id == SpecialtyInCollegeTable.id).one_or_none()
        departments = session.query(SpecialtyInCollegeTable).all()
        return render_template('edit_forms/edit_hall.html', hall_data=hall_data, departments=departments)


@app.route('/halls/<id>/delete')
def deleteHalls(id):

    try:
        hall_data = session.query(HallsTable).filter_by(id=id).one_or_none()

        session.delete(hall_data)
        session.commit()

        return redirect(url_for("halls"))

    except:
        session.rollback()
        abort(422)

#---------------------------------------#
#              work time                #
#---------------------------------------#


@app.route('/worktime')
def worktime():
    worktimes = session.query(WorkTimeTable).all()
    return render_template('pages/worktime.html', worktimes=worktimes)


@app.route('/add_worktime', methods=['GET', 'POST'])
def addWorktime():

    if request.method == 'POST':
        try:
            day = request.form["day"]
            start_time_raw = datetime.strptime(
                request.form["start_time"], "%H:%M")
            start_time = start_time_raw.strftime("%H:%M:%S")
            end_time_raw = datetime.strptime(request.form["end_time"], "%H:%M")
            end_time = end_time_raw.strftime("%H:%M:%S")
            if request.form["break_time_start"]:
                break_time_start_raw = datetime.strptime(
                    request.form["break_time_start"], "%H:%M")
                break_time_start = break_time_start_raw.strftime("%H:%M:%S")
            else:
                break_time_start = None
            if request.form["break_time_end"]:
                break_time_end_raw = datetime.strptime(
                    request.form["break_time_end"], "%H:%M")
                break_time_end = break_time_end_raw.strftime("%H:%M:%S")
            else:
                break_time_end = None
            worktime_data = WorkTimeTable(day=day, start_time=start_time, end_time=end_time,
                                          break_time_start=break_time_start, break_time_end=break_time_end)
            session.add(worktime_data)
            session.commit()

            return redirect(url_for("worktime"))

        except:
            session.rollback()
            abort(422)
    else:
        return render_template('new_forms/new_worktime.html')


@app.route('/worktime/<id>/edit', methods=['GET', 'POST'])
def editWorktime(id):

    if request.method == 'POST':
        day = request.form["day"]
        start_time_raw = datetime.strptime(request.form["start_time"], "%H:%M")
        start_time = start_time_raw.strftime("%H:%M:%S")
        end_time_raw = datetime.strptime(request.form["end_time"], "%H:%M")
        end_time = end_time_raw.strftime("%H:%M:%S")
        if request.form["break_time_start"]:
            break_time_start_raw = datetime.strptime(
                request.form["break_time_start"], "%H:%M:%S")
            break_time_start = break_time_start_raw.strftime("%H:%M:%S")
        else:
            break_time_start = None
        if request.form["break_time_end"]:
            break_time_end_raw = datetime.strptime(
                request.form["break_time_end"], "%H:%M:%S")
            break_time_end = break_time_end_raw.strftime("%H:%M:%S")
        else:
            break_time_end = None
        try:
            worktime_data = session.query(
                WorkTimeTable).filter_by(id=id).one_or_none()

            worktime_data.day = day
            worktime_data.start_time = start_time
            worktime_data.end_time = end_time
            worktime_data.break_time_start = break_time_start
            worktime_data.break_time_end = break_time_end

            session.commit()

            return redirect(url_for("worktime"))

        except:
            session.rollback()
            abort(422)
    else:
        worktime_data = session.query(
            WorkTimeTable).filter_by(id=id).one_or_none()
        return render_template('edit_forms/edit_worktime.html', worktime_data=worktime_data)


@app.route('/worktime/<id>/delete')
def deleteWorktime(id):

    try:
        worktime_data = session.query(
            WorkTimeTable).filter_by(id=id).one_or_none()

        session.delete(worktime_data)
        session.commit()

        return redirect(url_for("worktime"))

    except:
        session.rollback()
        abort(422)

#---------------------------------------#
#            student plan               #
#---------------------------------------#


@app.route('/studentplan')
def studentplan():
    student_plan_list = session.query(StudentPlanTable).join(SpecialtyInCollegeTable).filter(
        StudentPlanTable.specialty == SpecialtyInCollegeTable.id).all()
    student_plans = []

    for student_plan in student_plan_list:
        student_plans.append({
            "id": student_plan.id,
            "name": student_plan.name,
            "specialty": student_plan.specialtyInCollege.name
        })
    return render_template('pages/studentplan.html', student_plans=student_plans)


@app.route('/add_studentplan', methods=['GET', 'POST'])
def addStudentPlan():

    if request.method == 'POST':
        try:
            name = request.form["name"]
            specialty = request.form["specialty"]
            student_plan_data = StudentPlanTable(
                name=name, specialty=specialty)
            session.add(student_plan_data)
            session.commit()

            return redirect(url_for("studentplan"))

        except:
            session.rollback()
            abort(422)
    else:
        departments = session.query(SpecialtyInCollegeTable).all()
        return render_template('new_forms/new_studentplan.html', departments=departments)


@app.route('/studentplan/<id>/edit', methods=['GET', 'POST'])
def editStudentPlan(id):

    if request.method == 'POST':
        name = request.form["name"]
        specialty = request.form["specialty"]
        try:
            student_plan_data = session.query(
                StudentPlanTable).filter_by(id=id).one_or_none()

            student_plan_data.name = name
            student_plan_data.specialty = specialty

            session.commit()

            return redirect(url_for("studentplan"))

        except:
            session.rollback()
            abort(422)
    else:
        student_plan_data = session.query(
            StudentPlanTable).filter_by(id=id).one_or_none()
        departments = session.query(SpecialtyInCollegeTable).all()
        return render_template('edit_forms/edit_studentplan.html', student_plan_data=student_plan_data, departments=departments)


@app.route('/studentplan/<id>/delete')
def deleteStudentPlan(id):

    try:
        student_plan_data = session.query(
            StudentPlanTable).filter_by(id=id).one_or_none()

        session.delete(student_plan_data)
        session.commit()

        return redirect(url_for("studentplan"))

    except:
        session.rollback()
        abort(422)

#---------------------------------------#
#        student plan courses           #
#---------------------------------------#


@app.route('/studentplan/<id>')
def studentplanCourses(id):
    paln_name = session.query(StudentPlanTable).filter(
        id == StudentPlanTable.id).one_or_none()
    student_plan_courses_list = session.query(StudentPlanCoursesTable).filter(id == StudentPlanCoursesTable.student_plan_id).join(CoursesTable).filter(
        StudentPlanCoursesTable.course_id == CoursesTable.id).all()
    student_plan_courses = []

    for student_plan_course in student_plan_courses_list:
        student_plan_courses.append({
            "id": student_plan_course.id,
            "student_plan": student_plan_course.student_plan_id,
            "course": student_plan_course.course.name,
            "level": student_plan_course.level
        })
    return render_template('pages/studentplancourses.html', student_plan_courses=student_plan_courses, paln_name=paln_name)


@app.route('/studentplan/<id>/add_course', methods=['GET', 'POST'])
def addStudentPlanCourses(id):

    if request.method == 'POST':
        try:
            course_id = request.form["course_id"]
            level = request.form["level"]
            student_plan_data = StudentPlanCoursesTable(
                student_plan_id=id, level=level, course_id=course_id)
            session.add(student_plan_data)
            session.commit()

            return redirect(url_for("studentplanCourses", id=id))

        except:
            session.rollback()
            abort(422)
    else:
        paln_name = session.query(StudentPlanTable).filter(
            id == StudentPlanTable.id).one_or_none()
        courses = session.query(CoursesTable).all()
        return render_template('new_forms/new_studentplancourse.html', paln_name=paln_name, courses=courses)


@app.route('/studentplan/<id>/edit_course/<courseId>', methods=['GET', 'POST'])
def editStudentPlanCourses(id, courseId):

    if request.method == 'POST':
        course_id = request.form["course_id"]
        level = request.form["level"]
        try:
            studentplan_course_data = session.query(
                StudentPlanCoursesTable).filter_by(id=courseId).one_or_none()

            studentplan_course_data.course_id = course_id
            studentplan_course_data.level = level

            session.commit()

            return redirect(url_for("studentplanCourses", id=id))

        except:
            session.rollback()
            abort(422)
    else:
        studentplan_course_data = session.query(StudentPlanCoursesTable).filter_by(id=courseId).join(CoursesTable).filter(
            StudentPlanCoursesTable.course_id == CoursesTable.id).one_or_none()
        courses = session.query(CoursesTable).all()
        return render_template('edit_forms/edit_studentplancourse.html', studentplan_course_data=studentplan_course_data, courses=courses)


@app.route('/studentplan/<id>/delete_course/<courseId>')
def deleteStudentPlanCourses(id, courseId):

    try:
        studentplan_course_data = session.query(
            StudentPlanCoursesTable).filter_by(id=courseId).one_or_none()

        session.delete(studentplan_course_data)
        session.commit()

        return redirect(url_for("studentplanCourses", id=id))

    except:
        session.rollback()
        abort(422)


'''
Error Handling 
'''


@app.errorhandler(422)
def unprocessable(error):
    error_code = '422'
    return render_template('error/error.html', error_code=error_code)


@app.errorhandler(404)
def not_found(error):
    error_code = '404'
    return render_template('error/error.html', error_code=error_code)


'''
Launch
'''
if __name__ == '__main__':
    app.run(debug=True)
