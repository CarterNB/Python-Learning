array = [6, 4, 7, 9, 3,8,10,1]
targ = 13

def ThreeSum(array, targ):
    counter = 0
    final = []
    for i in range(len(array)):
        for j in range(len(array)):
            for k in range(len(array)):
                if i != j and i != k and j != k:
                    if array[i] + array[j] + array[k] == targ:
                        valid = [i, j, k]
                        final.append(valid)
    for index in range(len(final)):
        row = final[index]
        row.sort()
        final[index] = row
    new_final = []
    for elem in final:
        if elem not in new_final:
            new_final.append(elem)
    final = new_final
    print(final)


ThreeSum(array, targ)
