class Solution(object):
    def isPalindrome(self, x):
        list_x = list(str(x))
        reverse_list_x = list(reversed(list_x))
        print(list_x, reverse_list_x)
        
        if list_x == reverse_list_x:
            return True
        else:
            False