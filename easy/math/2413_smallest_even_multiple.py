"""
LeetCode: 2413 最小偶倍数
难度: Easy
链接: https://leetcode.cn/problems/smallest-even-multiple/
标签: 数学
掌握程度: ✅
解题思路: 若 n 是偶数，最小偶倍数就是自身；若 n 是奇数，最小偶倍数为 2 * n。
关联题目: 无
易错点: 无
"""

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 != 0:
            res = 2 * n
        else:
            res = n
        return res
    
    """
    # 精简写法
    def smallestEvenMultiple(self, n: int) -> int:
    return n if n % 2 == 0 else n * 2
    """

if __name__ == "__main__":
    sol = Solution()
    assert sol.smallestEvenMultiple(5) == 10
    assert sol.smallestEvenMultiple(6) == 6
    assert sol.smallestEvenMultiple(1) == 2
    print("所有测试通过!")