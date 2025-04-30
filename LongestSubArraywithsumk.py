#Given an array arr[] containing integers and an integer k, 
# your task is to find the length of the longest subarray 
# where the sum of its elements is equal to the given value k. If there is no subarray with sum equal to k


# Naive Approach TC=O(n^2)
def longestSubarray1(arr,k):
    maxlen=0
    for i in range(len(arr)):
        sum=0
        for j in range(i,len(arr)):
            sum+=arr[j]
            if sum==k:
                maxlen=max((j-i+1),maxlen)
    return maxlen

# Better Approach with dictionary/hashmap TC=O(nlogn/n/n^2) SC=O(n):
def longestSubarray2(arr,k):
        maxlen = 0
        prefix_map = {}
        curr_sum = 0
        
        for i in range(len(arr)):
            curr_sum += arr[i]
            
            if curr_sum == k:
                maxlen = i + 1
            
            if (curr_sum - k) in prefix_map:
                maxlen = max(i - prefix_map[curr_sum - k], maxlen)
            
            if curr_sum not in prefix_map:
                prefix_map[curr_sum] = i
        
        return maxlen

#Best approach using 2 pointers
def longestSubarray3(arr,k):
    left=right=0
    sum=0
    n=len(arr)
    maxlen=0
    while right<n:
        while left<=right and sum>k:
            sum-=arr[left]
            left+=1
        if sum==k:
            maxlen=max(maxlen,right-left+1)
        right+=1
        if right<n:
            sum+=arr[right]
    return maxlen

if __name__=='__main__':
    arr=[5, 8, 14, 2, 4, 12] 
    k = 5
    print(longestSubarray3(arr,k))