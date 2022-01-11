from Macro_Cell import *
from Small_Cell import *
from Const import *
from Auction import *
import matplotlib.pyplot as plt

DEBUG = 0
PROPOSED = 1
FIFO = 1
GREEDY = 1
MACRO_FIRST = 1
NO_SMALL = 1
if __name__ == "__main__":
    parameters = [[1e6, 1e6], [2e6, 2e6], [3e6, 3e6], [4e6, 4e6], [5e6, 5e6]]
    parameter = ["1Mcycles", "2Mcycles", "3Mcycles", "4Mcycles", "5Mcycles"]
    tasks_greedy = []
    tasks_proposed = []
    tasks_FIFO = []
    tasks_macro_cell_first = []
    tasks_no_small_cell = []
    for par in parameters:
        sum_greedy = 0
        sum_proposed = 0
        sum_FIFO = 0
        sum_macro_cell_first = 0
        sum_no_small_cell = 0
        for j in range(ITER):
            macro_cell_lst, small_cell_lst, total = Generate_task()
            if FIFO:
                winning_FIFO_macro_cell, winning_FIFO_small_cell = Fifo(
                    macro_cell_lst,
                    small_cell_lst,
                    total,
                    par[0] / macro_CPU_freq,
                    par[1] / small_CPU_freq,
                )
                sum_FIFO += len(winning_FIFO_macro_cell)
                sum_FIFO += len(winning_FIFO_small_cell)
            macro_cell_lst.sort(reverse=True)
            for lst in small_cell_lst:
                lst.sort(reverse=True)
            total.sort(reverse=True)
            if MACRO_FIRST:
                (
                    winning_macro_cell_first_macro_cell,
                    winning_macro_cell_first_small_cell,
                ) = macro_cell_first(
                    macro_cell_lst,
                    small_cell_lst,
                    total,
                    par[0] / macro_CPU_freq,
                    par[1] / small_CPU_freq,
                )
                sum_macro_cell_first += len(winning_macro_cell_first_macro_cell)
                sum_macro_cell_first += len(winning_macro_cell_first_small_cell)
            if GREEDY:
                winning_greedy_macro_cell, winning_greedy_small_cell = Greedy(
                    macro_cell_lst,
                    small_cell_lst,
                    total,
                    par[0] / macro_CPU_freq,
                    par[1] / small_CPU_freq,
                )
                sum_greedy += len(winning_greedy_macro_cell)
                sum_greedy += len(winning_greedy_small_cell)
            if NO_SMALL:
                winning_No_small_cell_macro_cell = No_small_cell(
                    macro_cell_lst,
                    small_cell_lst,
                    total,
                    par[0] / macro_CPU_freq,
                    par[1] / small_CPU_freq,
                )
                sum_no_small_cell += len(winning_No_small_cell_macro_cell)
                
            if PROPOSED:
                winning_macro_cell, winning_small_cell = Proposed(
                    macro_cell_lst,
                    small_cell_lst,
                    total,
                    par[0] / macro_CPU_freq,
                    par[1] / small_CPU_freq,
                )
                sum_proposed += len(winning_macro_cell)
                sum_proposed += len(winning_small_cell)

            
            if DEBUG:
                if j == 0:
                    print(
                        "################################################################"
                    )
                    print("First time Generated Tasks")
                    print(small_cell_lst)
                    print(macro_cell_lst)
                    print(
                        f"FIFO : {len(winning_FIFO_macro_cell)+len(winning_FIFO_small_cell)}"
                    )
                    print(winning_FIFO_small_cell)
                    print(winning_FIFO_macro_cell)
                    print(
                        f"Greedy : {len(winning_greedy_macro_cell)+len(winning_greedy_small_cell)}"
                    )
                    print(winning_greedy_small_cell)
                    print(winning_greedy_macro_cell)
                    print(
                        f"My Algorithm : {len(winning_macro_cell)+len(winning_small_cell)}"
                    )
                    print(winning_small_cell)
                    print(winning_macro_cell)
                    print(
                        f"macro_cell First : {len(winning_macro_cell_first_macro_cell)+len(winning_macro_cell_first_small_cell)}"
                    )
                    print(winning_macro_cell_first_small_cell)
                    print(winning_macro_cell_first_macro_cell)
                    print(f"No small_cell : {len(winning_No_small_cell_macro_cell)}")
                    print(winning_No_small_cell_macro_cell)
                    print(
                        "################################################################"
                    )
        print(f"Avg of task being allocate by FIFO : {sum_FIFO/ITER}")
        tasks_FIFO.append(sum_FIFO / ITER)
        print(f"Avg of task being allocate by Proposed algorithm : {sum_proposed/ITER}")
        tasks_proposed.append(sum_proposed / ITER)
        print(f"Avg of task being allocate by Greedy algorithm : {sum_greedy/ITER}")
        tasks_greedy.append(sum_greedy / ITER)
        print(
            f"Avg of task being allocate by macro cell First algorithm : {sum_macro_cell_first/ITER}"
        )
        tasks_macro_cell_first.append(sum_macro_cell_first / ITER)
        print(
            f"Avg of task being allocate by No small cell algorithm : {sum_no_small_cell/ITER}"
        )
        tasks_no_small_cell.append(sum_no_small_cell / ITER)
    plt.figure()
    plt.plot(
        parameter, tasks_proposed, marker="8", markerfacecolor="none", label="Proposed"
    )
    plt.plot(parameter, tasks_FIFO, marker="o", markerfacecolor="none", label="FIFO")
    plt.plot(
        parameter, tasks_greedy, marker="^", markerfacecolor="none", label="Greedy"
    )
    plt.plot(
        parameter,
        tasks_macro_cell_first,
        marker="p",
        markerfacecolor="none",
        label="macro cell First",
    )
    plt.plot(
        parameter,
        tasks_no_small_cell,
        marker=">",
        markerfacecolor="none",
        label="No small cell",
    )
    plt.legend(loc="best")
    plt.savefig('./Result.jpg')
