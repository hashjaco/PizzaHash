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


    def setPizzaWeights(self, pizza_weights: list):
        self.pizza_weights = pizza_weights


    def setNumOfTypes(self, num_types):
        self.num_types = num_types


    def setMaxSlices(self, max_slices):
        self.max_slices = max_slices


    def resetValues(self, file):
        self.max_slices, self.num_types, self.pizza_weights = getData(file)


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


    def getSubsetSolution(self, matrix, curr_column: int, curr_row: int):
        print("Getting solution...")
        solution = []
        solution_slices = []
        while curr_column != 0:
            if curr_row != 0 and matrix[curr_row-1][curr_column] == 1:
                curr_row -= 1
            else:
                solution.append(f"pizza {curr_row}: {self.pizza_weights[curr_row]}")
                solution_slices.append(self.pizza_weights[curr_row])
                curr_column -= self.pizza_weights[curr_row]
        print(f"A solution is {repr(solution)} with a total of {sum(solution_slices)} slices!")
        return solution


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


    def findCombination(self):
        print("Finding combination of pizzas that will maximize the number of slices we can get for the event without going over the max allowed...This may take some time for outrageously large sets...\n")

        print("Initializing matrix...")

        matrix = np.array([[0 for x in range(int(self.max_slices) + 1)] for x in range(int(self.num_types))])
        matrix = self.fillMatrix(matrix)

        max_possible, curr_row = self.getMaxPossible(matrix)

        return self.getSubsetSolution(matrix, max_possible, curr_row)


def getData(file):
    max_slices, num_types = file.readline().replace("\n", "").split(" ")
    pizza_weights = file.readline().replace("\n", "").split(" ")
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
