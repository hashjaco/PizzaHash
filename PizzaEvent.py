import numpy as np

class PizzaEvent:
    def __init__(self, file):
        self.max_slices, self.num_types, self.pizza_weights = getData(file)


    ''' Return a dictionary of pizza weights a'''
    def returnPizzaDict(self):
        pizza_dict = {}
        for i in range(len(self.pizza_weights)):
            pizza_dict.update({i: self.pizza_weights[i]})
        return pizza_dict


    ''' This function traverses the matrix to determine the highest possible value we can achieve with the original options given 
        Time Complexity: Theta(n); Space Complexity: O(1) '''
    def getMaxPossible(self, matrix):
        index_value, curr_row, max_possible = matrix[self.num_types - 1][self.max_slices], self.num_types - 1, self.max_slices

        while index_value != 1:
            if curr_row and max_possible == 0:
                return
            elif max_possible == 0:
                curr_column, curr_row = self.max_slices + 1, curr_row - 1
            max_possible -= 1
            index_value = matrix[curr_row][max_possible]
        return max_possible, curr_row


    ''' This function navigates the matrix to build the solution array, determining the combination that will maximize our value '''
    def getSubsetSolution(self, matrix, curr_column: int, curr_row: int):
        solution = {}
        while curr_column != 0:
            if curr_row != 0 and matrix[curr_row-1][curr_column] == 1:
                curr_row -= 1
                continue
            solution.update({curr_row: self.pizza_weights[curr_row]})
            curr_column -= self.pizza_weights[curr_row]
        return solution


    ''' This function runs the dynamic algorithm that fills the matrix with 1s and 0s conditionally '''
    def fillMatrix(self, matrix):
        for row in range(self.num_types):
            for column in range(0, self.max_slices+1):
                if column == 0:
                    matrix[row][column] = 0
                    continue
                slices = self.pizza_weights[row]
                if column == slices:
                    matrix[row][column] = 1
                elif row == 0 and column != slices:
                    matrix[row][column] = 0
                elif matrix[row-1][column] == 1:
                    matrix[row][column] = 1
                else:
                    matrix[row][column] = matrix[row-1][column-slices]
        return matrix


    ''' This is the bottom-up dynamic programming solution. Though extremely accurate, it's not so scalable. Time complexity: theta(N * w), Space complexity: theta(N * w) '''
    def findCombination(self):
        matrix = self.fillMatrix([[0 for x in range(int(self.max_slices) + 1)] for x in range(int(self.num_types))])
        max_possible, curr_row = self.getMaxPossible(matrix)
        return self.getSubsetSolution(matrix, max_possible, curr_row)


    ''' The Shimmy Search algorithm traverses the list of pizzas in descending order, summing the slices up along the way until it exceeds the maximum amount of slices, then it continues skips every value until it reaches one that puts it under the maximum and repeats the cycle '''
    def shimmySearch(self):
        size = len(self.pizza_weights)
        assert size > 0
        pizza_dict = self.returnPizzaDict()
        solution_dict = {}
        for i in range(size):
            index = size - i - 1
            next_value = pizza_dict[index]
            p_keys, p_values = list(pizza_dict.keys()), list(pizza_dict.values())
            curr_max = sum(list(solution_dict.values()))
            curr_sum = curr_max + next_value

            if curr_sum == self.max_slices:
                solution_dict.update({index: next_value})
                return solution_dict

            elif curr_sum < self.max_slices:
                low_delta = self.max_slices - curr_sum
                solution_dict.update({index: next_value})
                if low_delta not in pizza_dict.values():
                    continue
                solution_dict.update({p_values.index(low_delta): low_delta})
                return solution_dict
            else:
                high_delta = curr_sum - self.max_slices
                if high_delta not in solution_dict.values():
                    continue
                solution_dict.pop(p_keys[p_values.index(high_delta)]) and solution_dict.update({index: next_value})
                # return solution_dict
        return solution_dict


''' This function extracts the appropriate values from the given file '''
def getData(file):
    file = open(f'data/{file}', 'r', encoding='utf-8')
    max_slices, num_types = file.readline().replace("\n", "").split(" ")
    pizza_weights = file.readline().replace("\n", "").split(" ")
    file.close()
    return int(max_slices), int(num_types), list(map(int, pizza_weights))






