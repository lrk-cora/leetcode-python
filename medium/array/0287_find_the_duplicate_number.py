"""
LeetCode: 287 寻找重复数
难度: Medium
链接: https://leetcode.cn/problems/find-the-duplicate-number/
标签: 数组, 快慢双指针, Floyd判圈算法(龟兔赛跑), 链表判环
掌握程度: 🔴
解题思路: 
1. 模型转换：将数组nums虚拟成链表，索引i视为链表节点，nums[i]视为当前节点指向的下一个索引节点
   数组范围[1,n]、长度n+1，必然存在重复数字，等价于链表必然存在环，**重复数字就是链表环的入口节点**
2. 第一轮快慢指针赛跑：慢指针s一次走1步，快指针f一次走2步，快慢指针一定会在环内相遇，证明存在环
3. 第二轮同速指针找环入口：相遇后将慢指针重置到起点下标0，快慢指针都改为每次走1步，再次相遇的节点即为环入口，也就是重复数字
关联题目: 141.环形链表、142.环形链表II
易错点: 
- 第一轮快慢指针的相遇点 ≠ 环入口，不能直接返回相遇位置的值，必须执行第二轮指针遍历
- 指针移动的逻辑是【索引跳转】s = nums[s]，不是索引自增s += 1，容易混淆指针移动方式
"""

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = f = 0
        while True:
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break
        s = 0
        while s != f:
            s = nums[s]
            f = nums[f]
        return s
    
if __name__ == "__main__":
    sol = Solution()
    # 测试用例1：题目示例1 常规数组
    assert sol.findDuplicate([1,3,4,2,2]) == 2
    # 测试用例2：题目示例2 重复数字靠前
    assert sol.findDuplicate([3,1,3,4,2]) == 3
    # 测试用例3：极端用例，数组全部为同一个数字
    assert sol.findDuplicate([3,3,3,3,3]) == 3
    # 测试用例4：小数组边界场景
    assert sol.findDuplicate([1,1]) == 1
    # 测试用例5：长度稍大的数组场景
    assert sol.findDuplicate([2,1,5,3,4,5,6]) == 5
    print("所有测试通过！")