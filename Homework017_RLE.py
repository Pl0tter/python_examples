# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

def RLE_decoder(string_input):
    string_output = ''
    if string_input[0].isdigit():
        number = ''
        for i in range(len(string_input)):
            if string_input[i].isdigit():
                number += string_input[i]
            else:
                string_output += string_input[i] * int(number)
                number = ''
    else:
        index_start_letter = 0
        for i in range(1, len(string_input)):
            if string_input[i] != string_input[i-1]:
                string_output += str(i-index_start_letter) + string_input[i-1]
                index_start_letter = i
            elif i == len(string_input) - 1:
                string_output += str(i-index_start_letter+1) + string_input[i]
    return string_output


input_file_path = 'Python/Examples/Homework017_RLE_input.txt'
output_file_path = 'Python/Examples/Homework017_RLE_output.txt'

data = open(input_file_path, 'r')
string_input = data.read()
data.close()

data = open(output_file_path, 'w')
data.write(RLE_decoder(string_input))
data.close()
