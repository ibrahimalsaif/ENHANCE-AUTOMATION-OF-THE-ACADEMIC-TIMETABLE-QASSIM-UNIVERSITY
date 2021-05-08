from typing import List, Dict

from table import *


def fitness(table: Table, max_level=8) -> int:
    """
    test the time table of level if has conflict with next or previous level courses
    :param max_level: max level of student plan that been added
    :param table: generated  time table
    :return: number of conflict courses
    """
    courses_level = []
    number_of_conflict = 0
    for level in range(max_level):
        courses_level.append(getCoursesOfLevel(table.time_table, (level + 1)))

    for i in range(len(courses_level)):
        for table_cell in courses_level[i]:
            if i < len(courses_level) - 1:
                number_of_conflict += compareWithLevel(table_cell, courses_level[i + 1])
            if i > 0:
                number_of_conflict += compareWithLevel(table_cell, courses_level[i - 1])

    return number_of_conflict


def compareWithLevel(table_cell: TableCell, cells: List[TableCell]) -> int:
    """

    :param table_cell:
    :param cells:
    :return:
    """
    conflict_counter = 0
    for cell in cells:
        if table_cell == cell:
            conflict_counter += 1
            print(table_cell.course.name, table_cell.level, table_cell.table_cell_time.start,
                  table_cell.table_cell_time.end, table_cell.table_cell_time.day,
                  end='\n')
            print(cell.course.name, cell.level, cell.table_cell_time.start, cell.table_cell_time.end,
                  cell.table_cell_time.day,
                  end='\n\n')

    return conflict_counter


def getCoursesOfLevel(time_table: Dict[str, List[TableCell]], level: int) -> List[TableCell]:
    """

    :param time_table:
    :param level:
    :return:
    """
    table_cells = list([TableCell])
    table_cells.clear()
    for day in time_table:
        for table_cell in time_table[day]:
            if table_cell.level == level:
                table_cells.append(table_cell)

    return table_cells


class Fitness:
    def __init__(self, time_table: dict):
        self.time_table = time_table
