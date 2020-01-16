
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


max_slices, num_types, pizza_weights = getData(set_a)
print(max_slices)
print(num_types)
print(pizza_weights)
