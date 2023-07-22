import os
import copy

def choose_file():
    print('Enter filename: ')
    for filename in os.listdir("images"):
        if filename != '.ipynb_checkpoints':
            print(f'- ', filename)

    filename = input()

    new_lst = read_to_matrix('images', filename)

    return filename, new_lst

def read_to_matrix(folder, filename):
    with open(f'{folder}/{filename}', 'r') as file:
        lst = file.readlines()
    new_lst = [[int(n) for n in x[:-1]] for x in lst[:-1]]
    new_lst.append([])
    for i in lst[-1]:
        new_lst[-1].append(int(i))

    return new_lst

def transpose(matrix):
    matrix = copy.deepcopy(matrix)
    trans_matrix = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
    return trans_matrix

def multi_matrix(a, b):
    a = copy.deepcopy(a)
    b = copy.deepcopy(b)
    zip_b = zip(*b)
    zip_b = list(zip_b)  # массив столбцов второй матрицы

    return [[sum(ele_a * ele_b for ele_a, ele_b in zip(row_a, col_b)) for col_b in zip_b] for row_a in a]

def null_square_matrix_diagonal(matrix):
    for i in range(len(matrix)):
        matrix[i][i] = 0

    return matrix

def write_to_txt(matrix, folder, filename):
    with open(f'{folder}/{filename}', 'w') as f:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                f.write(f"{matrix[i][j]}")
            f.write('\n')

def int_r(num):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num