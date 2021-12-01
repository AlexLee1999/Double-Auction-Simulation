from Const import *
from Macro import *
from Micro import *


def Generate_task():
    macro_lst = []
    micro_lst = []
    total = []
    for _ in range(10):
        a = macro()
        b = micro()
        macro_lst.append(a)
        micro_lst.append(b)
        total.append(a)
        total.append(b)
    return macro_lst, micro_lst, total


def Proposed(macro_lst, micro_lst, total, macrot, microt):
    macro_lst = macro_lst.copy()
    micro_lst = micro_lst.copy()
    total = total.copy()
    winning_macro = []
    winning_micro = []
    for i in range(len(micro_lst)):
        b = (len(winning_micro)+1) * microt + time_to_micro
        if b <= micro_lst[i].time:
            winning_micro.append(micro_lst[i])
            total.remove(micro_lst[i])
    for i in range(len(total)):
        a = (len(winning_macro)+1) * macrot + time_to_macro
        if a <= total[i].time:
            winning_macro.append(total[i])
    return winning_macro, winning_micro


def Greedy(macro_lst, micro_lst, total, macrot, microt):
    winning_macro = []
    winning_micro = []
    macro_lst = macro_lst.copy()
    micro_lst = micro_lst.copy()
    total = total.copy()
    for i in range(len(total)):
        a = (len(winning_macro)+1)*macrot + time_to_macro
        b = (len(winning_micro)+1)*microt + time_to_micro
        if (total[i].ismacro == 0):
            if a < b and a <= total[i].time:
                winning_macro.append(total[i])
            elif a >= b and b <= total[i].time:
                winning_micro.append(total[i])
        else:
            if a <= total[i].time:
                winning_macro.append(total[i])
    return winning_macro, winning_micro


def FIFO(macro_lst, micro_lst, total, macrot, microt):
    winning_macro = []
    winning_micro = []
    macro_lst = macro_lst.copy()
    micro_lst = micro_lst.copy()
    total = total.copy()
    for i in range(len(micro_lst)):
        b = (len(winning_micro)+1) * microt + time_to_micro
        flag_current = False
        if b <= micro_lst[i].time:
            flag_current = True
        flag_lst = True
        for task in winning_micro:
            if task.time < b:
                flag_lst = False
        if flag_current and flag_lst:
            winning_micro.append(micro_lst[i])
            total.remove(micro_lst[i])
    for i in range(len(total)):
        a = (len(winning_macro)+1) * macrot + time_to_macro
        flag_current = False
        if a <= total[i].time:
            flag_current = True
        flag_lst = True
        for task in winning_macro:
            if task.time < a:
                flag_lst = False
        if flag_current and flag_lst:
            winning_macro.append(total[i])
    return winning_macro, winning_micro

def Macro_first(macro_lst, micro_lst, total, macrot, microt):
    macro_lst = macro_lst.copy()
    micro_lst = micro_lst.copy()
    total = total.copy()
    winning_macro = []
    winning_micro = []
    for i in range(len(macro_lst)):
        b = (len(winning_macro)+1) * macrot + time_to_macro
        if b <= macro_lst[i].time:
            winning_macro.append(macro_lst[i])
            total.remove(macro_lst[i])
    for i in range(len(micro_lst)):
        a = (len(winning_micro)+1) * microt + time_to_micro
        if a <= micro_lst[i].time:
            winning_micro.append(micro_lst[i])
    return winning_macro, winning_micro