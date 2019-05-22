import random
import timeit
import sys
sys.setrecursionlimit(100000)

MAX_RANGE = 10000
RANDOM = False
RANDOM_PIVOT = False

def partition(arr, start, end):
    pivot = arr[end]
    ix = start
    #print(arr)
    for i in range(start, end):
        if arr[i] <= pivot:
            arr[i], arr[ix] = arr[ix], arr[i]
            ix += 1
    arr[ix], arr[end] = arr[end], arr[ix]
    return ix

def quick_sort(arr, start, end):
    if start > end: 
        return
    if RANDOM_PIVOT:
        rand_num = random.randint(start, end)
        arr[rand_num], arr[end] = arr[end], arr[rand_num]
        ix = partition(arr, start, end)
    else:
        ix = partition(arr, start, end)
    
    quick_sort(arr, start, ix-1)
    quick_sort(arr, ix+1, end)


try:
    numOfInt = input("Input number of integers: ")
    numOfInt = int(numOfInt)
    reply = input("Would you like to generate random numbers? (Y/N): ")
    
    # IF reply is anything but yes or y then RANDOM is kept false
    if reply.lower() in ("yes", "y"):
        RANDOM = True
    else:
        print("Randomizer not set.")
        # As mentioned in the directions, we are to set a number for the sorted array to increment the array 
        incremental = input("Set a number to multiply and increment the sorted array elements by: ")
    
    reply = input("Would you like to use randomized quicksort? (Y/N): ")

    # IF reply is anything but yes or y then RANDOM_PIVOT is kept false
    if reply.lower() in ("yes", "y"):
        print("Using randomized quicksort.")
        RANDOM_PIVOT = True
    else:
        print("Using regular quicksort.")
    
    arr = []
    print("Generating a list of", numOfInt, "numbers")
    if RANDOM:
        for x in range(numOfInt):
            element = random.randrange(MAX_RANGE)
            arr.append(element)
    else:
        for x in range(numOfInt):
            # element = X + NX or numofInt + incremental(numofInt)
            element = (x + 1) + (x + 1) * (int(incremental))
            arr.append(element)
    
    #print("BEFORE SORT:", arr,'\n\n')
    start_time = timeit.default_timer()
    
    quick_sort(arr, 0, len(arr) - 1)
    
    elapsed = timeit.default_timer() - start_time

    #print("\n\nAFTER SORT:", arr)
    print("RUNNING TIME:", elapsed)
except ValueError as err:
    print("Value error: {0}".format(err))
    print("**INPUT WAS PROBABLY NOT AN INTEGER**")