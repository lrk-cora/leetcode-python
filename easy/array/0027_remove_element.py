"""
LeetCode: 27 移除元素
难度: Easy
链接: https://leetcode.cn/problems/remove-element/
标签: 数组, 双指针
掌握程度: ✅
解题思路: 使用快慢双指针，慢指针指向保留元素的末尾，快指针遍历数组，遇到不等于val的元素则写入慢指针位置并移动慢指针
关联题目: 0026 删除有序数组中的重复项
易错点: 
- 题目要求「原地修改」数组，不能使用额外空间
"""

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow

if __name__ == "__main__":
    sol = Solution()
    # 测试用例1：正常移除
    nums1 = [3,2,2,3]
    assert sol.removeElement(nums1, 3) == 2
    assert nums1[:2] == [2, 2]

    # 测试用例2：移除所有元素
    nums2 = [0,1,2,2,3,0,4,2]
    assert sol.removeElement(nums2, 2) == 5
    assert nums2[:5] == [0,1,3,0,4]

    # 测试用例3：空数组
    nums3 = []
    assert sol.removeElement(nums3, 0) == 0

    # 测试用例4：全是要移除的元素
    nums4 = [2,2,2]
    assert sol.removeElement(nums4, 2) == 0

    print("所有测试通过！")