# Amir Hosein Safari on Oct 15, 2021

import numpy as np


def message_encoder(message):
    encoded_message = ""

    # finding number of rows and columns
    lower_bound = int(np.sqrt(len(message)))
    if lower_bound == np.sqrt(len(message)):
        column_num = lower_bound
        row_num = lower_bound
    else:
        column_num = lower_bound + 1
        row_num = len(message)//column_num + 1

    # iterate over the string in order to make the encoded message
    for j in range(0, column_num):
        for i in range(0, row_num):
            if column_num * i + j < len(message):
                encoded_message += message[column_num * i + j]
        encoded_message += " "

    return encoded_message


if __name__ == '__main__':
    input_message = input()
    print(message_encoder(input_message))
