numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

negative=[i for i in numbers if i<0]
print(negative)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

single_list=[number for row in list_of_lists for number in row]
flattened_list=[number for row in single_list for number in row]
print(flattened_list)

square_array=[(i,i**0,i**1,i**2,i**3,i**4,i**5)for i in range(11)]
print(square_array)
