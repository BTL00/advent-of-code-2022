import numpy as np
import re
from timeit import timeit
from math import floor
from functools import reduce

# class LinkedList:
#     def __init__(self, chars: str) -> None:
#         if chars == "   ":
#             self.content: str = ""
#         elif re.match("\[\w\]", chars):
#             self.content: str = re.search("\[(\w)\]", chars).groups()[0]
#         else: 
#              Exception
#         self.next = None
#     def add(self,chars):
#         if self.next is None:
#             self.next = LinkedList(chars)
#         else:
#             self.next.add(chars)
#     def push(self, element):
#         if self.next is None:
#             self.next = element
#         else:
#             self.next.push(element)
#     def take2(self, n):
#         this: LinkedList
#         next: LinkedList = self.next
       
#         if n == 1: 
#             next = self.next
#             self.next = None
#             return self, next
#         elif n>1:
#             out1, outn = self.next.take2(n-1)
#             return self , outn




#     def take(self, n, is_first):
#         elements: dict[LinkedList]
#         if self.next is None and n != 1:
#             return Exception
#         elif self.next is not None and n > 1:
#             not_important, left = self.next.take(n - 1, False)
#             if is_first:
#                 return self, [not_important] + [left]
#             else:
#                 return  self, [not_important] + [left]
#         elif n == 1:
#             next = self.next
#             self.next = None
#             return self, next
#         else:
#             Exception

#     def setNthNone(self, n):
#         if n == 1:
#             self.next = None
#         else:
#             self.next.setNthNone(n-1)
        
    # def __str__(self) -> str:
    #     output = self.content
    #     if self.next is not None:
    #         output += str(self.next)
    #     return output
    # def first(self):
    #     return self.content

def getChar(text):
    return re.search("\[(\w)\]", text).groups()[0]


# def task_two():
#     points: int = 0
#     lists: dict[LinkedList] = {}
#     first_line = True
#     start_sorting = False
#     with open("input-5.txt", "r") as file:
#         file_line = file.readline()
#         while file_line:
#             line_array = list(file_line)
#             if re.match(r"\s1\s\s\s2.*", file_line):
#                 file_line = file.readline()
#                 file_line = file.readline()
#                 start_sorting = True
#             if start_sorting:
#                 task = re.search(r"move (\d+) from (\d+) to (\d+)", file_line).groups()
#                 how_many = int(task[0])
#                 from_stack = int(task[1]) -1
#                 to_stack = int(task[2]) - 1

#                 elements_to_add = lists[from_stack]
#                 for i in range(0, how_many):
#                    next = elements_to_add.next
#                 left = next
#                 elements_to_add.setNthNone(how_many)
                
#                 # elements_to_add, left = lists[from_stack].take2(how_many)
#                 lists[from_stack] = left
#                 elements_pushed = lists[to_stack]
#                 elements_to_add.push(elements_pushed)
#                 lists[to_stack] = elements_to_add
            
#             else:
#             # if re.match(" 1  .*",file_line): break
#                 if first_line:
#                     for short in range(0, len(line_array)-3, 4):
#                         if file_line[short:short+3] != '   ':
#                             lists[short//4] = LinkedList(file_line[short:short+3])
#                         print(file_line[short:short+3])
#                     first_line = False
#                 else:
#                     for short in range(0, len(line_array)-3, 4):
#                         if file_line[short:short+3] != '   ':
#                             if short//4 in lists.keys() and lists[short//4] != '':
#                                 lists[short//4].add(file_line[short:short+3])
#                             else:
#                                 lists[short//4] = LinkedList(file_line[short:short+3])
#                         print(file_line[short:short+3])



#             file_line = file.readline()

#     for element in lists:
#         print(str(element))
    

#     print(f'answer 2: ')
#     for element in sorted(lists.keys()):
#         print(lists[element].first())

def task_one_simple():
    points: int = 0
    lists: dict[str] = {}
    first_line = True
    start_sorting = False
    with open("input-5.txt", "r") as file:
        file_line = file.readline()
        while file_line:
            line_array = list(file_line)
            if re.match(r"\s1\s\s\s2.*", file_line):
                file_line = file.readline()
                file_line = file.readline()
                start_sorting = True
                for i,x in lists.items():
                    lists[i] = str(x[::-1])
            if start_sorting:
                task = re.search(r"move (\d+) from (\d+) to (\d+)", file_line).groups()
                how_many = int(task[0])
                from_stack = int(task[1]) -1
                to_stack = int(task[2]) - 1

                for i in range(0, how_many):
                    lists[to_stack] += list(lists[from_stack]).pop()
                    trim_length = len(lists[from_stack]) -1
                    lists[from_stack]  = str(lists[from_stack][:trim_length])
            
            else:
                if first_line:
                    for short in range(0, len(line_array)-3, 4):
                        if file_line[short:short+3] != '   ':
                            lists[short//4] = getChar(file_line[short:short+3])
                        print(file_line[short:short+3])
                    first_line = False
                else:
                    for short in range(0, len(line_array)-3, 4):
                        if file_line[short:short+3] != '   ':
                            if short//4 in lists.keys():
                                lists[short//4] += getChar(file_line[short:short+3])
                            else:
                                lists[short//4] = getChar(file_line[short:short+3])
                        print(file_line[short:short+3])

            file_line = file.readline()
    for element in lists:
        print(str(element))
    

    print(f'answer 1: ')
    for element in sorted(lists.keys()):
        print(list(lists[element]).pop())






def task_two_simple():
    points: int = 0
    lists: dict[str] = {}
    first_line = True
    start_sorting = False
    with open("input-5.txt", "r") as file:
        file_line = file.readline()
        while file_line:
            line_array = list(file_line)
            if re.match(r"\s1\s\s\s2.*", file_line):
                file_line = file.readline()
                file_line = file.readline()
                start_sorting = True
                for i,x in lists.items():
                    lists[i] = str(x[::-1])
            if start_sorting:
                task = re.search(r"move (\d+) from (\d+) to (\d+)", file_line).groups()
                how_many = int(task[0])
                from_stack = int(task[1]) -1
                to_stack = int(task[2]) - 1


                # input_list_length = len(lists[from_stack])
                # elements_to_add = list(lists[from_stack])[input_list_length-how_many:input_list_length]
                # lists[to_stack] += str(elements_to_add)
                
                # lists[from_stack]  = str(lists[from_stack][:input_list_length-how_many])
                to_push = ""
                for i in range(0, how_many):
                    to_push += list(lists[from_stack]).pop()
                    trim_length = len(lists[from_stack]) -1
                    lists[from_stack]  = str(lists[from_stack][:trim_length])
                lists[to_stack] += to_push[::-1]

            else:
                if first_line:
                    for short in range(0, len(line_array)-3, 4):
                        if file_line[short:short+3] != '   ':
                            lists[short//4] = getChar(file_line[short:short+3])
                        print(file_line[short:short+3])
                    first_line = False
                else:
                    for short in range(0, len(line_array)-3, 4):
                        if file_line[short:short+3] != '   ':
                            if short//4 in lists.keys():
                                lists[short//4] += getChar(file_line[short:short+3])
                            else:
                                lists[short//4] = getChar(file_line[short:short+3])
                        print(file_line[short:short+3])

            file_line = file.readline()
    for element in lists:
        print(str(element))
    

    print(f'answer 2: ')
    for element in sorted(lists.keys()):
        print(list(lists[element]).pop())





if __name__ == "__main__":


    for i in [task_one_simple, task_two_simple]:
        elapsed = timeit(i, number=1)
        print(f"elapsed seconds {i.__name__}: {elapsed}")