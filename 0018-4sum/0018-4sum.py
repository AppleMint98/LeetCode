class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        ans = set()

        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                left = j + 1
                right = len(nums) - 1

                while left < right:
                    nums_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    # print('i, j, left, right :', i, j, left, right)
                    # print('nums[i], nums[j], nums[left], nums[right]', nums[i], nums[j], nums[left], nums[right])
                    # print('nums_sum : ', nums_sum)
                    # print()

                    if nums_sum == target:
                        ans.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                    elif nums_sum < target:
                        left += 1
                    else:
                        right -= 1

        return list(ans)