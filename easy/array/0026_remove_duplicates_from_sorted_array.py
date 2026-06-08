"""
LeetCode: 26 删除有序数组中的重复项
难度: Easy
链接: https://leetcode.cn/problems/remove-duplicates-from-sorted-array/
标签: 数组, 双指针
掌握程度: ✅
解题思路: 使用快慢双指针，慢指针指向无重复元素的末尾，快指针遍历数组，遇到新元素则写入慢指针位置并移动慢指针
关联题目: 0027 移除元素
易错点: 
- 题目要求「原地修改」数组，不能使用额外空间
"""

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1
    
if __name__ == "__main__":
    sol = Solution()
    # 测试用例1：正常去重
    nums1 = [1,1,2]
    assert sol.removeDuplicates(nums1) == 2
    assert nums1[:2] == [1, 2]

    # 测试用例2：全是重复元素
    nums2 = [0,0,1,1,1,2,2,3,3,4]
    assert sol.removeDuplicates(nums2) == 5
    assert nums2[:5] == [0,1,2,3,4]

    # 测试用例3：空数组
    nums3 = []
    assert sol.removeDuplicates(nums3) == 0

    # 测试用例4：长度为1的数组
    nums4 = [1]
    assert sol.removeDuplicates(nums4) == 1

    print("所有测试通过！")