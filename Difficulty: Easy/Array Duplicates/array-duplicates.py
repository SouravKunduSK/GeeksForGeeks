
class Solution:
    def findDuplicates(self,arr):
        newList = []
        seen = set()
        if(len(arr)<=1):
            return []
    
        for num in arr:
            if num in seen:
                newList.append(num)
            else:
                seen.add(num)
        return newList


#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().findDuplicates(arr)  # find the duplicates
    # Sort the result in ascending order
    s.sort()
    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print duplicates in ascending order
    else:
        print("[]")  # Print empty list if no duplicates are found
    print("~")

# } Driver Code Ends