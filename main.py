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
    return max_slices, num_types, pizza_weights


def buildPizzaDictionary(weight_list: []):
    size = len(weight_list)
    assert size > 0
    pizza_dict = {}

    try:
        for x in range(size):
            pizza_dict.update({f'pizza {x + 1}' : int(weight_list.pop(0))})

        return pizza_dict
    except IndexError:
        print("index is out of range")



def findCombination(max_slices, pizzas: {}):
    num_pizzas = len(pizzas)
    assert num_pizzas > 0 and max_slices > 0
    knapsack_matrix = np.array([[], []])
    for row in range(max_slices):
        for column in range(num_pizzas):

    return knapsack_matrix[:, max_slices]


max_slices, num_types, pizza_weights = getData(set_a)
pizza_dictionary = buildPizzaDictionary(pizza_weights)
print(max_slices)
print(num_types)
print(pizza_weights)
print(pizza_dictionary)
