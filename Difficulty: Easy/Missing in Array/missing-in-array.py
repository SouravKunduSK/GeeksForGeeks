#User function Template for python3
class Solution:
    def missingNumber(self, arr):
        # code here
        n = len(arr) + 1
        sum_till_n = n*(n+1)/2
        sum_of_array = 0
        for i in range(len(arr)):
            sum_of_array += arr[i]

        missing_number = sum_till_n - sum_of_array

        return int(missing_number)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    arr = list(map(int, input().split()))
    s = Solution().missingNumber(arr)
    print(s)

    print("~")
# } Driver Code Ends