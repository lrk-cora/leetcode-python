"""
LeetCode: 349 两个数组的交集
难度: Easy
链接: https://leetcode.cn/problems/intersection-of-two-arrays/
标签: 数组, 哈希集合
掌握程度: ✅
解题思路: 将两个数组转为集合，利用集合交集运算得到共同元素，最后转回列表返回。集合会自动去重，符合题目要求。
关联题目: 217 存在重复元素
易错点: 
- 结果元素唯一，无需手动去重
- 集合交集运算简洁高效
"""

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1 & set2)

if __name__ == "__main__":
    sol = Solution()
    assert sol.intersection([1,2,2,1], [2,2]) == [2]
    assert sol.intersection([4,9,5], [9,4,9,8,4]) == [9,4]
    assert sol.intersection([], [1,2]) == []
    print("所有测试通过!")