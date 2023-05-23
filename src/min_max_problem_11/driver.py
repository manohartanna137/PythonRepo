from src.min_max_problem_11.utils import *
row, column = map(int, input("Enter the number of rows and columns: ").split())
result = find_max_min(row, column)
print("Result:", result)