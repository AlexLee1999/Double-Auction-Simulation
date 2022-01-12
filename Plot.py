from Const import *
from System import *
from Auction import *
import matplotlib.pyplot as plt
from tqdm import tqdm

def cpu_cycles():
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
        i = 0
        pbar = tqdm(total=ITER)
        while i < ITER:
            system = System(MACRO_CELL_USER_NUM,
                            SMALL_NUM, SMALL_CELL_USER_NUM)
            if FIFO:
                winning_FIFO_macro_cell, winning_FIFO_small_cell = Fifo(
                    system.macro_cell_lst,
                    system.small_cell_lst,
                    system.total,
                    par[0] / MACRO_CPU_FREQ,
                    par[1] / SMALL_CPU_FREQ,
                    TIME_TO_MACRO_CELL,
                    TIME_TO_SMALL_CELL,
                )
                sum_FIFO += len(winning_FIFO_macro_cell)
                sum_FIFO += len(winning_FIFO_small_cell)
            system.macro_cell_lst.sort(reverse=True)
            for lst in system.small_cell_lst:
                lst.sort(reverse=True)
            system.total.sort(reverse=True)
            if MACRO_FIRST:
                (
                    winning_macro_cell_first_macro_cell,
                    winning_macro_cell_first_small_cell,
                ) = macro_cell_first(
                    system.macro_cell_lst,
                    system.small_cell_lst,
                    system.total,
                    par[0] / MACRO_CPU_FREQ,
                    par[1] / SMALL_CPU_FREQ,
                    TIME_TO_MACRO_CELL,
                    TIME_TO_SMALL_CELL,
                )
                sum_macro_cell_first += len(
                    winning_macro_cell_first_macro_cell)
                sum_macro_cell_first += len(
                    winning_macro_cell_first_small_cell)
            if GREEDY:
                winning_greedy_macro_cell, winning_greedy_small_cell = Greedy(
                    system.macro_cell_lst,
                    system.small_cell_lst,
                    system.total,
                    par[0] / MACRO_CPU_FREQ,
                    par[1] / SMALL_CPU_FREQ,
                    TIME_TO_MACRO_CELL,
                    TIME_TO_SMALL_CELL,
                )
                sum_greedy += len(winning_greedy_macro_cell)
                sum_greedy += len(winning_greedy_small_cell)
            if NO_SMALL:
                winning_No_small_cell_macro_cell = No_small_cell(
                    system.macro_cell_lst,
                    system.small_cell_lst,
                    system.total,
                    par[0] / MACRO_CPU_FREQ,
                    par[1] / SMALL_CPU_FREQ,
                    TIME_TO_MACRO_CELL,
                    TIME_TO_SMALL_CELL,
                )
                sum_no_small_cell += len(winning_No_small_cell_macro_cell)

            if PROPOSED:
                winning_macro_cell, winning_small_cell = Proposed(
                    system.macro_cell_lst,
                    system.small_cell_lst,
                    system.total,
                    par[0] / MACRO_CPU_FREQ,
                    par[1] / SMALL_CPU_FREQ,
                    TIME_TO_MACRO_CELL,
                    TIME_TO_SMALL_CELL,
                )
                sum_proposed += len(winning_macro_cell)
                sum_proposed += len(winning_small_cell)

            if DEBUG:
                if i == 0:
                    print("First time Generated Tasks")
                    print(system.small_cell_lst)
                    print(system.macro_cell_lst)
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
                    print(
                        f"No small_cell : {len(winning_No_small_cell_macro_cell)}")
                    print(winning_No_small_cell_macro_cell)
            i += 1
            pbar.update(1)
        if DEBUG:
            print(par)
            print(f"Avg of task being allocate by FIFO : {sum_FIFO/ITER}")
            print(
                f"Avg of task being allocate by Proposed algorithm : {sum_proposed/ITER}")
            print(
                f"Avg of task being allocate by Greedy algorithm : {sum_greedy/ITER}")
            print(
                f"Avg of task being allocate by macro cell First algorithm : {sum_macro_cell_first/ITER}"
            )
            print(
                f"Avg of task being allocate by No small cell algorithm : {sum_no_small_cell/ITER}"
            )
        tasks_FIFO.append(sum_FIFO / ITER)
        tasks_proposed.append(sum_proposed / ITER)
        tasks_greedy.append(sum_greedy / ITER)
        tasks_macro_cell_first.append(sum_macro_cell_first / ITER)
        tasks_no_small_cell.append(sum_no_small_cell / ITER)
    plt.figure()
    plt.plot(
        parameter, tasks_proposed, marker="s", markerfacecolor="none", label="Proposed"
    )
    plt.plot(parameter, tasks_FIFO, marker="o",
             markerfacecolor="none", label="FIFO")
    plt.plot(
        parameter, tasks_greedy, marker="^", markerfacecolor="none", label="Greedy"
    )
    plt.plot(
        parameter,
        tasks_macro_cell_first,
        marker="p",
        markerfacecolor="none",
        label="Macro Cell First",
    )
    plt.plot(
        parameter,
        tasks_no_small_cell,
        marker=">",
        markerfacecolor="none",
        label="No Small Cell",
    )
    plt.legend(loc="best")
    plt.savefig('./Pics/CPU_CYCLE_Result.pdf')


