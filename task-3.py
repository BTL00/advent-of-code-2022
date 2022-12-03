import numpy as np
import re
from timeit import timeit
from math import floor
from functools import reduce

def priority(l):
    x = ord(l)
    if(l.islower()):
         return x - 97 + 1
    else:
        return x - 65 + 27

def task_one():
    points: int = 0

    with open("input-3.txt", "r") as file:
        file_data = file.read()
        codes = file_data.strip().split("\n")     
        
        for arr in list(codes):
                # print("----------")
                end = set(arr[len(arr)//2:])
                begining  = set(arr[0:len(arr)//2])
                inter = begining.intersection(end)
                # print(begining)
                # print(end)
                for i in inter:
                        # print(f'i {i}')
                        # print(priority(i))
                        points += priority(i)
        print(reduce(lambda x,arr: x+reduce(lambda a,b: a+priority(b), set(arr[0:len(arr)//2]).intersection( set(arr[len(arr)//2:])), 0), list(codes) ,0))



    print(f'answer 1: {points}')

def task_two():
    points: int = 0

    with open("input-3.txt", "r") as file:
        file_data = file.read()
        codes = file_data.strip().split("\n")     
        list_of_codes = list(codes)
        for index in range(0, len(list_of_codes), 3):
                # print(index)
                first = set(list_of_codes[index])
                second = set(list_of_codes[index+1])
                third = set(list_of_codes[index+2])
                # print("----------")
                inter = first.intersection(second).intersection(third)
                for i in inter:
                        # print(f'i {i}')
                        # print(priority(i))
                        points += priority(i)

    print(f'answer 2: {points}')



# sprobowac z zamiana na liczby, wtedy to bedzie dzikie bo +2 wygrywa +1 przegyrwa a 0 to draw

if __name__ == "__main__":


    for i in [task_one, task_two]:
        elapsed = timeit(i, number=1)
        print(f"elapsed seconds {i.__name__}: {elapsed}")