from typing import List

class Solution:
    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        n = len(nums)
        for i in range(n):
            hashmap = {}
            for j in range(i + 1, n):
                target = -(nums[i] + nums[j])
                if target in hashmap:
                    triplet = tuple(sorted([nums[i], nums[j], target]))
                    ans.add(triplet)
                hashmap[nums[j]] = j
        return [list(t) for t in ans]

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return ans