def small_cells_nums():
    parameters = [5, 10, 15, 20]
    parameter = ["5", "10", "15", "20"]
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
        i = 0
        pbar = tqdm(total=ITER)
        while i < ITER:
            system = System(MACRO_CELL_USER_NUM,
                            par, SMALL_CELL_USER_NUM)
            if FIFO:
                winning_FIFO_macro_cell, winning_FIFO_small_cell = Fifo(
                    system.macro_cell_lst,
                    system.small_cell_lst,
                    system.total,
                    TASK_SIZE / MACRO_CPU_FREQ,
                    TASK_SIZE / SMALL_CPU_FREQ,
                    TIME_TO_MACRO_CELL,
                    TIME_TO_SMALL_CELL,
                )
                sum_FIFO += len(winning_FIFO_macro_cell)
                sum_FIFO += len(winning_FIFO_small_cell)
            system.macro_cell_lst.sort(reverse=True)
            for lst in system.small_cell_lst:
                lst.sort(reverse=True)
            system.total.sort(reverse=True)
            if MACRO_FIRST:
                (
                    winning_macro_cell_first_macro_cell,
                    winning_macro_cell_first_small_cell,
                ) = macro_cell_first(
                    system.macro_cell_lst,
                    system.small_cell_lst,
                    system.total,
                    TASK_SIZE / MACRO_CPU_FREQ,
                    TASK_SIZE / SMALL_CPU_FREQ,
                    TIME_TO_MACRO_CELL,
                    TIME_TO_SMALL_CELL,
                )
                sum_macro_cell_first += len(
                    winning_macro_cell_first_macro_cell)
                sum_macro_cell_first += len(
                    winning_macro_cell_first_small_cell)
            if GREEDY:
                winning_greedy_macro_cell, winning_greedy_small_cell = Greedy(
                    system.macro_cell_lst,
                    system.small_cell_lst,
                    system.total,
                    TASK_SIZE / MACRO_CPU_FREQ,
                    TASK_SIZE / SMALL_CPU_FREQ,
                    TIME_TO_MACRO_CELL,
                    TIME_TO_SMALL_CELL,
                )
                sum_greedy += len(winning_greedy_macro_cell)
                sum_greedy += len(winning_greedy_small_cell)
            if NO_SMALL:
                winning_No_small_cell_macro_cell = No_small_cell(
                    system.macro_cell_lst,
                    system.small_cell_lst,
                    system.total,
                    TASK_SIZE / MACRO_CPU_FREQ,
                    TASK_SIZE / SMALL_CPU_FREQ,
                    TIME_TO_MACRO_CELL,
                    TIME_TO_SMALL_CELL,
                )
                sum_no_small_cell += len(winning_No_small_cell_macro_cell)

            if PROPOSED:
                winning_macro_cell, winning_small_cell = Proposed(
                    system.macro_cell_lst,
                    system.small_cell_lst,
                    system.total,
                    TASK_SIZE / MACRO_CPU_FREQ,
                    TASK_SIZE / SMALL_CPU_FREQ,
                    TIME_TO_MACRO_CELL,
                    TIME_TO_SMALL_CELL,
                )
                sum_proposed += len(winning_macro_cell)
                sum_proposed += len(winning_small_cell)

            if DEBUG:
                if i == 0:
                    
                    print("First time Generated Tasks")
                    print(system.small_cell_lst)
                    print(system.macro_cell_lst)
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
                    print(
                        f"No small_cell : {len(winning_No_small_cell_macro_cell)}")
                    print(winning_No_small_cell_macro_cell)
                    
            i += 1
            pbar.update(1)
        if DEBUG:
            print(par)
            print(f"Avg of task being allocate by FIFO : {sum_FIFO/ITER}")
            print(
                f"Avg of task being allocate by Proposed algorithm : {sum_proposed/ITER}")
            print(
                f"Avg of task being allocate by Greedy algorithm : {sum_greedy/ITER}")
            print(
                f"Avg of task being allocate by macro cell First algorithm : {sum_macro_cell_first/ITER}"
            )
            print(
                f"Avg of task being allocate by No small cell algorithm : {sum_no_small_cell/ITER}"
            )
        tasks_FIFO.append(sum_FIFO / ITER)
        tasks_proposed.append(sum_proposed / ITER)
        tasks_greedy.append(sum_greedy / ITER)
        tasks_macro_cell_first.append(sum_macro_cell_first / ITER)
        tasks_no_small_cell.append(sum_no_small_cell / ITER)
    plt.figure()
    plt.plot(
        parameter, tasks_proposed, marker="s", markerfacecolor="none", label="Proposed"
    )
    plt.plot(parameter, tasks_FIFO, marker="o",
             markerfacecolor="none", label="FIFO")
    plt.plot(
        parameter, tasks_greedy, marker="^", markerfacecolor="none", label="Greedy"
    )
    plt.plot(
        parameter,
        tasks_macro_cell_first,
        marker="p",
        markerfacecolor="none",
        label="Macro Cell First",
    )
    plt.plot(
        parameter,
        tasks_no_small_cell,
        marker=">",
        markerfacecolor="none",
        label="No Small Cell",
    )
    plt.legend(loc="best")
    plt.savefig('./Pics/SMALL_CELL_NUM_Result.pdf')


