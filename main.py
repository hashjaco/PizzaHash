from PizzaEvent import PizzaEvent
from time import perf_counter

# data sets are in ascending order


if __name__ == "__main__":
    set_a = 'a_example.in'
    set_b = 'b_small.in'
    set_c = 'c_medium.in'
    set_d = 'd_quite_big.in'
    set_e = 'e_also_big.in'

    try:
        event_a = PizzaEvent(set_a)
        event_b = PizzaEvent(set_b)
        event_c = PizzaEvent(set_c)
        event_d = PizzaEvent(set_d)
        event_e = PizzaEvent(set_e)

        # Set a
        alg1_start = perf_counter()
        solution_a = event_a.shimmySearch()
        alg1_stop = perf_counter()
        solutionA_performance = alg1_stop - alg1_start

        # Set b
        alg2_start = perf_counter()
        solution_b = event_b.findCombination()
        alg2_stop = perf_counter()
        solutionB_performance = alg2_stop - alg2_start

        # Set c
        alg3_start = perf_counter()
        solution_c = event_c.findCombination()
        alg3_stop = perf_counter()
        solutionC_performance = alg3_stop - alg3_start

        # Set d
        alg4_start = perf_counter()
        solution_d = event_d.shimmySearch()
        alg4_stop = perf_counter()
        solutionD_performance = alg4_stop - alg4_start

        # Set e
        alg5_start = perf_counter()
        solution_e = event_e.shimmySearch()
        alg5_stop = perf_counter()
        solutionE_performance = alg5_stop - alg5_start

        print(f"Solution found in {solutionA_performance} seconds.\n")
        num_pizzasA = len(solution_a)
        pizzasA = " ".join(map(str, sorted(list(solution_a.keys()))))
        print(sum(solution_a.values()))

        print(f"Solution found in {solutionB_performance} seconds.\n")
        num_pizzasB = len(solution_b)
        pizzasB = " ".join(map(str, sorted(list(solution_b.keys()))))
        print(sum(solution_b.values()))

        print(f"Solution found in {solutionC_performance} seconds.\n")
        num_pizzasC = len(solution_c)
        pizzasC = " ".join(map(str, sorted(list(solution_c.keys()))))
        print(sum(solution_c.values()))

        print(f"Solution found in {solutionD_performance} seconds.\n")
        num_pizzasD = len(solution_d)
        pizzasD = " ".join(map(str, sorted(list(solution_d.keys()))))
        print(sum(solution_d.values()))

        print(f"Solution found in {solutionE_performance} seconds.\n")
        num_pizzasE = len(solution_e)
        pizzasE = " ".join(map(str, sorted(list(solution_e.keys()))))
        print(sum(solution_e.values()))

        file = open(f'data/a_output.in', 'w', encoding='utf-8')
        file.write(str(num_pizzasA) + '\n')
        file.write(pizzasA)
        file.close()

        file = open(f'data/b_output.in', 'w', encoding='utf-8')
        file.write(str(num_pizzasB) + '\n')
        file.write(pizzasB)
        file.close()

        file = open(f'data/c_output.in', 'w', encoding='utf-8')
        file.write(str(num_pizzasC) + '\n')
        file.write(pizzasC)
        file.close()

        file = open(f'data/d_output.in', 'w', encoding='utf-8')
        file.write(str(num_pizzasD) + '\n')
        file.write(pizzasD)
        file.close()

        file = open(f'data/e_output.in', 'w', encoding='utf-8')
        file.write(str(num_pizzasE) + '\n')
        file.write(pizzasE)
        file.close()
    except KeyError:
        print(KeyError)
