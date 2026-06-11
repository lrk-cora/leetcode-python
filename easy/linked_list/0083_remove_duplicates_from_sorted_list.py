"""
LeetCode: 83 删除排序链表重复节点
难度: Easy
链接: https://leetcode.cn/problems/remove-duplicates-from-sorted-list/
标签: 链表
掌握程度: ⚠️
解题思路: 遍历有序链表，比较当前节点与下一节点值，若值相等则跳过下一节点完成去重；不相等则移动当前指针继续遍历。
关联题目: 1047 删除字符串所有相邻重复项
易错点: 
- 循环条件需同时判断 cur 和 cur.next，避免空指针报错
- 链表已有序，只需相邻比对，无需额外排序
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

# --- 下面是测试用例部分 ---
def list_to_linked_list(lst):
    """辅助函数：把列表转为链表"""
    if not lst:
        return None
    head = ListNode(lst[0])
    cur = head
    for val in lst[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return head

def linked_list_to_list(head):
    """辅助函数：把链表转为列表"""
    res = []
    cur = head
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res

if __name__ == "__main__":
    sol = Solution()

    # 测试用例1: 常规重复链表
    head1 = list_to_linked_list([1,1,2])
    res1 = sol.deleteDuplicates(head1)
    assert linked_list_to_list(res1) == [1, 2]

    # 测试用例2: 连续重复
    head2 = list_to_linked_list([1,1,2,3,3])
    res2 = sol.deleteDuplicates(head2)
    assert linked_list_to_list(res2) == [1, 2, 3]

    # 测试用例3: 空链表
    head3 = list_to_linked_list([])
    res3 = sol.deleteDuplicates(head3)
    assert linked_list_to_list(res3) == []

    print("所有测试通过!")