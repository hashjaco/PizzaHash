import numpy as np

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
            pizza_dict.update({f'pizza {x + 1}' : int(num_of_slice_list.pop(0))})

        return pizza_dict
    except IndexError:
        print("index is out of range")



def findCombination(max_slices: int, pizzas: dict):
    maximum = int(max_slices)
    pizza_dict = pizzas
    num_pizzas = len(pizza_dict)
    assert num_pizzas > 0 and maximum > 0
    knapsack_matrix = np.array([[0 for x in range(maximum+1)] for x in range(num_pizzas)])

    print('\n', repr(knapsack_matrix))
    for column in range(maximum+1):
        print(column)
        for row in range(0, num_pizzas):
            if row == 0 or column == 0:
                knapsack_matrix[column][row] = 0
            elif pizza_dict.get() <= column:

            else:
                knapsack_matrix[column][row] = knapsack_matrix[column][row-1]
    return knapsack_matrix[:, max_slices]


max_slices, num_types, pizza_weights = getData(set_a)
pizza_dictionary = buildPizzaDictionary(pizza_weights)
print(max_slices)
print(num_types)
print(pizza_weights)
print(pizza_dictionary)

combo = findCombination(max_slices, pizza_dictionary)
print(repr(combo))
