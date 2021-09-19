# merge sort experiment
# by Liam Morrison
# V 1.00
import random, time
TIMES = 1000
SIZE = 10


def mergesort(sort_list):
    """ does the merge sort """
    if len(sort_list) == 1:
        return sort_list
    else:
        middle = len(sort_list) // 2
        left = mergesort(sort_list[0:middle])
        right = mergesort(sort_list[middle:])
        sorted_list = []
        while len(left) != 0 and len(right) != 0:
            if left[0] == right[0]:
                sorted_list.append(left.pop(0))
                sorted_list.append(right.pop(0))
            elif left[0] < right[0]:
                sorted_list.append(left.pop(0))
            else:
                sorted_list.append(right.pop(0))
        if len(left) == 0:
            return sorted_list + right
        return sorted_list + left


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
        sorted_list = mergesort(sort_list)
        print(f" sorted list {repeats + 1}: {sorted_list}")
        repeats += 1
    total = time.time() - start_time
    print(f"total time: {total:.2f} (s)")
    print(f"average time: {(total/TIMES):.10f} (s)")
main()
        
    
    