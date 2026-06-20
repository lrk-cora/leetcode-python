"""
LeetCode: 11 盛最多水的容器
难度: Medium
链接: https://leetcode.cn/problems/container-with-most-water/
标签: 数组, 相向双指针
掌握程度: ✅
解题思路: 核心指针移动规则：只移动高度更小的一侧指针。
         原因：容器盛水高度由矮柱决定，移动高侧只会让宽度缩小，面积不可能变大；移动矮侧才有可能遇到更高的柱子，从而得到更大面积。
易错点: 
- 指针移动逻辑不能搞反，永远移动高度更小的一端
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0
        while l < r:
            A = (r - l) * min(height[l], height[r])
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            if A > res:
                res = A
        return res
    
if __name__ == "__main__":
    sol = Solution()
    # 测试用例1：题目官方样例，常规场景
    assert sol.maxArea([1,8,6,2,5,4,8,3,7]) == 49
    # 测试用例2：仅两根柱子，边界最简情况
    assert sol.maxArea([1,1]) == 1
    # 测试用例3：严格递增数组
    assert sol.maxArea([1,2,3,4,5]) == 6
    # 测试用例4：严格递减数组
    assert sol.maxArea([5,4,3,2,1]) == 6
    # 测试用例5：首尾等高的特殊场景
    assert sol.maxArea([4,3,2,1,4]) == 16
    print("所有测试通过！")