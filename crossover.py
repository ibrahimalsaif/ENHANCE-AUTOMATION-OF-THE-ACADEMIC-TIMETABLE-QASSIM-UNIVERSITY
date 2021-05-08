from random import randint

from table import *


def crossover(table: Table):
    """
    swap courses between days
    :param table:
    :return:
    """
    time_table = table.time_table
    random_day = randint(1, 5)
    random_day_2 = 0
    while (True):
        random_day_2 = randint(1, 5)
        if random_day != random_day_2:
            break
    temp_list_for_day = time_table[str(random_day)]
    temp_list_for_other_day = time_table[str(random_day_2)]
    time_table[str(random_day)] = []
    time_table[str(random_day_2)] = []

    for cell in temp_list_for_day:
        if cell.table_cell_time.start >= 11:
            cell.table_cell_time.day = random_day_2
        time_table[str(random_day_2)].append(cell)

    for cell in temp_list_for_other_day:
        if cell.table_cell_time.start >= 11:
            cell.table_cell_time.day = random_day
        time_table[str(random_day)].append(cell)

