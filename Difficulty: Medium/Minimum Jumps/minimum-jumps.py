#User function Template for python3
class Solution:
	def minJumps(self, arr):
	    # code here
	    length = len(arr)
        if length <= 1 or arr[0] == 0:
            return -1
    
        jums_count = 0
        max_steps = 0
        current_end = 0

        for i in range (length):
            max_steps = max(max_steps, i+arr[i])

            if i == current_end:
                jums_count +=1
                current_end = max_steps

                if current_end >= length-1:
                    return jums_count
            
            if i >= max_steps:
                return -1
        
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        # n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr)
        print(ans)
        print("~")
# } Driver Code Ends