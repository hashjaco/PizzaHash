import numpy as np

class PizzaEvent:
    def __init__(self, file):
        self.max_slices, self.num_types, self.pizza_weights = getData(file)


    def getPizzaWeights(self):
        return self.pizza_weights


    def getNumOfTypes(self):
        return self.num_types


    def getMaxSlices(self):
        return self.max_slices


    ''' This functions allows the user to import a custom collection of pizzas '''
    def setPizzaWeights(self, pizza_weights: list):
        self.pizza_weights = pizza_weights
        self.num_types = len(self.pizza_weights)


    ''' This function allows the user to set a custom maximum amount '''
    def setMaxSlices(self, max_slices):
        self.max_slices = max_slices


    ''' This function will reset the object parameters given a new, valid file of values '''
    def resetValues(self, file):
        self.max_slices, self.num_types, self.pizza_weights = getData(file)


    ''' Return a dictionary of pizza weights a'''
    def returnPizzaDict(self):
        pizza_dict = {}
        for i in range(len(self.pizza_weights)):
            pizza_dict.update({i: self.pizza_weights[i]})
        print(repr(pizza_dict))
        return pizza_dict

    ''' This function traverses the matrix to determine the highest possible value we can achieve with the original options given 
        Time Complexity: O(n); Space Complexity: O(1) '''
    def getMaxPossible(self, matrix):
        print("Getting the maximum amount of slices possible with the pizza options given.\n")
        index_value, curr_row, max_possible = matrix[self.num_types - 1][self.max_slices], self.num_types - 1, self.max_slices

        while index_value != 1:
            if curr_row and max_possible == 0:
                print(f"Solution does not exist for some reason.")
                return
            elif max_possible == 0:
                curr_column, curr_row = self.max_slices + 1, curr_row - 1
            max_possible -= 1
            index_value = matrix[curr_row][max_possible]

        print(f"Max possible slices: {max_possible}")
        return max_possible, curr_row


    ''' This function navigates the matrix to build the solution array, determining the combination that will maximize our value '''
    def getSubsetSolution(self, matrix, curr_column: int, curr_row: int):
        print("Getting solution...")
        solution = {}
        solution_slices = []
        while curr_column != 0:
            if curr_row != 0 and matrix[curr_row-1][curr_column] == 1:
                curr_row -= 1
            else:
                solution.update({curr_row: self.pizza_weights[curr_row]})
                solution_slices.append(self.pizza_weights[curr_row])
                curr_column -= self.pizza_weights[curr_row]
        print(f"A solution is {repr(solution)} with a total of {sum(solution_slices)} slices!")
        return solution


    ''' This function runs the dynamic algorithm that fills the matrix with 1s and 0s conditionally '''
    def fillMatrix(self, matrix):
        print("Filling matrix...this may take a while for large sets")

        for row in range(self.num_types):
            for column in range(0, self.max_slices+1):
                slices = self.pizza_weights[row]
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


    ''' This is the main function that runs everything and returns the solution '''
    def findCombination(self):
        print("Finding combination of pizzas that will maximize the number of slices we can get for the event without going over the max allowed...This may take some time for outrageously large sets...\n")
        print("Initializing matrix...")

        matrix = np.array([[0 for x in range(int(self.max_slices) + 1)] for x in range(int(self.num_types))])
        matrix = self.fillMatrix(matrix)
        max_possible, curr_row = self.getMaxPossible(matrix)

        return self.getSubsetSolution(matrix, max_possible, curr_row)

    # try multiple pointers, no recursion, no matrix
    # for very large sets that have around a million or so integers and a max number that's also really high, we run out of memory in the heap which crashes the program.
    # our current solution is running at O(n*W) with a space complexity of O(n*W) for the matrix
    # this requires a lot more RAM to store and compute solution.
    def hashimsAlgorithm(self):
        # create pizza dictionary for the list of different pizza weights: store weights as keys; values are the index
        pizza_dict = self.returnPizzaDict()
        # create empty dictionary for the solutions
        solution_dict = {}
        low, high = 0, len(pizza_dict)
        on_low = False

        while low != high:
            curr_sum = sum(solution_dict)
            if curr_sum == self.max_slices:
                return solution_dict
            elif curr_sum < self.max_slices:
                low_delta = self.max_slices - curr_sum
                if low_delta in pizza_dict.keys():
                    solution_dict.update({low_delta: pizza_dict.get(low_delta)})
                    return solution_dict
                else:
                    if not on_low:
                        solution_dict.update({})
            else:
                high_delta = curr_sum - self.max_slices
                if high_delta in solution_dict.keys():
                    solution_dict.pop(high_delta)
                    return solution_dict



        # return values of solution dictionary
        return solution_dict

    # Solution below runs at O(n) time using O(n) space
    # Needs some tweaking to return the most optimal solution
    def shimmySearch(self):
        size = len(self.pizza_weights)
        assert size > 0
        pizza_dict = self.returnPizzaDict()
        solution_dict = {}
        for i in range(size):
            index = size - i - 1
            next_value = pizza_dict[index]
            curr_max = sum(solution_dict.keys())
            curr_sum = curr_max + next_value

            if curr_sum == self.max_slices:
                solution_dict.update({next_value: index})
                return solution_dict

            elif curr_max + next_value < self.max_slices:
                low_delta = self.max_slices - curr_max
                if low_delta not in pizza_dict.values():
                    solution_dict.update({next_value: index})
                    continue
                keys, values = list(pizza_dict.keys()), list(pizza_dict.values())
                solution_dict.update({keys[values.index(low_delta)]: index})
            else:
                high_delta = curr_max + next_value - self.max_slices
                if high_delta not in solution_dict.keys():
                    continue
                solution_dict.pop(high_delta) and solution_dict.update({next_value: index})
        return solution_dict

    def shimmySearch2(self):
        size = len(self.pizza_weights)
        assert size > 0
        pizza_dict = self.returnPizzaDict()
        solution_dict = {}
        for i in range(size):
            index = size - i - 1
            next_value = pizza_dict[index]
            p_keys, p_values = list(pizza_dict.keys()), list(pizza_dict.values())
            curr_max = sum(solution_dict.values())
            curr_sum = curr_max + next_value

            if curr_sum == self.max_slices:
                solution_dict.update({index: next_value})
                return solution_dict

            elif curr_sum < self.max_slices:
                low_delta = self.max_slices - curr_max
                if low_delta not in pizza_dict.values():
                    solution_dict.update({index: next_value})
                    continue
                solution_dict.update({p_values.index(low_delta): low_delta})
                return solution_dict
            else:
                high_delta = curr_sum - self.max_slices
                if high_delta not in solution_dict.values():
                    continue
                solution_dict.pop(p_keys[p_values.index(high_delta)]) and solution_dict.update({index: next_value})
                return solution_dict
        return solution_dict


    def get_fastest(self, solution1: float, solution2: float):
        if solution1 < solution2:
            print(f'\nDynamic Programming solution is the fastest with {solution1} seconds by {solution2 - solution1} seconds')
        else:
            print(f'\nShim Search solution is the fastest with {solution2} seconds by {solution1 - solution2} seconds')


    def get_most_accurate(self, solution1: list, solution2: list):
        if sum(solution1) > sum(solution2):
            print(f'Most accurate solution is Dynamic Programming solution with a total of {sum(solution1)} slices')
            return
        print(f'Most accurate solution is Shimmy Search solution with a total of {sum(solution2)} slices')


    def compare_choices(self, solution1: list, solution2: list):
        print(repr(solution1))
        print(repr(solution2))


''' This function extracts the appropriate values from the given file '''
def getData(file):
    file = open(f'data/{file}', 'r', encoding='utf-8')
    max_slices, num_types = file.readline().replace("\n", "").split(" ")
    pizza_weights = file.readline().replace("\n", "").split(" ")
    file.close()
    return int(max_slices), int(num_types), list(map(int, pizza_weights))


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



