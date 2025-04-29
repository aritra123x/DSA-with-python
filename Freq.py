#Given an array of n integers, find the most frequent element in it i.e., 
# the element that occurs the maximum number of times. If there are multiple elements that appear a maximum number of times, 
# find the smallest of them.

def mostFrequentelement(arr):
    freq={}
    for i in range(len(arr)):
        if arr[i] in freq:
            freq[arr[i]]+=1
        else:
            freq[arr[i]]=1
    max_freq = max(freq.values())
    result = min([key for key, val in freq.items() if val == max_freq])
    print(result)

if __name__=='__main__':
    arr=[2,3,5,7,2,2,3,2]
    mostFrequentelement(arr)