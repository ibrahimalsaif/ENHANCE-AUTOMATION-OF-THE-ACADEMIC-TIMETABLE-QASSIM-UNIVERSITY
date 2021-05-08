"""
this file will handle the generation step


steps to make a table:
# 1-course should connect with there levels
# 2-course should sorted by priority
# 3-make a list for every level taking this form student`s plan
# 4-we can shortcut the way to take the courses from student`s plan ----- note
# 5-distribute the time of every course so
    if course has credit > 2 hours course will divide into 2 parts
# 6-course that has 2 parts will saved as a list of 2 elements
# 7-moving level by level to add course to the table so in this
    case we will band the conflict between level itself
# 8-the way to add the courses is:
#     a- sort courses by priority

"""

from crossover import crossover
from database_oparations import *
from table import *


class Generation:
    """
    auto generate tables
    """

    def __init__(self, specialty_id):
        get_from_database = GetFromDatabase()

        self.courses_list = []
        self.halls = get_from_database.halls(specialty_id)
        self.student_plan_courses = get_from_database.studentPlanCourses(specialty_id)
        self.table = Table()
        self.err_name = ""
        self.err_value = 0
        self.err_counter = 0
        self.startGen()
        self.work_time = get_from_database.workTime()


    def getData(self):
        """
        getting data from database and fill the properties of this class
        :return:
        """
        get_from_database = GetFromDatabase()

    def startGen(self):
        """
        thie is the main method of Generation and it will generate different tables for population
        :return: number of tables
        """
        q_operations = QueryOperations()
        get_from_database = GetFromDatabase()
        list_of_courses = get_from_database.courses()
        self.courses_list = []
        for std_plan_course in self.student_plan_courses:
            self.courses_list.append(q_operations.getCourseById(
                std_plan_course.course_id, list_of_courses))

        self.sortCourseByPriority()
        self.distributeCourseCredit()
        self.startAddingToTable()

    def startAddingToTable(self):
        counter_for_course_not_added = 0
        temp = 0
        for course in self.courses_list:
            tries = 0
            result = 0
            # init false value for saving old result in iteration
            cell = TableCell(0, 0, 0, 0)
            while True:
                level = self.getCourseLevel(course)
                cell = self.makeTableCell(course, level, tries, result, cell)
                result = self.table.addClassToTable(cell)
                if result == 1 or tries >= 10000:  # loop will stop if course been added or did not find place in table
                    temp += 1
                    if tries >= 10000:
                        print(course.name, " || ", course.credit, " || ", temp,
                              ": has end the tries without been added")
                        counter_for_course_not_added += 1
                    break
                tries += 1
            self.err_name = ""
            self.err_value = 0
        print("Number of courses are not added:", counter_for_course_not_added)
        print("Number of courses are: ", len(self.courses_list))

    def makeTableCell(self, course: Courses, level: int, tries: int, conflict: int, old_value: TableCell) -> TableCell:
        """

        :param old_value:
        :param course:
        :param level:
        :param tries:
        :param conflict:
        :return:
        """
        hall = old_value.hall
        table_cell_time = old_value.table_cell_time

        if conflict == 0:
            table_cell_time = self.makeTableCellTime(
                conflict, course.credit, TableCellTime(0, 0, 1))
            hall = self.getHall(Halls(0, 0, False, 0))

        elif conflict == -1:  # conflict in halls
            if tries % len(self.halls) == 0:
                table_cell_time = self.makeTableCellTime(
                    conflict, course.credit, table_cell_time)
            else:
                hall = self.getHall(hall)
        elif conflict == -2:  # conflict with Time
            table_cell_time = self.makeTableCellTime(
                conflict, course.credit, table_cell_time)
        elif conflict == -3:  # conflict with doctor
            table_cell_time = self.makeTableCellTime(
                conflict, course.credit, table_cell_time)
        elif conflict == -4:  # conflict with second part of same course
            table_cell_time = self.makeTableCellTime(
                conflict, course.credit, table_cell_time, True, course)

        return TableCell(course, hall, table_cell_time, level)

    def makeTableCellTime(self, conflict: int, course_credit: float, old_value: TableCellTime,
                          is_adding_second_part_of_course=False, course=None) -> TableCellTime:
        """
        :param course:
        :param is_adding_second_part_of_course:
        :param course_credit:
        :param conflict:
        :param old_value:
        :return:
        """
        work_time = [8.0, 16.0]  # work time from 8AM to 4PM
        break_time_between_courses = [0.0, 0.0]

        day = old_value.day  # represent sunday
        first_day = 1
        max_days = 5  # represent maximum number of day in week
        start_time = old_value.start
        # divide time into to parts morning and afternoon where morning start from 8-11
        time_division = 11.0
        favorite_time = work_time[0] if course_credit < 2 else time_division

        if is_adding_second_part_of_course and course is not None:
            get_time_cell_of_first_part_of_course = self.getTimeCellOfFirstPartOfCourse(
                course)
            if get_time_cell_of_first_part_of_course is not None:
                start_time = get_time_cell_of_first_part_of_course.start
                end_time = start_time + course_credit
                day += 1
                if day > max_days:
                    day = first_day
                return TableCellTime(start_time, end_time, day)

        if start_time == 0:
            start_time = favorite_time
            end_time = start_time + course_credit
            return TableCellTime(start_time, end_time, day)

        else:
            start_time = old_value.end
            if (break_time_between_courses[0] < old_value.end < break_time_between_courses[1]) or \
                    (break_time_between_courses[0] < old_value.end + course_credit < break_time_between_courses[1]):
                start_time = break_time_between_courses[1]
            end_time = start_time + course_credit
            if start_time + course_credit > work_time[1]:
                day = old_value.day + 1
                start_time = favorite_time
                end_time = start_time + course_credit
                if day > max_days:
                    day = first_day
                    start_time = work_time[0]
                    end_time = start_time + course_credit

            return TableCellTime(start_time, end_time, day)

    def getHall(self, old_value: Halls) -> Halls:
        if old_value.id == 0:
            return self.halls[0]

        index = self.halls.index(old_value) + 1
        if index >= len(self.halls):
            index = 0

        return self.halls[index]

    def getTimeCellOfFirstPartOfCourse(self, course: Courses) -> TableCellTime:
        for r in self.table.time_table:
            for c in self.table.time_table[r]:
                if course.id == c.course.id:
                    return c.table_cell_time
        return None

    def sortCourseByPriority(self):
        """
        sort course by priority
        :return: none
        """
        for i in range(len(self.courses_list)):
            for j in range(len(self.courses_list)):
                if self.courses_list[i].getCredit() < self.courses_list[j].getCredit():
                    temp = self.courses_list[i]
                    self.courses_list[i] = self.courses_list[j]
                    self.courses_list[j] = temp

    def sortCourseByLevel(self):
        """
        sort course by priority
        :return: none
        """
        for i in range(len(self.courses_list)):
            for j in range(len(self.courses_list)):
                if self.getCourseLevel(self.courses_list[i]) < self.getCourseLevel(self.courses_list[j]):
                    temp = self.courses_list[i]
                    self.courses_list[i] = self.courses_list[j]
                    self.courses_list[j] = temp

    def distributeCourseCredit(self):
        """
        to distribute course credit for courses that grater than 2 hour
        :return: none
        """
        new_distributed_course_credit = []
        for course in self.courses_list:
            credit = course.getCredit()
            if credit > 2:
                course1 = course
                course1.setCredit(credit / 2)
                course2 = course
                course2.setCredit(credit / 2)
                new_distributed_course_credit.append(course1)
                new_distributed_course_credit.append(course2)
                continue
            else:
                new_distributed_course_credit.append(course)
        self.courses_list = new_distributed_course_credit

    def getCourseLevel(self, course: Courses) -> int:
        """
        help to find the level of the cours
        :param course: specific course
        :return: level as integer
        """
        for x in self.student_plan_courses:
            if x.course_id == course.id:
                return x.level
        return -1  # course not found


'''

Generate tables with the parameter department_id

'''

def createGeneration(dep_id):
    gen = Generation(dep_id)
    crossover(gen.table)
    tables = gen.table.getTableData()
    return tables


