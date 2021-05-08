from user_data import *


class TableCellTime:
    """
    used to set the time of every cell in the table
    """

    def __init__(self, start: float, end: float, day: int):
        """
            time should represent like this 10:30 => 10.50,
            so the rule is minutes will divided by 60 like: 30/60 = 0.5 and sum with true numbers
            :param start: is the start time of the class
            :param end: is the end time of the class
            :param day: the doy of the lecture days will represent like this(sunday = 1, monday = 2, ...)
        """
        self.start = start
        self.end = end
        self.day = day
        self.course_credit = abs(end - start)

    def __eq__(self, other):
        """
        equality method for comparing
        :param other: same object to compare
        :return: true if there is conflict
        """
        if not isinstance(other, TableCellTime):
            return NotImplemented
        other_credit = abs(other.end - other.start)
        return (abs((self.start + self.end) - (other.start + other.end)) < (
                self.course_credit + other_credit)) and self.day == other.day


# this class are used by table to save all data need of table cell
class TableCell:
    """ this class are used by table to save all data need of table cell"""

    def __init__(self, course: Courses, hall: Halls, table_cell_time: TableCellTime, level: int):
        """
        :param course: object of course class
        :param hall: object of hall class
        :param table_cell_time: object of table_cell_time class
        :param level: integer value of level and should be limit to 10 as max level
        """
        self.course = course
        self.hall = hall
        self.table_cell_time = table_cell_time
        self.level = level

    def __eq__(self, other):
        """
        this method for equality
        :param other: same object to compare
        :return: true if there is conflict
        """
        if not isinstance(other, TableCell):
            return NotImplemented
        return (
                       self.course.instructor == other.course.instructor and self.table_cell_time == other.table_cell_time) or (
                       self.hall == other.hall and self.table_cell_time == other.table_cell_time) or (
                       self.level == other.level and self.table_cell_time == other.table_cell_time) or (
                       self.level == (other.level + 1) and self.table_cell_time == other.table_cell_time
                       and other.course.pre_req != self.course.name) or (
                       (self.level + 1) == other.level and self.table_cell_time == other.table_cell_time
                       and other.course.pre_req != self.course.name)


class Table:
    """
    this class will represent the full table
    :arg time_table will save data of all levels and we can figure out the courses of every level depending on var
        level in table_cell object
    """

    def __init__(self):
        self.time_table = {'1': [], '2': [], '3': [], '4': [], '5': []}

    def addClassToTable(self, table_cell: TableCell) -> int:
        """
        this method will add table_cell to the table
        :param table_cell: object of TableCell
        :return: 1 if there is no conflict, -1 if there is conflict in Hall,
                -2 if there is conflict with time, -3 if there is conflict with doctor,
                -4 if course been divided and other part been add to the same day
        """
        for cell in self.time_table[str(table_cell.table_cell_time.day)]:
            if cell == table_cell:  # chek if there is conflict with other courses
                if cell.course.instructor == table_cell.course.instructor and cell.table_cell_time == table_cell.table_cell_time:
                    return -3  # conflict with doctor
                if cell.hall == table_cell.hall and cell.table_cell_time == table_cell.table_cell_time:
                    return -1  # conflict with Hall
                else:
                    return -2  # conflict with time

        for cell in self.time_table[str(table_cell.table_cell_time.day)]:
            if cell.course.id == table_cell.course.id:
                return -4  # conflict with same course in same day
        self.time_table[str(table_cell.table_cell_time.day)].append(table_cell)  # add the table cell to the time table
        return 1  # no conflict

    def isCourseBeenAdded(self, table_cell: TableCell):
        """
        this will search in all table if the material has been added form other specialist
        :param table_cell:
        :return: true if course has been founded
        """
        for cells_in_day in self.time_table:  # get the list of every day
            for cell in self.time_table[cells_in_day]:  # loop to find the course throw list of day
                if cell.course.id == table_cell.course.id:
                    return True
        return False

    def isAddable(self, table_cell: TableCell) -> bool:
        """
        this method will add table_cell to the table
        :param table_cell: object of TableCell
        :return: True if it can be added, otherwise false
        """
        for cell in self.time_table[str(table_cell.table_cell_time.day)]:
            if cell == table_cell:  # chek if there is conflict with other courses
                return False
        return True

    def getTableData(self) -> list:
        """
        get all data in the table
        :return: list of deic
        """
        data = []
        for day in self.time_table:
            for cell in self.time_table[day]:
                data.append({"specialty_id": cell.hall.specialty_id,
                             "course_id": cell.course.id,
                             "instructor": cell.course.instructor,
                             "hall_id": cell.hall.id,
                             "start_time": cell.table_cell_time.start,
                             "end_time": cell.table_cell_time.end,
                             "day": cell.table_cell_time.day,
                             "level": cell.level})

        return data


