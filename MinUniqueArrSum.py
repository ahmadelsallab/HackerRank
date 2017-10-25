def getMinimumUniqueSum(arr):
    last_unique_val = {}

    for i in range(len(arr)):

        if arr[i] in last_unique_val:
            last_unique_val[arr[i]] += 1
        else:
            last_unique_val[arr[i]] = arr[i]

        arr[i] = last_unique_val[arr[i]]
    print arr
    return sum(arr)

arr = [1,2,2,2,3]
print getMinimumUniqueSum(arr)