# quick sort experiment
# by Liam Morrison
# V 1.00
import random, time
TIMES = 1000
SIZE = 10


def quicksort(sort_list):
    """ does the quick sort """
    if len(sort_list) <= 1:
        return sort_list
    else:
        x = len(sort_list) // 2 
        middle_item = sort_list[x]
        left = []
        middle = []
        right =[]
        for i in sort_list:
            if i == middle_item:
                middle.append(i)
            elif i < middle_item:
                left.append(i)
            else:
                right.append(i)
        left = quicksort(left)
        right = quicksort(right)
        return left + middle + right 

def list_create():
    """creates a random list of size SIZE"""
    new_list = []
    for i in range(SIZE):
        new_list.append(random.randint(-1000,1000))
    return new_list
    

def main():
    """controls number of sorts and list generations"""
    repeats = 0
    start_time = time.time()
    while repeats < TIMES:
        sort_list = list_create()
        sorted_list = quicksort(sort_list)
        print(f" sorted list {repeats + 1}: {sorted_list}")
        repeats += 1
    total = time.time() - start_time
    print(f"total time: {total:.2f} (s)")
    print(f"average time: {(total/TIMES):.10f} (s)")
main()