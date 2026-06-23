"""
LeetCode: 977 有序数组的平方
难度: Easy
链接: https://leetcode.cn/problems/squares-of-a-sorted-array/
标签: 数组、双指针
掌握程度: ✅
解题思路: 采用左右双指针分别指向数组首尾，比较两端元素平方值大小，将较大值从结果数组的尾部向前倒序存放，对应指针向内收缩，最终得到升序平方数组，时间复杂度 O(n)。
关联题目: 无
易错点: 
- 左右指针循环条件为 l <= r，需要处理左右指针重合的最后一个元素；
- 结果数组必须预先初始化定长数组，从末尾逆序填充，不要正序追加。
"""

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        res = [0] * len(nums)
        idx = len(nums) - 1
        while l <= r:
            if nums[l] ** 2 > nums[r] ** 2:
                res[idx] = nums[l] ** 2
                l += 1
            else:
                res[idx] = nums[r] ** 2
                r -= 1
            idx -= 1
        return res
    
if __name__ == "__main__":
    sol = Solution()
    # 测试用例1：常规正负混合数组
    assert sol.sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    # 测试用例2：全负数数组
    assert sol.sortedSquares([-7, -3, -2]) == [4, 9, 49]
    # 测试用例3：全正数数组
    assert sol.sortedSquares([1, 2, 5, 8]) == [1, 4, 25, 64]
    # 测试用例4：单个元素边界
    assert sol.sortedSquares([-5]) == [25]
    # 测试用例5：包含0的边界数组
    assert sol.sortedSquares([0]) == [0]
    print("所有测试通过！")