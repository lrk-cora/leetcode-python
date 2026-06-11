"""
LeetCode: 876 链表的中间结点
难度: Easy
链接: https://leetcode.cn/problems/middle-of-the-linked-list/
标签: 链表, 快慢指针
掌握程度: ✅
解题思路: 快慢指针法，慢指针每次走一步，快指针每次走两步。快指针走到链表末尾时，慢指针恰好停在中间位置；偶数长度链表取靠后中间节点。
关联题目: 141 环形链表、234 回文链表
易错点: 
- 循环条件为 fast and fast.next，保证不会空指针访问
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
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

def get_node_val(node):
    return node.val if node else None

if __name__ == "__main__":
    sol = Solution()

    # 奇数个节点
    h1 = list_to_linked_list([1,2,3,4,5])
    assert get_node_val(sol.middleNode(h1)) == 3

    # 偶数个节点，取后一个中间节点
    h2 = list_to_linked_list([1,2,3,4,5,6])
    assert get_node_val(sol.middleNode(h2)) == 4

    # 单节点
    h3 = list_to_linked_list([1])
    assert get_node_val(sol.middleNode(h3)) == 1

    print("所有测试通过!")