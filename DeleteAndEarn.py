import sys
import os
def reduceArray(arr, element):
    new_arr = []
    for a in arr:
        if not (a == element or a == element - 1 or a == element + 1):
            new_arr.append(a)
    return new_arr
def calcGain(arr, element):
    gain = 0
    for a in arr:
        if a == element:
            gain += element
    return gain

def maxPoints(elements):

    total_gain = 0
    while len(elements) != 0:
        potential_gain = []
        for element in elements:
            potential_gain.append(calcGain(elements, element))

        max_gain = max(potential_gain)
        max_idx = potential_gain.index(max(potential_gain))

        total_gain += max_gain
        elements = reduceArray(elements, elements[max_idx])

    return total_gain

#arr = [1, 2, 1, 3, 2, 3]
#arr = [3,4,2]

#print maxPoints(arr)

if __name__ == "__main__":
    #f = open(os.environ['OUTPUT_PATH'], 'w')
    elements_cnt = 0
    elements_cnt = int(raw_input())
    elements_i = 0
    elements = []
    while elements_i < elements_cnt:
        elements_item = int(raw_input());
        elements.append(elements_item)
        elements_i += 1


    res = maxPoints(elements);
    #f.write(str(res) + "\n")
    print res

    #f.close()