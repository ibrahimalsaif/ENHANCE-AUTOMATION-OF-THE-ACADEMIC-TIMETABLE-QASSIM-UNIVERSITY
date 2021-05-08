from models import CoursesTable, StudentPlanTable, SpecialtyInCollegeTable, InstructorsTable, HallsTable, \
    StudentPlanCoursesTable, WorkTimeTable, TimetableTable, session
from user_data import *

'''
The class below is a helper for the getting the data from the database
1- courses:
    :return: list of dictionaries for th data in courses
2- studentPan:
    :return: list of dictionaries for th data in studentPan
3- specialtyInCollege:
    :return: list of dictionaries for th data in specialtyInCollege
4- instructors:
    :return: list of dictionaries for th data in instructors
5- halls:
    :return: list of dictionaries for th data in halls
6- studentPlanCourses:
    :return: list of dictionaries for th data in studentPlanCourses
7- workTime:
    :return: list of dictionaries for th data in workTime
'''


class GetFromDatabase:

    def courses(self):
        allCourses = session.query(CoursesTable).all()
        data = []

        for row in allCourses:
            dataRow = Courses(row.id, row.name, row.credit, row.instructor_id,
                              row.pre_req, row.co_req, row.is_lab,
                              row.common, row.priority)
            data.append(dataRow)

        return data

    def studentPlan(self,id):
        allStudentPlans = session.query(StudentPlanTable).filter_by(specialty=id).all()
        data = []

        for row in allStudentPlans:
            dataRow = StudentPlan(row.id, row.name, row.specialty)
            data.append(dataRow)

        return data

    def specialtyInCollege(self):
        allSpecialtyInCollege = session.query(SpecialtyInCollegeTable).all()
        data = []

        for row in allSpecialtyInCollege:
            dataRow = SpecialtyInCollege(row.id, row.name)
            data.append(dataRow)

        return data

    def instructors(self):
        allInstructors = session.query(InstructorsTable).all()
        data = []

        for row in allInstructors:
            dataRow = Instructors(row.id, row.name, row.specialty)
            data.append(dataRow)

        return data

    def halls(self, id):
        allHalls = session.query(HallsTable).filter_by(specialty_id=id).all()
        data = []

        for row in allHalls:
            dataRow = Halls(row.id, row.specialty_id, row.is_lab, row.building)
            data.append(dataRow)

        return data

    def studentPlanCourses(self,id):
        allStudentPlanCourses = session.query(StudentPlanCoursesTable).filter_by(student_plan_id=id).all()
        data = []

        for row in allStudentPlanCourses:
            dataRow = StudentPlanCourses(row.student_plan_id, row.level, row.course_id)
            data.append(dataRow)

        return data

    def workTime(self):
        allWorkTime = session.query(WorkTimeTable).all()
        data = []

        for row in allWorkTime:
            dataRow = WorkTime(row.day, row.start_time, row.end_time,
                               row.break_time_start, row.break_time_end)
            data.append(dataRow)

        return data


class QueryOperations:

    def getCourseById(self, course_id, courses) -> Courses:
        for course in courses:
            if course.id == course_id:
                return course
        return -1

    def getInstructorById(self, instructor_id, instructors):
        for instructor in instructors:
            if instructor.id == instructor_id:
                return instructor
        return -1


def addGenerationToDatabase(tables):
    for course in tables:
        course_data = TimetableTable(specialty_id=course['specialty_id'], course_id=course['course_id'],
                                     hall_id=course['hall_id'],
                                     instructor_id=course['instructor'], start_time=course['start_time'],
                                     end_time=course['end_time'], day=course['day'], level=course['level'])
        session.add(course_data)
        session.commit()
