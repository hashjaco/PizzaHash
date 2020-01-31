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
            pizza_dict.update({int(num_of_slice_list[x]) : f"pizza {x + 1}"})

        return pizza_dict
    except IndexError:
        print("index is out of range")



def findCombination(max_slices: int, pizzas: dict):
    print("Finding combination of pizzas that will maximize the number of slices we can get for the event without going over the max allowed...This may take some time for outrageously large sets...")
    pizza_slices = []

    for item in pizzas.keys():
        pizza_slices.append(item)
    print(f'Pizza slices for each type: {repr(pizza_slices)}')
    num_pizzas = len(pizzas)
    assert num_pizzas > 0 and max_slices > 0
    print("Initializing matrix...")
    matrix = np.array([[0 for x in range(max_slices + 1)] for x in range(num_pizzas)])

    matrix = fillMatrix(matrix, num_pizzas, pizza_slices)

    max_possible, curr_row = getMaxPossible(matrix, num_pizzas, max_slices)

    return getSubsetSolution(matrix, max_possible, curr_row, pizza_slices)


def fillMatrix(matrix, num_pizzas: int, pizza_slices: []):
    print("Filling matrix...this may take a while for large sets")

    for row in range(num_pizzas):
        for column in range(0, max_slices+1):
            slices = pizza_slices[row]
            if column != 0:
                if column == slices:
                    matrix[row][column] = 1
                elif row == 0 and column != slices:
                    matrix[row][column] = 0
                elif matrix[row-1][column] == 1:
                    matrix[row][column] = 1
                else:
                    matrix[row][column] = matrix[row-1][column-slices]
            else:
                matrix[row][column] = 0
    return matrix


def getMaxPossible(matrix, num_pizzas, max_slices):
    print("Getting the maximum amount of slices we can get. This may take a while for very large sets...")
    index_value, curr_row, max_possible = matrix[num_pizzas - 1][max_slices], num_pizzas - 1, max_slices

    while index_value != 1:
        if curr_row and max_possible == 0:
            print(f"Solution does not exist for some reason.")
            return
        elif max_possible == 0:
            curr_column, curr_row = max_slices + 1, curr_row - 1
        max_possible -= 1
        index_value = matrix[curr_row][max_possible]

    print(f"Max possible slices: {max_possible}")
    return max_possible, curr_row



def getSubsetSolution(matrix, curr_column: int, curr_row: int, pizza_slices: []):
    print("Getting solution...")
    solution = []
    solution_slices = []
    while curr_column != 0:
        if curr_row != 0 and matrix[curr_row-1][curr_column] == 1:
            curr_row -= 1
        else:
            solution.append(f"pizza {curr_row + 1}")
            solution_slices.append(pizza_slices[curr_row])
            curr_column -= pizza_slices[curr_row]
    print(f"A solution is {repr(solution)} with a total of {sum(solution_slices)} slices!")
    return solution


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


max_slices, num_types, pizza_weights = getData(set_c)
pizza_dictionary = buildPizzaDictionary(pizza_weights)
some_array = [4, 2, 6, 123, 53, 2, -2, 444, 23, 12, -354]  # testing quicksort algorithm

''' Tests '''

print(f'Max number of slices for event: {max_slices}')
print(f'Number of different types of pizza: {num_types}')
print(f'Amount of slices for each pizza: {pizza_weights}\n')
solution = findCombination(max_slices, pizza_dictionary)

print(f"Quicksort: {some_array}\n")
size = len(some_array)
t1_start = perf_counter()  # Begin performance monitor for sorting
quickSort(some_array, 0, size - 1)
t1_stop = perf_counter()  # Stop performance monitor and calculate below
print(f'Quicksort result: {repr(some_array)} with elapsed time from {t1_stop}-{t1_start} = {t1_stop-t1_start}\n')
