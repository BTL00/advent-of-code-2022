import numpy
import re
from timeit import timeit

def task_one():
    # opponent
    # A rock
    # B paper
    # C scizzors
    # you
    # X rock
    # Y paper
    # Z scissors


    # dict_loses = {'A': 'Z', 'B': 'X', 'C' : 'Y'} # A beats : [Z] so user loses # 0 points
    # dict_draws = {'A': 'X', 'B': 'Y', 'C' : 'Z'} # 3 points
    # dict_wins = {'A': 'Y', 'B': 'Z', 'C': 'X'} # Y beats A so user wins # 6 poinst


    list_loses = [('A', 'Z'), ('B', 'X'), ('C', 'Y')] # A beats : [Z] so user loses # 0 points
    list_draws = [('A', 'X'), ('B', 'Y'), ('C', 'Z')] # 3 points
    list_wins = [('A', 'Y'), ('B', 'Z'), ('C', 'X')] # Y beats A so user wins # 6 poinst


    dict_points = {'X': 1, 'Y': 2, 'Z': 3}

    points: int = 0

    with open("input-2.txt", "r") as file:
        line = " "
        while line != '':
            line = file.readline()
            if line == '':
                break
            if '\n' in line:
                line = line.split("\n")[0]
            opponent, you = line.split(" ")
            if (opponent, you) in list_wins:
                points += 6
            elif (opponent, you) in list_draws:
                points += 3
            else:
                points += 0
            points += dict_points[you]

    print(f'answer 1: {points}')

def task_two():
    # opponent
    # A rock
    # B paper
    # C scizzors
    # you
    # X rock
    # Y paper
    # Z scissors


    dict_loses = {'A': 'Z', 'B': 'X', 'C' : 'Y'} # A beats : [Z] so user loses # 0 points
    dict_draws = {'A': 'X', 'B': 'Y', 'C' : 'Z'} # 3 points
    dict_wins = {'A': 'Y', 'B': 'Z', 'C': 'X'} # Y beats A so user wins # 6 poinst


    dict_should = {'X': (0,dict_loses), 'Y': (3,dict_draws), 'Z': (6,dict_wins)}

    # list_loses = [('A', 'Z'), ('B', 'X'), ('C', 'Y')] # A beats : [Z] so user loses # 0 points
    # list_draws = [('A', 'X'), ('B', 'Y'), ('C', 'Z')] # 3 points
    # list_wins = [('A', 'Y'), ('B', 'Z'), ('C', 'X')] # Y beats A so user wins # 6 poinst


    dict_points = {'X': 1, 'Y': 2, 'Z': 3}

    points: int = 0

    with open("input-2.txt", "r") as file:
        line = " "
        while line != '':
            line = file.readline()
            if line == '':
                break
            if '\n' in line:
                line = line.split("\n")[0]
            opponent, outcome = line.split(" ")
            should = dict_should[outcome]
            points += should[0]
            you = should[1][opponent]
            points += dict_points[you]

    print(f'answer 1: {points}')



# sprobowac z zamiana na liczby, wtedy to bedzie dzikie bo +2 wygrywa +1 przegyrwa a 0 to draw

if __name__ == "__main__":
    for i in [task_one, task_two]:
        elapsed = timeit(i, number=1)
        print(f"elapsed seconds {i.__name__}: {elapsed}")