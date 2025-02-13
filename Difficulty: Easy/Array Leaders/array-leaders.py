class Solution:
    def leaders(self, arr):
        length = len(arr)
        leaders_list = []
        leader = arr[-1]
        leaders_list.append(leader)

        for i in range(length-2,-1,-1):
            if arr[i] >= leader:
                leader = arr[i]
                leaders_list.append(leader)

        result = leaders_list[::-1]
        return result


#{ 
 # Driver Code Starts
t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().leaders(arr)  # find the leaders

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print leaders in the required order
    else:
        print("[]")  # Print empty list if no leaders are found

    print("~")

# } Driver Code Ends