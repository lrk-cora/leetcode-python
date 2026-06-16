"""
LeetCode: 15 三数之和
难度: Medium
链接: https://leetcode.cn/problems/3sum/
标签: 数组, 排序, 相向双指针
掌握程度: ⚠️
解题思路: 
1. 先对数组升序排序，为双指针创造有序条件，同时方便跳过重复数字
2. 若 nums[i] > 0，后面全为正数，三数之和不可能为0，直接剪枝退出循环
3. 跳过重复的 i，避免生成完全相同的三元组
4. 左指针 left = i+1，右指针 right = 数组末尾，相向收缩
关联题目:167. 两数之和 II - 输入有序数组（基础双指针模板、18. 四数之和（多层循环+双指针拓展）
易错点: 
- 注意去重
- 指针移动时要避免越界，循环条件为 `left < right`
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            else:
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    sm = nums[i] + nums[left] + nums[right]
                    if sm < 0:
                        left += 1
                    elif sm > 0:
                        right -= 1
                    else:
                        res.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
        return res
    
if __name__ == "__main__":
    sol = Solution()
    # 测试用例1：常规多解场景
    assert sol.threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
    # 测试用例2：空数组，无解
    assert sol.threeSum([]) == []
    # 测试用例3：三个0，唯一解
    assert sol.threeSum([0,0,0]) == [[0,0,0]]
    # 测试用例4：长度不足，无解
    assert sol.threeSum([0,1,1]) == []
    print("所有测试通过！")