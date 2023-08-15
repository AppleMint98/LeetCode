class Solution(object):
    def maxArea(self, height):
        maxvalue = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            if height[left] < height[right]:
                area = width * height[left]
                left += 1
            else:
                area = width * height[right]
                right -= 1
            maxvalue = max(maxvalue, area)
        return maxvalue