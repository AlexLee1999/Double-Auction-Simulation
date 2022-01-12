from Macro_Cell import *
from Small_Cell import *

class System():
    def __init__(self, macro_cell_user_num, small_num, small_cell_user_num):
        self._macro_cell_user = macro_cell_user_num
        self._small_num = small_num
        self._small_cell_user = small_cell_user_num
        self._macro_cell_lst = []
        self._small_cell_lst = []
        self._total = []
        self.Generate_task(macro_cell_user_num, small_num, small_cell_user_num)
        
        
    def Generate_task(self, macro_cell_user_num, small_num, small_cell_user_num):
        for _ in range(macro_cell_user_num):
            a = macro_cell_user()
            self._macro_cell_lst.append(a)
            self._total.append(a)
            
        for i in range(small_num):
            small_cell_user_lst = []
            for _ in range(small_cell_user_num):
                b = small_cell_user(i)
                small_cell_user_lst.append(b)
                self._total.append(b)
            self._small_cell_lst.append(small_cell_user_lst)
    
    @property
    def macro_cell_lst(self):
        return self._macro_cell_lst
    
    @property
    def small_cell_lst(self):
        return self._small_cell_lst
    
    @property
    def total(self):
        return self._total