array = [[1,2,3],[4,5],[6,7]]

def flattenArray(array):
    flat=[]
    for i in range(array.__len__()):
        flat=flat+array[i]
    return flat

print(flattenArray(array))
