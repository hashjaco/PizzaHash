import numpy as np
from time import perf_counter

# data sets ordered by size, ascending
set_a = open('data/a_example.in', 'r', encoding='utf-8')
set_b = open('data/b_small.in', 'r', encoding='utf-8')
set_c = open('data/c_medium.in', 'r', encoding='utf-8')
set_d = open('data/d_quite_big.in', 'r', encoding='utf-8')
set_e = open('data/e_also_big.in', 'r', encoding='utf-8')

def getData(file):
    max_slices, num_types = file.readline().replace("\n", "").split(" ")
    pizza_weights = file.readline().replace("\n", "").split(" ")
    return int(max_slices), int(num_types), pizza_weights


def buildPizzaDictionary(num_of_slice_list: []):
    size = len(num_of_slice_list)
    assert size > 0
    pizza_dict = {}

    try:
        for x in range(size):
            pizza_dict.update({int(num_of_slice_list[x]) : (f'pizza {x + 1}', 10)})

        return pizza_dict
    except IndexError:
        print("index is out of range")



def findCombination(max_slices: int, pizzas: dict):
    pizza_types = []
    pizza_slices = []
    pizza_values = []
    for item in pizzas.values():
        pizza_types.append(item[0])
        pizza_values.append(item[1])
    for item in pizzas.keys():
        pizza_slices.append(item)
    print(f'Pizza types: {repr(pizza_types)}')
    print(f'Pizza slices for each type: {repr(pizza_slices)}')
    print(f'Pizza values for each type: {repr(pizza_values)}')
    num_pizzas = len(pizzas)
    assert num_pizzas > 0 and max_slices > 0
    knapsack_matrix = np.array([[0 for x in range(max_slices + 1)] for x in range(num_pizzas+1)])

    ''' Fix this part. The cells should be assigned either 0 or 1, then we can figure out the max number of slices that we can possibly get. '''
    # print('\n', repr(knapsack_matrix))
    for row in range(num_pizzas-1):
        for column in range(0, max_slices+1):
            slices = pizza_slices[row]
            value = pizza_values[row]
            if column == 0:
                knapsack_matrix[row][column] = 0
            elif slices <= column:
                knapsack_matrix[row][column] = max(knapsack_matrix[row - 1][column] + value, knapsack_matrix[row - 1][column])
            else:
                knapsack_matrix[row][column] = knapsack_matrix[row - 1][column]
    return


''' In case we can't assume that the given list is sorted, here's quicksort '''

def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]   # assign value of high element to pivot

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


def quickSort(arr, low, high):
    if low < high:
        partition_index = partition(arr, low, high)

        quickSort(arr, low, partition_index - 1)
        quickSort(arr, partition_index + 1, high)


max_slices, num_types, pizza_weights = getData(set_a)
pizza_dictionary = buildPizzaDictionary(pizza_weights)
some_array = [4, 2, 6, 123, 53, 2, -2, 444, 23, 12, -354] # testing quicksort algorithm

''' Tests '''

print(f'Max number of slices for event: {max_slices}')
print(f'Number of different types of pizza: {num_types}')
print(f'Amount of slices for each pizza: {pizza_weights}\n')
print(f'Dictionary: {pizza_dictionary}\n')

print(f'Results of findCombination: {findCombination(max_slices, pizza_dictionary)}')

print(f"Quicksort: {some_array}\n")
size = len(some_array)
t1_start = perf_counter()  # Begin performance monitor for sorting
quickSort(some_array, 0, size - 1)
t1_stop = perf_counter()  # Stop performance monitor and calculate below
print(f'Quicksort result: {repr(some_array)} with elapsed time from {t1_stop}-{t1_start} = {t1_stop-t1_start}\n')
