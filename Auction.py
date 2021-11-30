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


def Proposed(macro_lst, micro_lst, total):
    winning_macro = []
    winning_micro = []
    for i in range(len(micro_lst)):
        b = (len(winning_micro)+1) * microt
        if b <= micro_lst[i].time:
            winning_micro.append(micro_lst[i])
            total.remove(micro_lst[i])
    for i in range(len(total)):
        a = (len(winning_macro)+1) * macrot
        if a <= total[i].time:
            winning_macro.append(total[i])
    return winning_macro, winning_micro


def Greedy(macro_lst, micro_lst, total):
    winning_macro = []
    winning_micro = []
    for i in range(len(total)):
        a = (len(winning_macro)+1)*macrot
        b = (len(winning_micro)+1)*microt
        if (total[i].ismacro == 0):
            if a < b and a <= total[i].time:
                winning_macro.append(total[i])
            elif a >= b and b <= total[i].time:
                winning_micro.append(total[i])
        else:
            if a <= total[i].time:
                winning_macro.append(total[i])
    return winning_macro, winning_micro

def FIFO(macro_lst, micro_lst, total):
    winning_macro = []
    winning_micro = []
    for i in range(len(micro_lst)):
        b = (len(winning_micro)+1) * microt
        if b <= micro_lst[i].time:
            winning_micro.append(micro_lst[i])
            total.remove(micro_lst[i])
    for i in range(len(total)):
        a = (len(winning_macro)+1) * macrot
        if a <= total[i].time:
            winning_macro.append(total[i])
    return winning_macro, winning_micro