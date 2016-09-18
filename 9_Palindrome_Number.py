import math
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        flag = 0
        if x < 0:
            return False
        elif 0 <= x <= 9:
            return True
            
        digits = int(math.log10(abs(x)))+1
        for i in range(1,digits/2+1):
            # print i
            # print (x/pow(10,digits-i))%10, (x%pow(10,i))/pow(10,i-1)
            if (x/pow(10,digits-i))%10 != (x%pow(10,i))/pow(10,i-1):
                flag = 1
                break
            
        if flag == 1:
            return False
        else:
            return True