def transmission_time():
    parameters = [[1E-3, 2E-3], [5E-3, 7E-3],
                  [10E-3, 13E-3], [15E-3, 17E-3], [20E-3, 25E-3]]
    parameter = ["1ms, 2ms", "5ms, 7ms",
                 "10ms, 13ms", "15ms, 17ms", "20ms, 25ms"]
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
        i = 0
        pbar = tqdm(total=ITER)
        while i < ITER:
            system = System(MACRO_CELL_USER_NUM,
                            SMALL_NUM, SMALL_CELL_USER_NUM)
            if FIFO:
                winning_FIFO_macro_cell, winning_FIFO_small_cell = Fifo(
                    system.macro_cell_lst,
                    system.small_cell_lst,
                    system.total,
                    TASK_SIZE / MACRO_CPU_FREQ,
                    TASK_SIZE / SMALL_CPU_FREQ,
                    par[0],
                    par[1],
                )
                sum_FIFO += len(winning_FIFO_macro_cell)
                sum_FIFO += len(winning_FIFO_small_cell)
            system.macro_cell_lst.sort(reverse=True)
            for lst in system.small_cell_lst:
                lst.sort(reverse=True)
            system.total.sort(reverse=True)
            if MACRO_FIRST:
                (
                    winning_macro_cell_first_macro_cell,
                    winning_macro_cell_first_small_cell,
                ) = macro_cell_first(
                    system.macro_cell_lst,
                    system.small_cell_lst,
                    system.total,
                    TASK_SIZE / MACRO_CPU_FREQ,
                    TASK_SIZE / SMALL_CPU_FREQ,
                    par[0],
                    par[1],
                )
                sum_macro_cell_first += len(
                    winning_macro_cell_first_macro_cell)
                sum_macro_cell_first += len(
                    winning_macro_cell_first_small_cell)
            if GREEDY:
                winning_greedy_macro_cell, winning_greedy_small_cell = Greedy(
                    system.macro_cell_lst,
                    system.small_cell_lst,
                    system.total,
                    TASK_SIZE / MACRO_CPU_FREQ,
                    TASK_SIZE / SMALL_CPU_FREQ,
                    par[0],
                    par[1],
                )
                sum_greedy += len(winning_greedy_macro_cell)
                sum_greedy += len(winning_greedy_small_cell)
            if NO_SMALL:
                winning_No_small_cell_macro_cell = No_small_cell(
                    system.macro_cell_lst,
                    system.small_cell_lst,
                    system.total,
                    TASK_SIZE / MACRO_CPU_FREQ,
                    TASK_SIZE / SMALL_CPU_FREQ,
                    par[0],
                    par[1],
                )
                sum_no_small_cell += len(winning_No_small_cell_macro_cell)

            if PROPOSED:
                winning_macro_cell, winning_small_cell = Proposed(
                    system.macro_cell_lst,
                    system.small_cell_lst,
                    system.total,
                    TASK_SIZE / MACRO_CPU_FREQ,
                    TASK_SIZE / SMALL_CPU_FREQ,
                    par[0],
                    par[1],
                )
                sum_proposed += len(winning_macro_cell)
                sum_proposed += len(winning_small_cell)

            if DEBUG:
                if i == 0:
                    
                    print("First time Generated Tasks")
                    print(system.small_cell_lst)
                    print(system.macro_cell_lst)
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
                    print(
                        f"No small_cell : {len(winning_No_small_cell_macro_cell)}")
                    print(winning_No_small_cell_macro_cell)
                    
            i += 1
            pbar.update(1)
        if DEBUG:
            print(par)
            print(f"Avg of task being allocate by FIFO : {sum_FIFO/ITER}")
            print(
                f"Avg of task being allocate by Proposed algorithm : {sum_proposed/ITER}")
            print(
                f"Avg of task being allocate by Greedy algorithm : {sum_greedy/ITER}")
            print(
                f"Avg of task being allocate by macro cell First algorithm : {sum_macro_cell_first/ITER}"
            )
            print(
                f"Avg of task being allocate by No small cell algorithm : {sum_no_small_cell/ITER}"
            )
        tasks_FIFO.append(sum_FIFO / ITER)
        tasks_proposed.append(sum_proposed / ITER)
        tasks_greedy.append(sum_greedy / ITER)
        tasks_macro_cell_first.append(sum_macro_cell_first / ITER)
        tasks_no_small_cell.append(sum_no_small_cell / ITER)
    plt.figure()
    plt.plot(
        parameter, tasks_proposed, marker="s", markerfacecolor="none", label="Proposed"
    )
    plt.plot(parameter, tasks_FIFO, marker="o",
             markerfacecolor="none", label="FIFO")
    plt.plot(
        parameter, tasks_greedy, marker="^", markerfacecolor="none", label="Greedy"
    )
    plt.plot(
        parameter,
        tasks_macro_cell_first,
        marker="p",
        markerfacecolor="none",
        label="Macro Cell First",
    )
    plt.plot(
        parameter,
        tasks_no_small_cell,
        marker=">",
        markerfacecolor="none",
        label="No Small Cell",
    )
    plt.legend(loc="best")
    plt.savefig('./Pics/TRANSMISSION_Result.pdf')
    
