"""
LeetCode: 141 环形链表
难度: Easy
链接: https://leetcode.cn/problems/linked-list-cycle/
标签: 链表, 双指针（快慢指针）
掌握程度: ⚠️
解题思路: 使用快慢指针（龟兔赛跑），慢指针每次走一步，快指针每次走两步。若链表无环，快指针会先走到末尾；若有环，快慢指针最终一定会在环内相遇。
关联题目: 142 环形链表 II
易错点: 
- 循环条件必须同时判断 `f` 和 `f.next`，避免 `f.next.next` 报错
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = head
        f = head
        while f and f.next:
            s = s.next
            f = f.next.next
            if f == s:
                return True
        return False
    
# --- 本地测试用例部分 ---
def create_cycle_linked_list(lst, pos):
    """
    创建带环的链表
    :param lst: 链表值列表
    :param pos: 环的入口索引（-1表示无环）
    :return: 链表头节点
    """
    if not lst:
        return None
    head = ListNode(lst[0])
    cur = head
    nodes = [head]
    for val in lst[1:]:
        cur.next = ListNode(val)
        cur = cur.next
        nodes.append(cur)
    # 创建环
    if pos != -1:
        cur.next = nodes[pos]
    return head


if __name__ == "__main__":
    sol = Solution()

    # 测试用例1: 有环链表
    head1 = create_cycle_linked_list([3, 2, 0, -4], 1)
    assert sol.hasCycle(head1) == True

    # 测试用例2: 有环链表（两个节点）
    head2 = create_cycle_linked_list([1, 2], 0)
    assert sol.hasCycle(head2) == True

    # 测试用例3: 无环链表
    head3 = create_cycle_linked_list([1], -1)
    assert sol.hasCycle(head3) == False

    print("所有测试通过!")