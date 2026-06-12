"""
LeetCode: 217 存在重复元素
难度: Easy
链接: https://leetcode.cn/problems/contains-duplicate/
标签: 数组, 哈希集合
掌握程度: ✅
解题思路: 借助集合遍历数组，遍历过程中判断当前元素是否已存在于集合中，存在则说明有重复，直接返回 True；不存在则将元素加入集合。遍历结束无重复则返回 False。
关联题目: 136 只出现一次的数字
易错点: 
- 集合查询效率高，适合快速判重
- 遍历中途发现重复可立即终止，无需遍历完全部数组
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        se = set()
        for i in nums:
            if i in se:
                return True
            se.add(i)
        return False

if __name__ == "__main__":
    sol = Solution()
    assert sol.containsDuplicate([1,2,3,1]) == True
    assert sol.containsDuplicate([1,2,3,4]) == False
    assert sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True
    print("所有测试通过!")