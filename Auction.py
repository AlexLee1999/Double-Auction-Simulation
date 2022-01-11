from Const import *
from Macro_Cell import *
from Small_Cell import *


def Generate_task():
    macro_cell_lst = []
    small_cell_lst = []
    total = []
    for _ in range(MACRO_CELL_USER):
        a = macro_cell_user()
        macro_cell_lst.append(a)
        total.append(a)
        
    for i in range(SMALL_NUM):
        small_cell_user_lst = []
        for _ in range(SMALL_CELL_USER):
            b = small_cell_user(i)
            small_cell_user_lst.append(b)
            total.append(b)
        small_cell_lst.append(small_cell_user_lst)
    return macro_cell_lst, small_cell_lst, total


def Proposed(macro_cell_lst, small_cell_lst, total, macro_cellt, small_cellt):
    macro_cell_lst = macro_cell_lst.copy()
    small_cell_lst = small_cell_lst.copy()
    total = total.copy()
    winning_macro_cell = []
    winning_small_cell = []
    for lst in small_cell_lst:
        cell_count = 0
        for i in range(len(lst)):
            b = (cell_count + 1) * small_cellt + time_to_small_cell
            if b <= lst[i].time:
                winning_small_cell.append(lst[i])
                total.remove(lst[i])
                cell_count += 1
    for i in range(len(total)):
        a = (len(winning_macro_cell) + 1) * macro_cellt + time_to_macro_cell
        if a <= total[i].time:
            winning_macro_cell.append(total[i])
    return winning_macro_cell, winning_small_cell


def Greedy(macro_cell_lst, small_cell_lst, total, macro_cellt, small_cellt):
    winning_macro_cell = []
    winning_small_cell = []
    cell_count = []
    for i in range(SMALL_NUM):
        cell_count.append(0)
    macro_cell_lst = macro_cell_lst.copy()
    small_cell_lst = small_cell_lst.copy()
    total = total.copy()
    for i in range(len(total)):
        a = (len(winning_macro_cell) + 1) * macro_cellt + time_to_macro_cell
        if total[i].is_macro_cell == 0:
            b = (cell_count[total[i].cell_num] + 1) * small_cellt + time_to_small_cell
            if a < b and a <= total[i].time:
                winning_macro_cell.append(total[i])
            elif a >= b and b <= total[i].time:
                winning_small_cell.append(total[i])
                cell_count[total[i].cell_num] += 1
        else:
            if a <= total[i].time:
                winning_macro_cell.append(total[i])
    return winning_macro_cell, winning_small_cell


def Fifo(macro_cell_lst, small_cell_lst, total, macro_cellt, small_cellt):
    winning_macro_cell = []
    winning_small_cell = []
    macro_cell_lst = macro_cell_lst.copy()
    small_cell_lst = small_cell_lst.copy()
    total = total.copy()
    for lst in small_cell_lst:
        count = 0
        for i in range(len(lst)):
            b = (count + 1) * small_cellt + time_to_small_cell
            flag_current = False
            if b <= lst[i].time:
                flag_current = True
            flag_lst = True
            for task in winning_small_cell:
                if task.time < b:
                    flag_lst = False
            if flag_current and flag_lst:
                winning_small_cell.append(lst[i])
                total.remove(lst[i])
                count += 1
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
    for lst in small_cell_lst:
        count = 0
        for i in range(len(lst)):
            a = (count + 1) * small_cellt + time_to_small_cell
            if a <= lst[i].time:
                winning_small_cell.append(lst[i])
                count += 1
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
