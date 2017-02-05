import math

# eg. 3 return "111", "001",...                   
def return_all_possible_binary(digit):
    if digit == 1:
        return ["0", "1"]
    elif digit == 2:
        return ["00", "01", "10", "11"]
    else:
        ans_list = []
        for r in return_all_possible_binary(digit-1):
            ans_list.extend(['0'+r, '1'+r])
        return ans_list
                
# eg. "010101" return 3
def count_number_of_decimal(dec_string):
    count = 0
    for s in dec_string:
        if s == '1':
            count = count + 1
    return count
    
# eg. "010101" return 21
def binaryToDecimal(b_string):
    return_dec = 0
    length = len(b_string)
    for index,b in enumerate(b_string):
        if b == '1':
            return_dec = return_dec + pow(2,length-index-1)
    return return_dec

class Solution(object):
            
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ans = []
        sec = 0
        if num == 0:
            return ["0:00"]
        elif num == 1:
            return ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]

        else: # num >= 2
            
            for hour_digit in range(0, min(num, 4)+1 ):
                
                # hour
                for r in return_all_possible_binary(4):
                    if count_number_of_decimal(r)==hour_digit and binaryToDecimal(r)<=11:
                        hour = binaryToDecimal(r);
                        
                        # Minute
                        for m in return_all_possible_binary(6):
                            if count_number_of_decimal(m)==num - hour_digit and binaryToDecimal(m)<=59:
                                minute = binaryToDecimal(m);
                                if minute < 10:
                                    ans.append(str(hour)+':0'+str(minute))
                                else:
                                    ans.append(str(hour)+':'+str(minute))
        return ans
    
            
            