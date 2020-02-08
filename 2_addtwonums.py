# -*- coding:utf-8 -*-
'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        if isinstance(val, int):
            self.val = val
            self.next = None

        elif isinstance(val, list):
            self.val = val[0]
            self.next = None
            cur = self
            for i in val[1:]:
                cur.next = ListNode(i)
                cur = cur.next



class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.add_two(l1,l2)

    def add_two(self,l1,l2,add_value=0):
        if not l1 and not l2 and add_value==0:
            return None

        l1_value = l1.val if l1 else 0
        l2_value = l2.val if l2 else 0
        node_val = l1_value + l2_value +add_value

        l1_next = l1.next if l1.next else 0
        l2_next = l2.next if l2.next else 0

        if node_val >=10:
            result_node = ListNode(node_val-10)
            result_node.next = self.add_two(l1_next,l2_next,1)

        else:
            result_node = ListNode(node_val)
            result_node.next = self.add_two(l1_next,l2_next)

        return result_node

if __name__=='__main__':
    L1=ListNode([1,2])
    L2=ListNode([2,3,4])
    s=Solution()
    sum=s.addTwoNumbers(L1,L2)
    print(sum)