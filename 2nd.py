def secondLargestElement(arr):
    if len(arr) < 2:
        return -1 
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num < first:
            second = num
    return second if second != float('-inf') else -1

if __name__=='__main__':
    arr=[8, 8, 7, 6, 5]
    print(secondLargestElement(arr))
