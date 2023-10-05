class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        n = len(nums)
        nums.sort()
        res = []
        count = 1
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                if count > n//3:
                    res.append(nums[i-1])
                count = 1
        if count > n//3:
            res.append(nums[n-1])
        return res