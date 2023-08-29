class Solution(object):
    def longestCommonPrefix(self, strs):
        ans = strs[0]
        ans_len = []
        for str in strs:
            for i in range(len(ans)):
                try:
                    if ans[i] == str[i]:
                        ans_len.append(ans[i])
                    else:
                        break
                except:
                    continue
            if len(ans_len) > 0:
                ans = "".join(ans_len)
                ans_len = []
            else:
                ans = ""
                break
        return ans