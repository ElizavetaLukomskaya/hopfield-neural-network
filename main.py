from utils import *
from math import tanh

filename, image = choose_file()
row, cols = len(image), len(image[0])
image = [[-1 if x == 0 else x for x in row] for row in image]
image = [sum(image, [])]

image = transpose(image)

weight_matrix = multi_matrix(image, transpose(image))
weight_matrix = null_square_matrix_diagonal(weight_matrix)

input_image = read_to_matrix('input', filename)
input_image = [[-1 if x == 0 else x for x in row] for row in input_image]
input_image = [sum(input_image, [])]
input_image = transpose(input_image)


flag = False
iteration = 0

while flag == False:
    hidden_layer = multi_matrix(weight_matrix, input_image)

    right_neural_counter = 0
    for i in range(len(hidden_layer)):
        for j in range(len(hidden_layer[0])):
            hidden_layer[i][j] = tanh(hidden_layer[i][j])

        if hidden_layer[i][0] == input_image[i][0]:
            right_neural_counter += 1



    iteration += 1
    print(f'Iteration #{iteration}\n{len(hidden_layer) - right_neural_counter}')

    if right_neural_counter == len(hidden_layer):
        flag = True
        print(f'\nRelaxation!!!\nFinal iteration: {iteration}')
        hidden_layer = [[0 if round(x) == -1 else x for x in row] for row in hidden_layer]
        hidden_layer = [[1 if round(x) == 1 else x for x in row] for row in hidden_layer]
        hidden_layer = transpose(hidden_layer)
        hidden_layer = sum(hidden_layer,[])
        return_to_output = []
        for i in range(row):
            vector = []
            for j in range(cols):
                vector.append(hidden_layer[i*cols+j])
            return_to_output.append(vector)
        write_to_txt(return_to_output, 'output', filename)

    else:
        input_image = hidden_layer

