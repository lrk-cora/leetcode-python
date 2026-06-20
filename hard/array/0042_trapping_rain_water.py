"""
LeetCode: 42 接雨水
难度: Hard
链接: https://leetcode.cn/problems/trapping-rain-water/
标签: 数组, 相向双指针
掌握程度: 🔴
解题思路: 
1. 每次先更新当前左右侧的最大高度，利用短板原理：容器蓄水量由较矮一侧的柱子决定。
2. 若左柱高度更小，水位由左侧最大值left_max决定，计算当前left位置蓄水量，左指针右移；
   若右柱高度更小/相等，水位由右侧最大值right_max决定，计算当前right位置蓄水量，右指针左移。
关联题目:11.盛最多水的容器、15.三数之和、18.四数之和
易错点: 
- 必须先更新左右侧最大高度，再计算水量，最大值是当前指针走过区域的最高柱。
- 水位高度取左右最大值的较小值，用最大值减去当前柱高得到本列存水量。
"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        res = 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if height[left] < height[right]:
                res += left_max - height[left]
                left += 1
            else:
                res += right_max - height[right]
                right -= 1
        return res
    
# 另一个思路
"""
标签: 数组, 排序, 相向双指针
解题思路: 动态规划预处理两个数组：
         leftMax数组：leftMax[i] 代表下标i左侧（包含i）所有柱子的最大高度，从左向右遍历生成。
         rightMax数组：rightMax[i] 代表下标i右侧（包含i）所有柱子的最大高度，从右向左遍历生成。
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        leftMax = [height[0]] + [0] * (n - 1)
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax = [0] * (n - 1) + [height[n - 1]]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        ans = sum(min(leftMax[i], rightMax[i]) - height[i] for i in range(n))
        return ans

if __name__ == "__main__":
    sol = Solution()
    # 测试用例1：题目官方示例1
    assert sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    # 测试用例2：题目官方示例2
    assert sol.trap([4,2,0,3,2,5]) == 9
    # 测试用例3：严格递增数组，无法接住雨水
    assert sol.trap([1,2,3,4,5]) == 0
    # 测试用例4：严格递减数组，无法接住雨水
    assert sol.trap([5,4,3,2,1]) == 0
    # 测试用例5：数组长度不足2，边界无解
    assert sol.trap([2]) == 0
    print("所有测试通过！")