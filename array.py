import array as arr
array_num = arr.array ('j', [1, 3, 5, 3, 7])
print("Original array : "+str(array_num))
print("number of occurrences of the number said array: "+str(array_num.count(3)))
array_num.reverse()
print("Reverse the order of the items:")
print(str(array_num))