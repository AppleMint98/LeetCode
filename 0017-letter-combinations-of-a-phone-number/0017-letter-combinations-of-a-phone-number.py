from itertools import product
class Solution(object):
    def letterCombinations(self, digits):
        digit_dict = {'2' : ['a','b','c'], '3' : ['d','e','f'] , '4': ['g','h','i'], '5' : ['j','k','l'], '6' : ['m','n','o'] , '7' : ['p','q','r','s'] , '8' : ['t','u','v'], '9' : ['w','x','y','z'] }

        digit_list = []
        for digit in digits:
            digit_list.append(digit_dict[digit])

        ans = product(*digit_list)
        result = [''.join(map(str, item)) for item in ans]
        
        if len(digits) == 0:
            return []
        else:
            return result