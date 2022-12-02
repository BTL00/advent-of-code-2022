import numpy
import re
from timeit import timeit

def do_stuff():

    with open("adv-of-code-1-2022-input.txt", "r") as file:
        full_list = numpy.array([])
        sum_of_calories: int = 0
        line = " "
        while line:
            line = file.readline()
            if re.match(line, "\n"):
                full_list = numpy.append(full_list, sum_of_calories)
                sum_of_calories = 0
                continue
            else:
                sum_of_calories += int(line)



    top = numpy.ndarray(3, dtype=int)
    for i in range(0,3):
        arg = full_list.argmax()
        top[i] =  full_list[arg]
        full_list[arg] = 0

    print(f'answer 1: {top[0]}')
    print(f'answer 2: {numpy.sum([top])}')

def other():
    with open("adv-of-code-1-2022-input.txt", "r") as file:
        x = 0
        y = 0
        y_max = 0
        line = file.readline()
        while line:
            if re.match(line, "\n"):
                 x += 1
                 y = 0
            else:
                y += 1
                if y > y_max: y_max = y
            line = file.readline()
        file.seek(0)
        
        full_list = numpy.zeros((x + 1,y_max), dtype=int)
        line = " "
        x_counter = 0
        y_counter = 0
        while line:
            line = file.readline()
            if re.match(line, "\n"):
                x_counter += 1
                y_counter = 0
                continue
            else:
                full_list[x_counter, y_counter] = int(line)
                y_counter += 1

    sums = numpy.ndarray(x)
    for i in range(0, x):
        sums[i] = numpy.sum(full_list[i, :])
    top = numpy.max(sums)
    print(f'answer 1: {top}')

    second = numpy.max(sums, initial=0, where=sums<top)
    third = numpy.max(sums, initial=0, where=sums<second)
    print(f'answer 2: {top + second + third}')



def last():

    with open("adv-of-code-1-2022-input.txt", "r") as file:
        full_list = numpy.array([])
        sum_of_calories: int = 0
        line = " "
        while line:
            line = file.readline()
            if re.match(line, "\n"):
                full_list = numpy.append(full_list, sum_of_calories)
                sum_of_calories = 0
                continue
            else:
                sum_of_calories += int(line)

    
    top = numpy.max(full_list)
    print(f'answer 1: {top}')

    second = numpy.max(full_list, initial=0, where=full_list<top)
    third = numpy.max(full_list, initial=0, where=full_list<second)
    print(f'answer 2: {top + second + third}')



if __name__ == "__main__":
    for i in [do_stuff, other, last]:
        elapsed = timeit(i)
        print(f"elapsed seconds {i.__name__}: {elapsed}")