from Macro import *
from Micro import *
from Const import *
from Auction import *
import matplotlib.pyplot as plt

if __name__ == "__main__":
    parameters = [[5, 8], [10, 20], [20, 30]]
    parameter = ["[5, 8]", "[10, 20]", "[20, 30]"]
    tasks_greedy = []
    tasks_proposed = []
    tasks_FIFO = []
    for par in parameters:
        sum_greedy = 0
        sum_proposed = 0
        sum_FIFO = 0
        for j in range(ITER):
            macro_lst, micro_lst, total = Generate_task()
            winning_FIFO_macro, winning_FIFO_micro = FIFO(
                macro_lst, micro_lst, total, par[0], par[1])
            macro_lst.sort(reverse=True)
            micro_lst.sort(reverse=True)
            total.sort(reverse=True)
            winning_greedy_macro, winning_greedy_micro = Greedy(
                macro_lst, micro_lst, total, par[0], par[1])
            winning_macro, winning_micro = Proposed(
                macro_lst, micro_lst, total, par[0], par[1])
            sum_FIFO += len(winning_FIFO_macro)
            sum_FIFO += len(winning_FIFO_micro)
            sum_greedy += len(winning_greedy_macro)
            sum_greedy += len(winning_greedy_micro)
            sum_proposed += len(winning_macro)
            sum_proposed += len(winning_micro)
            if j == 0:
                print('################################################################')
                print('First time Generated Tasks')
                print(micro_lst)
                print(macro_lst)
                print(f"FIFO : {len(winning_FIFO_macro)+len(winning_FIFO_micro)}")
                print(winning_FIFO_micro)
                print(winning_FIFO_macro)
                print(
                    f"Greedy : {len(winning_greedy_macro)+len(winning_greedy_micro)}")
                print(winning_greedy_micro)
                print(winning_greedy_macro)
                print(f"My Algorithm : {len(winning_macro)+len(winning_micro)}")
                print(winning_micro)
                print(winning_macro)
                print('################################################################')
        print(f'Avg of task being allocate by FIFO : {sum_FIFO/ITER}')
        tasks_FIFO.append(sum_FIFO/ITER)
        print(
            f'Avg of task being allocate by Proposed algorithm : {sum_proposed/ITER}')
        tasks_proposed.append(sum_proposed/ITER)
        print(
            f'Avg of task being allocate by Greedy algorithm : {sum_greedy/ITER}')
        tasks_greedy.append(sum_greedy/ITER)
    plt.figure()
    plt.plot(parameter, tasks_FIFO, marker='o',
             markerfacecolor='none', label='FIFO')
    plt.plot(parameter, tasks_greedy, marker='^',
             markerfacecolor='none', label='Greedy')
    plt.plot(parameter, tasks_proposed, marker='8',
             markerfacecolor='none', label='Proposed')
    plt.legend(loc="best")
    plt.show()
