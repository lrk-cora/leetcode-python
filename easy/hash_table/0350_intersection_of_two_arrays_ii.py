"""
LeetCode: 350 两个数组的交集 II
难度: Easy
链接: https://leetcode.cn/problems/intersection-of-two-arrays-ii/
标签: 数组, 双指针, 排序
掌握程度: ✅
解题思路: 先对两个数组排序，再用双指针遍历，当两指针指向元素相等时加入结果并同时后移；不等则移动数值较小的指针，直到任一数组遍历完成。
关联题目: 349 两个数组的交集
易错点: 
- 排序后再用双指针，可同时处理重复元素
- 指针移动条件要区分大小，避免死循环
"""

from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        s = 0
        l = 0
        res = []
        while s < len(nums1) and l < len(nums2):
            if nums1[s] == nums2[l]:
                res.append(nums1[s])
                s += 1
                l += 1
            elif nums1[s] < nums2[l]:
                s += 1
            else:
                l += 1
        return res
    
if __name__ == "__main__":
    sol = Solution()
    assert sol.intersect([1,2,2,1], [2,2]) == [2,2]
    assert sol.intersect([4,9,5], [9,4,9,8,4]) == [4,9]
    assert sol.intersect([1,2,3,4], []) == []
    print("所有测试通过!")