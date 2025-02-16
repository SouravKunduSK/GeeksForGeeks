#User function template for Python 3

class Solution:
    def majorityElement(self, arr):
        #Your code here
        length = len(arr)
        candidate = None
        count = 0
        # finding candidate by using boyer-moore algorithm
        for num in arr:
            if count == 0:
                candidate = num
            if candidate == num:
                count +=1
            else:
                count -=1

        # verifying the candidate
        count = 0
        for num in arr:
            if num == candidate:
                count +=1

        if count > length // 2:
            return candidate
        else:
            return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.majorityElement(A))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends