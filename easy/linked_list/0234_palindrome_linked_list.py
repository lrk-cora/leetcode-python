"""
LeetCode: 234 回文链表
难度: Easy
链接: https://leetcode.cn/problems/palindrome-linked-list/
标签: 链表、快慢指针、链表反转
掌握程度: 🔴
解题思路: 先用快慢指针找到链表中点，反转后半段链表；再分别从原链表头部、反转后的后半段开始逐节点比对，全部相等则为回文链表。
关联题目: 141 环形链表、206 反转链表
易错点: 
- 快慢指针取中点逻辑，区分奇偶长度链表
- 后半段反转后再逐一比较节点值，不要遗漏边界判断
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(node):
            pre = None
            while node:
                nxt = node.next
                node.next = pre
                pre = node
                node = nxt
            return pre
        slow, fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        half_right = reverse(slow)
        p1, p2 = head, half_right
        while p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True
    
# 测试辅助函数
def list_to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    curr = head
    for val in lst[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

if __name__ == "__main__":
    sol = Solution()

    # 偶数个节点回文
    h1 = list_to_linked_list([1,2,2,1])
    assert sol.isPalindrome(h1) == True

    # 奇数个节点回文
    h2 = list_to_linked_list([1,2,3,2,1])
    assert sol.isPalindrome(h2) == True

    # 非回文链表
    h3 = list_to_linked_list([1,2])
    assert sol.isPalindrome(h3) == False

    # 单节点
    h4 = list_to_linked_list([1])
    assert sol.isPalindrome(h4) == True

    print("所有测试通过!")