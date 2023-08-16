class Solution(object):
    def reverse(self, x):
        x = str(x)
        ans = 0
        if x[0] == '-':
            x = x[1:]
            ans = -int(x[::-1])
        else:
            ans = int(x[::-1])
        
        if ans < -2**31 or ans > 2**31:
            return 0
        else:
            return ans