class Solution(object):
    def threeSumClosest(self, nums, target):
        gap = 1e9
        nums.sort()

        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1

            while left < right:
                sum_nums = nums[left] + nums[i] + nums[right]

                if sum_nums == target:
                    return sum_nums
                elif sum_nums < target:
                    left += 1
                else:
                    right -= 1

                if abs(target-sum_nums) < abs(target - gap):
                    gap = sum_nums
        return gap