"""
LeetCode: 1 两数之和
难度: Easy 
链接: https://leetcode.cn/problems/two-sum/
标签: 数组, 哈希表
掌握程度: ⚠️
解题思路: 遍历数组，用哈希表存储已遍历元素及其索引，通过 target - 当前值 查找互补元素
关联题目: 167 两数之和 II
易错点: 
- 同一个元素不能被使用两次，需在遍历到当前元素时再检查哈希表
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_dict = {}
        for ind, num in enumerate(nums):
            need = target - num
            if need in hash_dict:
                return [hash_dict[need], ind]
            else:
                hash_dict[num] = ind

if __name__ == "__main__":
    sol = Solution()
    assert sol.twoSum([2,7,11,15], 9) == [0, 1]
    assert sol.twoSum([3,2,4], 6) == [1, 2]
    assert sol.twoSum([3,3], 6) == [0, 1]
    print("测试通过")