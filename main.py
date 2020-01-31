import numpy as np
import dask.array as da
from PizzaEvent import PizzaEvent
from time import perf_counter

# data sets ordered by size, ascending
set_a = open('data/a_example.in', 'r', encoding='utf-8')
set_b = open('data/b_small.in', 'r', encoding='utf-8')
set_c = open('data/c_medium.in', 'r', encoding='utf-8')
set_d = open('data/d_quite_big.in', 'r', encoding='utf-8')
set_e = open('data/e_also_big.in', 'r', encoding='utf-8')


if __name__ == "__main__":
    pizzaEvent = PizzaEvent(set_c)

    start = perf_counter()
    solution = pizzaEvent.findCombination()
    stop = perf_counter()

    print(solution)
    print(f"\nSolution found in {stop - start} seconds.")
