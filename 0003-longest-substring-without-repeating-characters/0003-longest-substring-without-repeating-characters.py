from collections import deque

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        deq = deque([])
        ans = 0
        for i in s:
            if i in deq:
                while True:
                    tmp = deq.popleft()
                    if tmp == i:
                        break
            deq.append(i)
            ans = max(ans, len(deq))
        return ans