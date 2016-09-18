class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        altered_str = ''
        ans = 0
        for index, x in enumerate(str):
            if '0' <= x <= '9':
                altered_str += x
            elif x == '+' or x == '-':
                if index < len(str)-1:
                    if ('0' <= str[index+1] <= '9'):
                        altered_str += x
                    else:
                        break
            else:
                break
        if altered_str == '' or altered_str == '+' or altered_str == '-':
            return ans
        
        ans = int(altered_str)
        if ans >= 2147483647:
            return 2147483647
        elif ans <= -2147483648:
            return -2147483648
        return ans
        
        # "234sdf"
        # "e234sdf"
        # "++-"
        # "+-2"
        # "   -3fsd"