"""
LeetCode: 496 下一个更大元素 I
难度: Easy
链接: https://leetcode.cn/problems/next-greater-element-i/
标签: 栈, 哈希表, 单调栈
掌握程度: 🔴
解题思路: 用单调栈遍历 nums2，为每个元素找到它右边第一个更大的元素，并用哈希表存储结果；最后根据 nums1 直接查表得到答案。
关联题目: 739 每日温度, 503 下一个更大元素 II
易错点: 
- 遍历结束后，栈中剩余元素的下一个更大元素都为 -1
"""

from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        bigger = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                out = stack.pop()
                bigger[out] = num
            stack.append(num)
        while stack:
            bigger[stack.pop()] = -1
        return [bigger[x] for x in nums1]
    
if __name__ == "__main__":
    sol = Solution()

    # 常规用例
    assert sol.nextGreaterElement([4,1,2], [1,3,4,2]) == [-1,3,-1]
    assert sol.nextGreaterElement([2,4], [1,2,3,4]) == [3,-1]
    # 单个元素
    assert sol.nextGreaterElement([5], [5]) == [-1]
    # 递减序列
    assert sol.nextGreaterElement([3,2,1], [3,2,1]) == [-1,-1,-1]

    print("所有测试通过!")