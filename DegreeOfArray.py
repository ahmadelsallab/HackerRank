class BruteForceSolution:
    def __init__(self):
        return
    def getSubArrayDegree(self, arr):
        freq = {}

        # O(n)
        for a in arr:
            if a in freq:
                freq[a] += 1
            else:
                freq[a] = 0

        # O(n)
        '''
        max_freq = 0
        for key in freq.keys():
            if freq[key] > max_freq:
                max_freq = freq[key]
    
        return max_freq
        '''
        return max(freq.values())
    def degreeOfArray(self, arr):
        max_arr_deg = self.getSubArrayDegree(arr)
        # O(n^2)
        min_sub_arr_len = len(arr)
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                sub_arr = arr[i:j]
                if(len(sub_arr) < min_sub_arr_len and self.getSubArrayDegree(sub_arr) == max_arr_deg):
                    min_sub_arr_len = len(sub_arr)
        return min_sub_arr_len


class Solution:
    def __init__(self):
        return

    def degreeOfArray(self, arr):
        freq_idx = {} #(freq, min_idx, max_idx)

        # O(n)
        max_freq = 0
        for i in range(len(arr)):
            a = arr[i]
            if a in freq_idx:
                l = list(freq_idx[a])
                l[0] += 1
                l[2] = i
                freq_idx[a] = l

            else:
                freq_idx[a] = (1, i, i)
            if(freq_idx[a] > max_freq):
                max_freq = freq_idx[a][0]

        # O(n)
        min_sub_arr_len = len(arr)
        for key in freq_idx.keys():
            sub_arr_len = freq_idx[key][2] - freq_idx[key][1] + 1
            if sub_arr_len < min_sub_arr_len and freq_idx[key][0] == max_freq:
                min_sub_arr_len = sub_arr_len

        return min_sub_arr_len





a = [1, 2, 2, 3, 1]
solution = Solution()
print solution.degreeOfArray(a)