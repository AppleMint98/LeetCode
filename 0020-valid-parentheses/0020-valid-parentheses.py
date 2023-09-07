from collections import deque

class Solution(object):
    def isValid(self, s):
        deq = deque()
        input_deq = ['(','{','[']
        output_deq = [')','}',']']
        for i in s:
            if i in input_deq:
                deq.append(i)
            else:
                tmp_index = output_deq.index(i)
                if len(deq) > 0:
                    deq_pop = deq.pop()
                    if deq_pop == input_deq[tmp_index]:
                        continue
                    else:
                        return False
                else:
                    return False
        if len(deq) == 0:
            return True
        else:
            return False




