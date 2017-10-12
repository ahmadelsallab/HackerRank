'''
Created on Oct 12, 2017

@author: linux
'''
def swap_in_place(arr):
    '''
    if(len(arr) == 1):
        return arr
    else:
        swap_in_place(arr[1])
    '''
    arr[0] = arr[1] - arr[0]
    arr[1] = arr[1] - arr[0]
    arr[0] = arr[1] + arr[0]

    return arr
if __name__ == '__main__':
    pass

a = [1,2]
print swap_in_place(a)