arr=[2,5,8,7,13,17]
targ=7

def linearSearch(arr,num):
    for i in range(arr.__len__()):
        if arr[i]==num:
            return i
    return -1

print(linearSearch(arr,targ))
