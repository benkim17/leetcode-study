class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            diff = self.twoSum(nums, i, diff, target) # 1
        return target - diff

    def twoSum(self, nums: List[int], i: int, diff: float, target: int) -> float:
        l, r = i + 1, len(nums) - 1
        while (l < r):
            sum = nums[i] + nums[l] + nums[r]
            if abs(target - sum) < abs(diff):
                diff = target - sum 
            if sum < target:
                l += 1 
            else:
                r -= 1
        return diff

    # 1. integers and floats are passed by value and not by reference(primitive types)


        
