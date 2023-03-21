array = [1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]


def mostConsecutiveZeros(array):
    mostzero = 0
    for i in range(array.__len__()):
        counter = 0
        if array[i] == 0:
            counter += 1
            flag = 0
            index = 1
            while flag != 1 and i + index < len(array):
                if array[i + index] == 0:
                    counter += 1
                    index += 1
                elif array[i + index] == 1:
                    flag = 1
        if counter >= mostzero:
            mostzero = counter
        else:
            counter = 0
    return mostzero


print(mostConsecutiveZeros(array))
