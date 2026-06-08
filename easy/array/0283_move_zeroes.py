"""
LeetCode: 283 移动零
难度: Easy
链接: https://leetcode.cn/problems/move-zeroes/
标签: 数组, 双指针
掌握程度: ✅
解题思路: 使用快慢双指针，慢指针指向非零元素的末尾，快指针遍历数组，遇到非零元素则写入慢指针位置并移动慢指针
关联题目: 0026 删除有序数组中的重复项、0027 移除元素
易错点: 
- 题目要求「原地修改」数组，不能使用额外空间
- 必须保持非零元素的相对顺序不变
- 空数组/全零数组的边界情况需要处理
"""

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1

if __name__ == "__main__":
    sol = Solution()
    # 测试用例1：正常移动
    nums1 = [0,1,0,3,12]
    sol.moveZeroes(nums1)
    assert nums1 == [1,3,12,0,0]

    # 测试用例2：全是零
    nums2 = [0,0,0]
    sol.moveZeroes(nums2)
    assert nums2 == [0,0,0]

    # 测试用例3：没有零
    nums3 = [1,2,3]
    sol.moveZeroes(nums3)
    assert nums3 == [1,2,3]

    # 测试用例4：零在前面
    nums4 = [0,0,1]
    sol.moveZeroes(nums4)
    assert nums4 == [1,0,0]

    print("所有测试通过！")