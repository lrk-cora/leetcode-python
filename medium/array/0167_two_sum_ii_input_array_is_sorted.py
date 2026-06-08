"""
LeetCode: 167 两数之和 II - 输入有序数组 
难度: Medium
链接: https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/
标签: 数组, 双指针
掌握程度: ⚠️
解题思路: 利用数组有序的特性，使用左右双指针：左指针指向数组开头，右指针指向末尾；计算两数之和，若和小于目标则左指针右移（增大和），若和大于目标则右指针左移（减小和），直到找到和为目标的两个数
关联题目: 0001 两数之和
易错点: 
- 题目要求返回的是「1-based 索引」，而不是数组的0-based下标
- 数组一定有且仅有一个解，无需处理无解情况
- 指针移动时要避免越界，循环条件为 `left < right`
"""

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        res = numbers[left] + numbers[right]
        while res != target:
            if res < target:
                left += 1
            else:
                right -= 1
            res = numbers[left] + numbers[right]
        return [left + 1, right + 1]

if __name__ == "__main__":
    sol = Solution()
    # 测试用例1：正常情况
    assert sol.twoSum([2,7,11,15], 9) == [1,2]
    # 测试用例2：中间两个数
    assert sol.twoSum([2,3,4], 6) == [1,3]
    # 测试用例3：首尾两个数
    assert sol.twoSum([-1,0], -1) == [1,2]
    print("所有测试通过！")