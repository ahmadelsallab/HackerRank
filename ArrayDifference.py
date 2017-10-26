'''
Created on Oct 12, 2017

@author: linux
'''

''' 
#define max(a, b) ((a > b) ? (a) : (b))
int maxDifference(int a_size, int* a) {
   
    if(a_size == 1)
    {
        return -1;
    }
    else
    {      
        int left_diff = maxDifference(a_size/2, a); 
       
        int right_size = a_size/2 + a_size%2;
        int *b = a + a_size/2;
        int right_diff = maxDifference(right_size, b);
       
        int min_left =  a[0];
        for (int i = 0; i < a_size/2; i++)
        {
            if(a[i] < min_left)
            {
                min_left = a[i];
            }
        }
       
        int max_right = b[0];
        for (int i = 0; i < right_size; i++)
        {
            if(b[i] > max_right)
            {
                max_right = b[i];
            }
        }

        int merge_diff = max_right - min_left;
        return max(merge_diff, max(right_diff, left_diff));
    }

}



}
'''


def maxDifference(a):
    if (len(a) == 1):
        return -1

    else:
        n = len(a)
        n_by_2 = n / 2 + n % 2
        left_arr = a[0:n_by_2]
        right_arr = a[n_by_2:]

        left_diff = maxDifference(left_arr)
        right_diff = maxDifference(right_arr)

        # O(n)
        min_left = min(left_arr)
        max_right = max(right_arr)

        merge_diff = max_right - min_left
        return max(merge_diff, max(right_diff, left_diff))
if __name__ == "__main__":
    f = open(os.environ['OUTPUT_PATH'], 'w')
    a_cnt = 0
    a_cnt = int(raw_input())
    a_i = 0
    a = []
    while a_i < a_cnt:
        a_item = int(raw_input());
        a.append(a_item)
        a_i += 1


    res = maxDifference(a);
    f.write(str(res) + "\n")

    f.close()
if __name__ == '__main__':
    pass