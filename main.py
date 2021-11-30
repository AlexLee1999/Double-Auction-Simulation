from Macro import *
from Micro import *
from Const import *
from Auction import *


if __name__ == "__main__":
    count1 = 0
    count2 = 0
    sum_greedy = 0
    sum_proposed = 0
    sum_FIFO = 0
    for j in range(ITER):
        macro_lst, micro_lst, total = Generate_task()
        winning_FIFO_macro = []
        winning_FIFO_micro = []
        macro_lst.sort(reverse=True)
        micro_lst.sort(reverse=True)
        total.sort(reverse=True)
        winning_greedy_macro, winning_greedy_micro = Greedy(macro_lst, micro_lst, total)

        winning_macro, winning_micro = Proposed(macro_lst, micro_lst, total)
        sum_FIFO += len(winning_FIFO_macro)
        sum_FIFO += len(winning_FIFO_micro)
        sum_greedy += len(winning_greedy_macro)
        sum_greedy += len(winning_greedy_micro)
        sum_proposed += len(winning_macro)
        sum_proposed += len(winning_micro)
        # if (len(winning_greedy_macro)+len(winning_greedy_micro)) > (len(winning_macro)+len(winning_micro)):
        #     count1 += 1
        #     if(len(winning_greedy_macro)+len(winning_greedy_micro)) - (len(winning_macro)+len(winning_micro)) > 1:
        #         print(micro_lst)
        #         print(macro_lst)
        #         print(
        #             f"Greedy : {len(winning_greedy_macro)+len(winning_greedy_micro)}")
        #         print(winning_greedy_micro)
        #         print(winning_greedy_macro)
        #         print(f"My Algorithm : {len(winning_macro)+len(winning_micro)}")
        #         print(winning_micro)
        #         print(winning_macro)
        #         print('\n')
        # if (len(winning_greedy_macro)+len(winning_greedy_micro)) < (len(winning_macro)+len(winning_micro)):
        #     count2 += 1
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
    # print(f'# of times that Greedy algorithm is better : {count1}')
    # print(f'# of times that My algorithm is better : {count2}')
    print(f'Avg of task being allocate by FIFO : {sum_FIFO/ITER}')
    print(f'Avg of task being allocate by My algorithm : {sum_proposed/ITER}')
    print(f'Avg of task being allocate by Greedy algorithm : {sum_greedy/ITER}')
