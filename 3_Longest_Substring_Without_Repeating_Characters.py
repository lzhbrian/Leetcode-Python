
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = maxlength = 0
        usedChar = {}   # A hashtable

        for i in range(len(s)):

            # If the overwatch substring contain the current pattern, then ...
            # Move the 'Start_Place' to 'Precious_Place_of_Current_Pattern' + 1
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxlength = max(maxlength, i - start + 1)

            usedChar[s[i]] = i

        return maxlength

        # Max_Length = 0
        # Target_Place = HASH()
        # for Current_Place, Current_Character in numerate(string):
            # If the overwatch substring contain the current pattern, then ...
            # Move the 'Start_Place' to 'Precious_Place_of_Current_Pattern' + 1
        #   if Start_Place <= Target_Place[ Current_Character ]:
                # Move the 'Start_Place' to 'Precious_Place_of_current_pattern' + 1
        #       Start_Place = Target_Place + 1
        #   else:
        #       Max_Length = Current_Place - Start_Place + 1
        #   Target_Place[ Current_Character ] = Current_Place
        # return Max_Length

# TLE Version - Brute Force
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         return_list = []
#         length = len(s)
#         max = 0
#         for i in range(0,length):
#             uni_list = [ s[i] ]
#             count = 1
#             for j in range(i+1,length):
#                 # print s[j]
#                 # print uni_list
#                 if s[j] not in uni_list:
#                     count = count + 1
#                     uni_list.append(s[j])
#                 else:
#                     if count > max:
#                         max = count
#                     break
#         if length == 1:
#             max = 1
#         if length == 0:
#             max = 0
#         return max