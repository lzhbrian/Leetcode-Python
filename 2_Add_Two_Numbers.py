# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        v1 = l1.val
        v1_node = l1
        v2 = l2.val
        v2_node = l2
        
        f1 = 0
        f2 = 0
        add = 0
        temp_ans = []
        while 1:
            print v1,v2
            sum = v1 + v2 + add
            if sum >= 10:
                add = 1
            else:
                add = 0
            
            temp_ans.append( sum%10 )
            
            if v1_node.next != None:
                v1_node = v1_node.next
                v1 = v1_node.val
            else:
                f1 = 1
                v1 = 0
            if v2_node.next != None:
                v2_node = v2_node.next
                v2 = v2_node.val
            else:
                f2 = 1
                v2 = 0
                
            if f1 == 1 and f2 == 1:
                if add == 1:
                    temp_ans.append(add)
                break

        flag = 0
        flag_2 = 0
        return_ans = ListNode(temp_ans[0])
        for t in temp_ans:
            if flag == 0:
                flag = 1
                continue
            elif flag_2 == 0:
                flag_2 = 1
                t_node = ListNode(t)
                return_ans.next = t_node
                continue
            else:
                previous_t_node = t_node
                t_node = ListNode(t)
                previous_t_node.next = t_node

        return return_ans

