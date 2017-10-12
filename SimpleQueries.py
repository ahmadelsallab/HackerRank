'''
Created on Oct 12, 2017

@author: linux
'''
#!/bin/python

import sys
import os
# Complete the function below.




'''
# Complete the function below.

def counts(nums, maxes):
    nums.sort()
    maxes.sort()
    n = len(nums)
    m = len(maxes)
    
    counts_res = [0]
    
    i = 0
    j = 0
    while(j < m):
        if(i < n):
            if(maxes[j] >= nums[i]):
                counts_res[j] += 1
                i += 1
            else:
                j += 1
                if(len(counts_res) < m):
                    counts_res.append(counts_res[-1])     
        else:
            j += 1
            if(len(counts_res) < m):
                counts_res.append(counts_res[-1])     
            
    return counts_res
        

'''  

def merge_sort(arr):
    n = len(arr)    
    if n == 1:
        return arr

    else:
        n_by_2 = n/2 + n%2
        left_sorted = merge_sort(arr[0:n_by_2])
        right_sorted = merge_sort(arr[n_by_2:])

        # merge
        sorted_arr = []
        i = 0
        j = 0
        for k in range(n):
            if i < len(left_sorted) and j < len(right_sorted):
                if(left_sorted[i] <= right_sorted[j]):
                    sorted_arr.append(left_sorted[i])
                    i += 1
                else:
                    sorted_arr.append(right_sorted[j])                
                    j += 1
            elif i >= len(left_sorted):
                sorted_arr.append(right_sorted[j])                
                j += 1                
            else:
                sorted_arr.append(left_sorted[i])
                i += 1                
                
            
        return sorted_arr
    
def merge_sort_map(arr, init_map):
    n = len(arr)    
    if n == 1:
        return arr, init_map

    else:
        n_by_2 = n/2 + n%2
        left_sorted, left_map = merge_sort_map(arr[0:n_by_2], init_map[0:n_by_2])
        right_sorted, right_map = merge_sort_map(arr[n_by_2:], init_map[n_by_2:])

        # merge
        sorted_arr = []
        sorted_map = []
        i = 0
        j = 0
        for k in range(n):
            if i < len(left_sorted) and j < len(right_sorted):
                if(left_sorted[i] <= right_sorted[j]):
                    sorted_arr.append(left_sorted[i])
                    sorted_map.append(left_map[i])
                    i += 1
                else:
                    sorted_arr.append(right_sorted[j]) 
                    sorted_map.append(right_map[j])               
                    j += 1
            elif i >= len(left_sorted):
                sorted_arr.append(right_sorted[j])       
                sorted_map.append(right_map[j])          
                j += 1                
            else:
                sorted_arr.append(left_sorted[i])
                sorted_map.append(left_map[i])
                i += 1                
                
            
        return sorted_arr, sorted_map

def counts(nums, maxes):
    # O(nlogn)
    nums, _ = merge_sort_map(nums, range(len(nums)))
    maxes, maxes_map = merge_sort_map(maxes, range(len(maxes)))

    n = len(nums)
    m = len(maxes)
    
    counts_res = [0]
    
    i = 0
    j = 0
    #O(n + m)
    while(j < m):
        if(i < n):
            if(maxes[j] >= nums[i]):
                counts_res[j] += 1
                i += 1
            else:
                j += 1
                if(len(counts_res) < m):
                    counts_res.append(counts_res[-1])     
        else:
            j += 1
            if(len(counts_res) < m):
                counts_res.append(counts_res[-1])     
    
    # Back to original indices
    # O(n)
    counts_orig = counts_res[:]
    
    
    
    for i in range(len(counts_res)):
        counts_orig[maxes_map[i]] = counts_res[i]
    
                
    return counts_orig

        
'''
def heap_sort(arr):
    
    sorted_arr = []
    # O(n)
    h_arr = heapify(arr)    
    for i in range(len(arr)):
        sorted_arr.append(h_arr.get_min())
    return sorted_arr
'''        
              
'''
# Brute force
def counts(nums, maxes):
    
    counts_res = []
    for i in range(len(maxes)):
        counts_res.append(0)
        for j in range(len(nums)):
            if maxes[i] >= nums[j]:
                counts_res[i] += 1
                 
    return counts_res
        
        

'''
'''
if __name__ == "__main__":
    f = open(os.environ['OUTPUT_PATH'], 'w')
    nums_cnt = 0
    nums_cnt = int(raw_input())
    nums_i = 0
    nums = []
    while nums_i < nums_cnt:
        nums_item = int(raw_input());
        nums.append(nums_item)
        nums_i += 1


    maxes_cnt = 0
    maxes_cnt = int(raw_input())
    maxes_i = 0
    maxes = []
    while maxes_i < maxes_cnt:
        maxes_item = int(raw_input());
        maxes.append(maxes_item)
        maxes_i += 1


    res = counts(nums, maxes);
    for res_cur in res:
        f.write( str(res_cur) + "\n" )

    f.close()
'''

#a = [3,7,8,1]
#a = [3,1,8,7,6]
#a = [0, -1, 0]
#print a
#print merge_sort(a)
#print merge_sort_map(a, range(len(a)))

nums = [2, 10, 5, 4, 8]
maxes = [3, 1, 7, 8]
print counts(nums, maxes)