def cell_capacity():
    parameters = [[5e8, 5e7], [7.5e8, 7.5e7], [1e9, 1e8], [2.5e9, 2.5e8], [5e9, 5e8]]
    parameter = ["500MHz, 50MHz", "750MHz, 75MHz", "1GHz, 100MHz", "2.5GHz, 250MHz", "5Gz, 500MHz"]
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
        i = 0
        pbar = tqdm(total=ITER)
        while i < ITER:
            system = System(MACRO_CELL_USER_NUM,
                            SMALL_NUM, SMALL_CELL_USER_NUM)
            if FIFO:
                winning_FIFO_macro_cell, winning_FIFO_small_cell = Fifo(
                    system.macro_cell_lst,
                    system.small_cell_lst,
                    system.total,
                    TASK_SIZE / par[0],
                    TASK_SIZE / par[1],
                    TIME_TO_MACRO_CELL,
                    TIME_TO_SMALL_CELL,
                )
                sum_FIFO += len(winning_FIFO_macro_cell)
                sum_FIFO += len(winning_FIFO_small_cell)
            system.macro_cell_lst.sort(reverse=True)
            for lst in system.small_cell_lst:
                lst.sort(reverse=True)
            system.total.sort(reverse=True)
            if MACRO_FIRST:
                (
                    winning_macro_cell_first_macro_cell,
                    winning_macro_cell_first_small_cell,
                ) = macro_cell_first(
                    system.macro_cell_lst,
                    system.small_cell_lst,
                    system.total,
                    TASK_SIZE / par[0],
                    TASK_SIZE / par[1],
                    TIME_TO_MACRO_CELL,
                    TIME_TO_SMALL_CELL,
                )
                sum_macro_cell_first += len(
                    winning_macro_cell_first_macro_cell)
                sum_macro_cell_first += len(
                    winning_macro_cell_first_small_cell)
            if GREEDY:
                winning_greedy_macro_cell, winning_greedy_small_cell = Greedy(
                    system.macro_cell_lst,
                    system.small_cell_lst,
                    system.total,
                    TASK_SIZE / par[0],
                    TASK_SIZE / par[1],
                    TIME_TO_MACRO_CELL,
                    TIME_TO_SMALL_CELL,
                )
                sum_greedy += len(winning_greedy_macro_cell)
                sum_greedy += len(winning_greedy_small_cell)
            if NO_SMALL:
                winning_No_small_cell_macro_cell = No_small_cell(
                    system.macro_cell_lst,
                    system.small_cell_lst,
                    system.total,
                    TASK_SIZE / par[0],
                    TASK_SIZE / par[1],
                    TIME_TO_MACRO_CELL,
                    TIME_TO_SMALL_CELL,
                )
                sum_no_small_cell += len(winning_No_small_cell_macro_cell)

            if PROPOSED:
                winning_macro_cell, winning_small_cell = Proposed(
                    system.macro_cell_lst,
                    system.small_cell_lst,
                    system.total,
                    TASK_SIZE / par[0],
                    TASK_SIZE / par[1],
                    TIME_TO_MACRO_CELL,
                    TIME_TO_SMALL_CELL,
                )
                sum_proposed += len(winning_macro_cell)
                sum_proposed += len(winning_small_cell)

            if DEBUG:
                if i == 0:
                    print("First time Generated Tasks")
                    print(system.small_cell_lst)
                    print(system.macro_cell_lst)
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
                    print(
                        f"No small_cell : {len(winning_No_small_cell_macro_cell)}")
                    print(winning_No_small_cell_macro_cell)
            i += 1
            pbar.update(1)
        if DEBUG:
            print(par)
            print(f"Avg of task being allocate by FIFO : {sum_FIFO/ITER}")
            print(
                f"Avg of task being allocate by Proposed algorithm : {sum_proposed/ITER}")
            print(
                f"Avg of task being allocate by Greedy algorithm : {sum_greedy/ITER}")
            print(
                f"Avg of task being allocate by macro cell First algorithm : {sum_macro_cell_first/ITER}"
            )
            print(
                f"Avg of task being allocate by No small cell algorithm : {sum_no_small_cell/ITER}"
            )
        tasks_FIFO.append(sum_FIFO / ITER)
        tasks_proposed.append(sum_proposed / ITER)
        tasks_greedy.append(sum_greedy / ITER)
        tasks_macro_cell_first.append(sum_macro_cell_first / ITER)
        tasks_no_small_cell.append(sum_no_small_cell / ITER)
    plt.figure()
    plt.plot(
        parameter, tasks_proposed, marker="s", markerfacecolor="none", label="Proposed"
    )
    plt.plot(parameter, tasks_FIFO, marker="o",
             markerfacecolor="none", label="FIFO")
    plt.plot(
        parameter, tasks_greedy, marker="^", markerfacecolor="none", label="Greedy"
    )
    plt.plot(
        parameter,
        tasks_macro_cell_first,
        marker="p",
        markerfacecolor="none",
        label="Macro Cell First",
    )
    plt.plot(
        parameter,
        tasks_no_small_cell,
        marker=">",
        markerfacecolor="none",
        label="No Small Cell",
    )
    plt.legend(loc="best")
    plt.savefig('./Pics/CELL_CAPICITY_Result.pdf')