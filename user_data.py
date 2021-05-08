def sortCoursesByPriority(courses_list) -> list:
    """
    this will sort all course that given by priority
    :param courses_list: list of courses that will get sorted
    :return: sorted list
    """
    for index in range(len(courses_list)):
        i = index
        while i < len(courses_list):
            if courses_list[index].priority > courses_list[i].priority:
                temp = courses_list[index]
                courses_list[index] = courses_list[i]
                courses_list[i] = temp
            i += 1
    return courses_list


'''
The classes below are helpers for sorting the data coming from the user
1- Setters:
    it will set the given value to the related variables in the class
    :param: the value to be set
2- Getters:
    it will get the value of the desired variable from the object
    :return : the desired variable
3- Get all:
    it will get all the variables stored in an object in a dictionary
    :return : a dictionary with the related variables
4- __eq__:
    it will compare two instances together
    :param : the related instances 
    :return : True if they are the same and False if they are not
'''


class Courses:
    def __int__(self):
        pass

    def __init__(self, id, name, credit, instructor, pre_req, co_req, is_lab, common, priority):
        self.id = id
        self.name = name
        self.credit = credit
        self.instructor = instructor
        self.pre_req = pre_req
        self.co_req = co_req
        self.is_lab = is_lab
        self.common = common
        self.priority = priority

    def setId(self, id):
        self.id = id

    def setName(self, name):
        self.name = name

    def setCredit(self, credit: float):
        self.credit = credit

    def setInstructor(self, instructor):
        self.instructor = instructor

    def setPreReq(self, pre_req):
        self.pre_req = pre_req

    def setCoReq(self, co_req):
        self.co_req = co_req

    def setIsLab(self, is_lab):
        self.is_lab = is_lab

    def setCommon(self, common):
        self.common = common

    def setPriority(self, priority):
        self.priority = priority

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getCredit(self):
        return self.credit

    def getInstructor(self):
        return self.instructor

    def getPreReq(self):
        return self.pre_req

    def getCoReq(self):
        return self.co_req

    def getIsLab(self):
        return self.is_lab

    def getCommon(self):
        return self.common

    def getPriority(self):
        return self.priority

    def getAll(self):
        data = {'id': self.id, 'name': self.name, 'credit': self.credit, 'instructor': self.instructor,
                'previos requirement': self.pre_req,
                'co requirement': self.co_req, 'lab': self.is_lab, 'common': self.common, 'priority': self.priority}
        return data

    def __eq__(self, other):
        if not isinstance(other, Courses):
            return NotImplemented
        return self.getAll() == other.getAll()


class StudentPlan:

    def __init__(self, id, name, specialty):
        self.id = id
        self.name = name
        self.specialty = specialty

    def setId(self, id):
        self.id = id

    def setName(self, name):
        self.name = name

    def setSpecialty(self, specialty):
        self.specialty = specialty

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getSpecialty(self):
        return self.specialty

    def getAll(self):
        data = {'id': self.id, 'name': self.name, 'specialty': self.specialty}
        return data

    def __eq__(self, other):
        if not isinstance(other, StudentPlan):
            return NotImplemented
        return self.getAll() == other.getAll()


class SpecialtyInCollege:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def setId(self, id):
        self.id = id

    def setName(self, name):
        self.name = name

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getAll(self):
        data = {'id': self.id, 'name': self.name}
        return data

    def __eq__(self, other):
        if not isinstance(other, SpecialtyInCollege):
            return NotImplemented
        return self.getAll() == other.getAll()


class Instructors:

    def __init__(self, id, name, specialty):
        self.id = id
        self.name = name
        self.specialty = specialty

    def setId(self, id):
        self.id = id

    def setName(self, name):
        self.name = name

    def setSpecialty(self, specialty):
        self.specialty = specialty

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getSpecialty(self):
        return self.specialty

    def getAll(self):
        data = {'id': self.id, 'name': self.name, 'specialty': self.specialty}
        return data

    def __eq__(self, other):
        if not isinstance(other, Instructors):
            return NotImplemented
        return self.getAll() == other.getAll()


class Halls:

    def __init__(self, id, specialty_id, is_lab, building):
        self.id = id
        self.specialty_id = specialty_id
        self.is_lab = is_lab
        self.building = building

    def setId(self, id):
        self.id = id

    def setSpecialtyId(self, specialty_id):
        self.specialty_id = specialty_id

    def setIsLab(self, is_lab):
        self.is_lab = is_lab

    def setBuilding(self, building):
        self.building = building

    def getId(self):
        return self.id

    def getSpecialtyId(self):
        return self.specialty_id

    def getIsLab(self):
        return self.is_lab

    def getBuilding(self):
        return self.building

    def getAll(self):
        data = {'id': self.id, 'specialty id': self.specialty_id, 'lab': self.is_lab, 'building': self.building}
        return data

    def __eq__(self, other):
        if not isinstance(other, Halls):
            return NotImplemented
        return self.getAll() == other.getAll()


class StudentPlanCourses:

    def __init__(self, student_plan_id, level, course_id):
        self.student_plan_id = student_plan_id
        self.level = level
        self.course_id = course_id

    def setStudentPlanId(self, student_plan_id):
        self.student_plan_id = student_plan_id

    def setLevel(self, level):
        self.level = level

    def setCourseId(self, course_id):
        self.course_id = course_id

    def getStudentPlanId(self):
        return self.student_plan_id

    def getLevel(self):
        return self.level

    def getCourseId(self):
        return self.course_id

    def getAll(self):
        data = {'student plan id': self.student_plan_id, 'level': self.level, 'course id': self.course_id}
        return data

    def __eq__(self, other):
        if not isinstance(other, StudentPlanCourses):
            return NotImplemented
        return self.getAll() == other.getAll()


class WorkTime:

    def __init__(self, day, start_time, end_time, break_time_start, break_time_end):
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self.break_time_start = break_time_start
        self.break_time_end = break_time_end

    def setDay(self, day):
        self.day = day

    def setStartTime(self, start_time):
        self.start_time = start_time

    def setEndTime(self, end_time):
        self.end_time = end_time

    def setBreakTimeStart(self, break_time_start):
        self.break_time_start = break_time_start

    def setBreakTimeEnd(self, break_time_end):
        self.break_time_end = break_time_end

    def getDay(self):
        return self.day

    def getStartTime(self):
        return self.start_time

    def getEndTime(self):
        return self.end_time

    def getBreakTimeStart(self):
        return self.break_time_start

    def getBreakTimeEnd(self):
        return self.break_time_end

    def getAll(self):
        data = {'day': self.day, 'start time': self.start_time, 'end time': self.end_time,
                'break time start': self.break_time_start, 'break time end': self.break_time_end}
        return data

    def __eq__(self, other):
        if not isinstance(other, WorkTime):
            return NotImplemented
        return self.getAll() == other.getAll()
