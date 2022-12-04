import numpy as np
import re
from timeit import timeit
from math import floor
from functools import reduce

class Range:
    def __init__(self, string) -> None:
        arr = string.split("-")
        lower, higher = arr[0], arr[1]
        self.lower = int(lower)
        self.higher = int(higher)
         
    # def lower(self):
    #     return self.lower
    # def higher(self):
    #     return self.higher

    def fully_contains(self, x):
        is_contained = False
        if x.lower >= self.lower and x.higher <= self.higher:
            is_contained = True
        else: return False
        return is_contained

    def partialy_contains(self, x):
        is_contained = False
        if (x.lower >= self.lower and x.lower <= self.higher )or (x.higher <= self.higher and x.higher >= self.lower):
            is_contained = True
        else: return False
        return is_contained


def task_one():
    points: int = 0

    with open("input-4.txt", "r") as file:
        file_data = file.read()
        codes = file_data.strip().split("\n")     
        
        for string in list(codes):
            arr = string.split(",")
            lower_range = Range(arr[0])
            higher_range = Range(arr[1])
            if(lower_range.fully_contains(higher_range) or higher_range.fully_contains(lower_range)):
                points += 1

    print(f'answer 1: {points}')

def task_two():
    points: int = 0

    with open("input-4.txt", "r") as file:
        file_data = file.read()
        codes = file_data.strip().split("\n")     
        
        for string in list(codes):
            arr = string.split(",")
            lower_range = Range(arr[0])
            higher_range = Range(arr[1])
            if(lower_range.partialy_contains(higher_range) or higher_range.partialy_contains(lower_range)):
                points += 1

    print(f'answer 2: {points}')



# sprobowac z zamiana na liczby, wtedy to bedzie dzikie bo +2 wygrywa +1 przegyrwa a 0 to draw

if __name__ == "__main__":


    for i in [task_one, task_two]:
        elapsed = timeit(i, number=1)
        print(f"elapsed seconds {i.__name__}: {elapsed}")