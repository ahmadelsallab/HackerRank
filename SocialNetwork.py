'''
Created on Oct 12, 2017

@author: linux
'''

# Complete the function below.

def socialGraphs(counts):
    groups = {}
    res = []
    for i in range(len(counts)):
        if (not (i in groups.keys())):
            groups[i] = []
        groups[i].append(counts[i])
        if len(groups[i]) == counts[i]:
            #print groups[i]
            res.append(groups[i])
            groups[i] = []
        
    return res    
    

if __name__ == "__main__":
    counts_cnt = 0
    counts_cnt = int(raw_input())
    counts_i = 0
    counts = []
    while counts_i < counts_cnt:
        counts_item = int(raw_input());
        counts.append(counts_item)
        counts_i += 1


    res = socialGraphs(counts);
    
