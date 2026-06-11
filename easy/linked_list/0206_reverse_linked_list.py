"""
LeetCode: 206 反转链表
难度: Easy
链接: https://leetcode.cn/problems/reverse-linked-list/
标签: 链表, 迭代
掌握程度: ⚠️
解题思路: 双指针迭代法，用 prev 记录前驱节点、cur 遍历当前节点。每次先保存后继节点，再将当前节点指向前驱，依次向后移动指针，最终 prev 成为新头节点。
关联题目: 83 删除排序链表中的重复元素
易错点: 
- 必须提前暂存 cur.next，防止断链丢失后续节点
- 初始 prev 设为 None，链表尾部最终指向空
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev

# 测试辅助函数 & 用例
def list_to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    curr = head
    for v in lst[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head

def linked_list_to_list(head):
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res

if __name__ == "__main__":
    sol = Solution()

    # 常规链表
    h1 = list_to_linked_list([1,2,3,4,5])
    assert linked_list_to_list(sol.reverseList(h1)) == [5,4,3,2,1]

    # 单节点
    h2 = list_to_linked_list([1])
    assert linked_list_to_list(sol.reverseList(h2)) == [1]

    # 空链表
    h3 = list_to_linked_list([])
    assert linked_list_to_list(sol.reverseList(h3)) == []

    print("所有测试通过!")