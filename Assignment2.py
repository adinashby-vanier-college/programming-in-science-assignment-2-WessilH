# Function 1: Lists - Finding the Maximum and Second Maximum in a List
# This function takes a list of numbers as input and returns the maximum and second maximum values.
def max_two_in_list(numbers):
    if len(numbers) == 0:
        return (None, None)

    if len(numbers) == 1:
        return (numbers[0], None)

    max1 = max(numbers)
    remaining = [n for n in numbers if n != max1]

    if not remaining:
        return (max1, max1)

    max2 = max(remaining)
    return (max1, max2)


# Function 2: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
    return sorted(list(set(numbers)))

# Function 3: Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
    result = [0] * len(arr)
    total = 0
    for i in range(len(arr)):
        total += arr[i]
        result[i] = total
    return result


# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):
    rows = len(matrix)
    collumn = len(matrix[0])

    result = [[0] * rows for i in range(collumn)]

    for r in range(rows):
        for c in range(collumn):
            result[c][r] = matrix[r][c]

    return result

# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):
    return lst[::step]

# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    total = 0
    for i in range(len(list1)):
        total += list1[i] * list2[i]
    return total

# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    result = [[0] * cols2 for i in range(rows1)]

    for r in range(rows1):
        for c in range(cols2):
            total = 0
            for k in range(cols1):
                total += matrix1[r][k] * matrix2[k][c]
            result[r][c] = total

    return result