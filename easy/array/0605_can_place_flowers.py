"""
LeetCode: 605 种花问题 
难度: Easy
链接: https://leetcode.cn/problems/can-place-flowers/
标签: 数组, 贪心
掌握程度: ⚠️
解题思路: 遍历数组，遇到空位时，同时检查左右两侧是否为空（或为边界）；若满足条件则在此处种花并计数，中途种够n朵即可提前返回True，遍历结束后判断计数是否达标
关联题目: 无
易错点: 
- 边界处理：首尾位置只需判断单侧邻居
- 种花后必须修改原数组，避免后续位置误判
- 输入n=0的特殊情况需要直接返回True
"""

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # 边界处理：n=0时直接返回True
        if n == 0:
            return True
        count = 0
        m = len(flowerbed)
        for i in range(m):
            if flowerbed[i] == 0:
                if (i == 0 or flowerbed[i - 1] == 0) and (i == m - 1 or flowerbed[i + 1] == 0):
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True
        return count >= n

if __name__ == "__main__":
    sol = Solution()
    # 测试用例1：可以种
    assert sol.canPlaceFlowers([1,0,0,0,1], 1) == True
    # 测试用例2：不可以种
    assert sol.canPlaceFlowers([1,0,0,0,1], 2) == False
    # 测试用例3：首尾位置种花
    assert sol.canPlaceFlowers([0,0,1,0,0], 2) == True
    # 测试用例4：n=0的边界
    assert sol.canPlaceFlowers([1], 0) == True
    print("所有测试通过！")