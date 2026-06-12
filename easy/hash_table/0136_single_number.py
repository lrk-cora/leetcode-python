"""
LeetCode: 136 只出现一次的数字
难度: Easy
链接: https://leetcode.cn/problems/single-number/
标签: 位运算, 数组
掌握程度: ✅
解题思路: 利用异或运算特性：相同数字异或结果为0，0异或任何数字等于其本身。遍历数组不断异或，最终结果即为唯一出现一次的数。
关联题目: 260 只出现一次的数字 III
易错点: 
- 熟练掌握异或运算的性质
"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ini = 0
        for i in nums:
            ini ^= i 
        return ini
    
if __name__ == "__main__":
    sol = Solution()
    assert sol.singleNumber([2,2,1]) == 1
    assert sol.singleNumber([4,1,2,1,2]) == 4
    assert sol.singleNumber([1]) == 1
    print("所有测试通过!")