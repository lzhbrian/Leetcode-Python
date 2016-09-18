import math
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        elif x < 0:
            ans_t = ''
            st = str(abs(x))
            for s in st:
                ans_t = s + ans_t
            ans = -int(ans_t)
        elif x > 0:
            ans_t = ''
            st = str(x)
            for s in st:
                ans_t = s + ans_t
            ans = int(ans_t)
        
        
        if ans >= pow(2,31)-1 or ans <= -pow(2,31):
            return 0
        return ans
        
        # 6463847412
        # 1000