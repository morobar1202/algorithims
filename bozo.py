# Bozo sort experiment
# by Liam Morrison
# V 1.01
import random
import time
# the number of times you wisg to run the program
TIMES = 1000
SIZE = 10
# takes the time the program starts
start_time = time.time()
# set up random number generator
random.seed(1)
new_list = []
x = 0
n = 0
p = 0
# this loop will conclude once the algorithm has been run the set amount of times
while x < TIMES:
    # this for loop is for the randomly generated list
    for i in range(SIZE):
        # this line randomly generates a number and adds to the list
        new_list.append(random.randint(-1000,1000))
    # This loop is the algorithm its self
    ind = range(0, len(new_list))
    while p < len(new_list) - 1:
        # checks if the next number is smaller
        if new_list[p] > new_list[p + 1]:
            # finds two random numbers in the list and swaps them
            z = random.choice(ind)
            y = z
            while y==z:
                y = random.choice(ind)
            a = new_list[z]
            b = new_list[y]
            new_list[y] = a
            new_list[z] = b
            # starts integrating through from the start of the list again
            p = -1
        n += 1
        p += 1
    print(f" sorted list {x + 1}: {new_list}")
    x += 1
    p = 0
    new_list=[]
total = time.time() - start_time
print(f"{(n/TIMES):.0f} interactions on average")
print(f"total time: {total:.2f} (s)")
print(f"average time: {(total/TIMES):.2f} (s)")