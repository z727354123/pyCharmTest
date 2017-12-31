arr = [1, 2, 3, 4, 5, 6]
print(arr[-0: 999])
print(arr[:])
print(arr)

arr2 = arr[:]
arr.append(1)
arr2.append(1)
print(arr)
print(arr2 == arr)


