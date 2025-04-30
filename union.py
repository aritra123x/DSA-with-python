#Given two sorted arrays nums1 and nums2, return an array 
# that contains the union of these two arrays. The elements in the union must be in ascending order.

def unionArray(nums1, nums2):
    m, n = len(nums1), len(nums2)
    i = 0
    j = 0
    union = set()
    
    while i < m and j < n:
        if nums1[i] == nums2[j]:
            union.add(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            union.add(nums1[i])
            i += 1
        else:
            union.add(nums2[j])
            j += 1

    while i < m:
        union.add(nums1[i])
        i += 1

    while j < n:
        union.add(nums2[j])
        j += 1

    print(union)

               

if __name__=='__main__':
     nums1 = [1, 2, 3, 4, 5]
     nums2 = [1, 2, 7]
     unionArray(nums1,nums2)