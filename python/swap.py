class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        abc = len(s)
        
        # Correct the division for even and odd cases
        if abc % 2 != 0:
            ans = abc // 2
            right = ans
            left = ans + 1
        else:
            ans = abc // 2
            right = ans
            left = ans - 1
        
        # Swap the elements from the two ends inward
        for i in range(0, right):
            temp = s[i]
            s[i] = s[abc - 1 - i]
            s[abc - 1 - i] = temp
            
        return s
