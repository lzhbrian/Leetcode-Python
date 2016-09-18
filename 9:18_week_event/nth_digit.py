import math
class Solution(object):
    def findNthDigit(self, n):
        index = 0
        if 1 <= n <= 9:
            return n
        for x in range(0,9):
            index += 9*pow(10,x)*(x+1)
            if index < n <= index + 9*pow(10,x+1)*(x+2):
                i = int(math.ceil( float(n-index)/(x+2) ))
                m = (n-index)%(x+2)
                string_i = str(pow(10,x+1)+i-1)
                if m==0:
                    return int(string_i[x+1])
                else:
                    return int(string_i[m-1])
                

        