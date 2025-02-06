class Solution:
    def maxSubArraySum(self, arr):
        # Your code here
        max_sum = arr[0]
        current_sum = 0

        for value in arr:
            current_sum += value
            max_sum = max(current_sum, max_sum)
            if(current_sum<0):
                current_sum = 0
        
        return max_sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends