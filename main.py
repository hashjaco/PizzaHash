import numpy as np
import dask.array as da
from PizzaEvent import PizzaEvent
from time import perf_counter

# data sets ordered by size, ascending


if __name__ == "__main__":
    set_a = 'a_example.in'
    set_b = 'b_small.in'
    set_c = 'c_medium.in'
    set_d = 'd_quite_big.in'
    set_e = 'e_also_big.in'

    try:
        pizzaEvent = PizzaEvent(set_c)

        alg1_start = perf_counter()
        solution1 = pizzaEvent.findCombination()
        alg1_stop = perf_counter()

        pizzaEvent2 = PizzaEvent(set_d)

        alg2_start = perf_counter()
        solution2 = pizzaEvent2.shimmySearch2()
        alg2_stop = perf_counter()

        print(f'\n{solution1}')
        solution1_performance = alg1_stop - alg1_start
        print(f"Solution found by Dynamic Programming in {solution1_performance} seconds.\n")
        print(f'Number of slices: {sum(solution1.values())}')

        print(f'\n{solution2}')
        solution2_performance = alg2_stop - alg2_start
        print(f"Solution found by Shim Search in {solution2_performance} seconds.")
        print(f'Number of slices: {sum(solution2.values())}')

        pizzaEvent.get_fastest(solution1_performance, solution2_performance)
        pizzaEvent.get_most_accurate(solution1.values(), solution2.values())

        print('\n')
        pizzaEvent.compare_choices(solution1.values(), solution2.values())
    except KeyError:
        print(KeyError)
