from Const import *
from Macro_Cell import *
from Small_Cell import *


def Generate_task():
    macro_cell_lst = []
    small_cell_lst = []
    total = []
    for _ in range(30):
        a = macro_cell()
        b = small_cell()
        macro_cell_lst.append(a)
        small_cell_lst.append(b)
        total.append(a)
        total.append(b)
    return macro_cell_lst, small_cell_lst, total


def Proposed(macro_cell_lst, small_cell_lst, total, macro_cellt, small_cellt):
    macro_cell_lst = macro_cell_lst.copy()
    small_cell_lst = small_cell_lst.copy()
    total = total.copy()
    winning_macro_cell = []
    winning_small_cell = []
    for i in range(len(small_cell_lst)):
        b = (len(winning_small_cell) + 1) * small_cellt + time_to_small_cell
        if b <= small_cell_lst[i].time:
            winning_small_cell.append(small_cell_lst[i])
            total.remove(small_cell_lst[i])
    for i in range(len(total)):
        a = (len(winning_macro_cell) + 1) * macro_cellt + time_to_macro_cell
        if a <= total[i].time:
            winning_macro_cell.append(total[i])
    return winning_macro_cell, winning_small_cell


def Greedy(macro_cell_lst, small_cell_lst, total, macro_cellt, small_cellt):
    winning_macro_cell = []
    winning_small_cell = []
    macro_cell_lst = macro_cell_lst.copy()
    small_cell_lst = small_cell_lst.copy()
    total = total.copy()
    for i in range(len(total)):
        a = (len(winning_macro_cell) + 1) * macro_cellt + time_to_macro_cell
        b = (len(winning_small_cell) + 1) * small_cellt + time_to_small_cell
        if total[i].is_macro_cell == 0:
            if a < b and a <= total[i].time:
                winning_macro_cell.append(total[i])
            elif a >= b and b <= total[i].time:
                winning_small_cell.append(total[i])
        else:
            if a <= total[i].time:
                winning_macro_cell.append(total[i])
    return winning_macro_cell, winning_small_cell


def FIFO(macro_cell_lst, small_cell_lst, total, macro_cellt, small_cellt):
    winning_macro_cell = []
    winning_small_cell = []
    macro_cell_lst = macro_cell_lst.copy()
    small_cell_lst = small_cell_lst.copy()
    total = total.copy()
    for i in range(len(small_cell_lst)):
        b = (len(winning_small_cell) + 1) * small_cellt + time_to_small_cell
        flag_current = False
        if b <= small_cell_lst[i].time:
            flag_current = True
        flag_lst = True
        for task in winning_small_cell:
            if task.time < b:
                flag_lst = False
        if flag_current and flag_lst:
            winning_small_cell.append(small_cell_lst[i])
            total.remove(small_cell_lst[i])
    for i in range(len(total)):
        a = (len(winning_macro_cell) + 1) * macro_cellt + time_to_macro_cell
        flag_current = False
        if a <= total[i].time:
            flag_current = True
        flag_lst = True
        for task in winning_macro_cell:
            if task.time < a:
                flag_lst = False
        if flag_current and flag_lst:
            winning_macro_cell.append(total[i])
    return winning_macro_cell, winning_small_cell


def macro_cell_first(macro_cell_lst, small_cell_lst, total, macro_cellt, small_cellt):
    macro_cell_lst = macro_cell_lst.copy()
    small_cell_lst = small_cell_lst.copy()
    total = total.copy()
    winning_macro_cell = []
    winning_small_cell = []
    for i in range(len(macro_cell_lst)):
        b = (len(winning_macro_cell) + 1) * macro_cellt + time_to_macro_cell
        if b <= macro_cell_lst[i].time:
            winning_macro_cell.append(macro_cell_lst[i])
            total.remove(macro_cell_lst[i])
    for i in range(len(small_cell_lst)):
        a = (len(winning_small_cell) + 1) * small_cellt + time_to_small_cell
        if a <= small_cell_lst[i].time:
            winning_small_cell.append(small_cell_lst[i])
    return winning_macro_cell, winning_small_cell


def No_small_cell(macro_cell_lst, small_cell_lst, total, macro_cellt, small_cellt):
    macro_cell_lst = macro_cell_lst.copy()
    total = total.copy()
    winning_macro_cell = []
    for i in range(len(total)):
        b = (len(winning_macro_cell) + 1) * macro_cellt + time_to_macro_cell
        if b <= total[i].time:
            winning_macro_cell.append(total[i])
    return winning_macro_cell
