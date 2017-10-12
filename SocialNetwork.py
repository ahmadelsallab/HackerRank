'''
Created on Oct 12, 2017

@author: linux
'''

# Complete the function below.
'''
import sys
def socialGraphs(counts):
    groups = {}
    res = []
    for i in range(len(counts)):
        count = counts[i]
        if (not (count in groups.keys())):
            
            groups[count] = []
        
        groups[count].append(i)
        
        if len(groups[count]) == count:
            #print groups[count]
            #print str(groups[count])
            #for members in groups[count]:
            #    print members
            #print ' '.join(str(groups[count]))
            for member in groups[count]:
                sys.stdout.write(str(member))
                sys.stdout.write(" ")
            sys.stdout.write("\n")
            res.append(groups[count])
            groups[count] = []
        
    return res  
'''
import sys
def socialGraphs(counts):
    groups = {}
    res = []
    for i in range(len(counts)):
        count = counts[i]
        if (not (count in groups.keys())):
            
            groups[count] = []
        
        groups[count].append(i)
    
    #for key, val in groups.iteritems():
    for key in reversed(sorted(groups)):
        group = groups[key]
        count = key
        for i in range(len(group)):
            sys.stdout.write(str(group[i]))
            sys.stdout.write(" ")
            if count == 1:
                if i % count == 0:
                    sys.stdout.write("\n")
            else:                
                if (i+1) % count == 0 and i != 0:
                    sys.stdout.write("\n")
    
        
    return res        
'''
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
    
'''
#counts = [2, 2, 2, 2]
#counts = [3, 3, 3, 3, 3, 1, 3]
#counts = [2, 1, 1, 2, 1]
counts = [2, 1, 1, 2, 1]
socialGraphs(counts)