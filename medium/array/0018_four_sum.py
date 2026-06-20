"""
LeetCode: 18 四数之和
难度: Medium
链接: https://leetcode.cn/problems/4sum/
标签: 数组, 排序, 相向双指针
掌握程度: ⚠️
解题思路: 对数组升序排序，为双指针创造有序条件，同时方便跳过重复数字，外层i、j分别进行去重：跳过和上一轮相同的数值，避免产生完全重复的四元组答案
关联题目:167. 两数之和 II - 输入有序数组、15. 三数之和
易错点: 
- 注意去重，尤其是固定的i和j
- 指针移动时要避免越界
"""

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    sm = nums[i] + nums[j] + nums[l] + nums[r]
                    if sm == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif sm < target:
                        l += 1
                    else:
                        r -= 1
        return res



# 更优解
"""
标签: 数组, 排序, 相向双指针、剪枝优化
解题思路: 
1. 前置判断：数组长度小于4时，直接返回空列表，不可能存在合法四元组
2. 数组升序排序，有序数组是双指针与高效去重、剪枝的前提
"""

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []
        
        nums.sort()
        res = []
        
        # 固定第一个数
        for i in range(n - 3):
            # 跳过重复的 nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # 剪枝1：当前最小的四数和已经大于 target，后面更大，直接结束
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            # 剪枝2：当前 i 能组成的最大四数和仍然小于 target，跳过这个 i
            if nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target:
                continue
            
            # 固定第二个数
            for j in range(i + 1, n - 2):
                # 跳过重复的 nums[j]
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # 剪枝3：固定 i,j 后的最小四数和大于 target，跳出 j 循环
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                # 剪枝4：固定 i,j 后的最大四数和小于 target，跳过当前 j
                if nums[i] + nums[j] + nums[n-2] + nums[n-1] < target:
                    continue
                
                # 双指针寻找剩余两个数
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        # 跳过重复的左值
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # 跳过重复的右值
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return res




if __name__ == "__main__":
    sol = Solution()
    # 测试用例1：题目示例1 常规多解场景 target=0
    assert sol.fourSum([1,0,-1,0,-2,2], 0) == [[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]]
    # 测试用例2：题目示例2 四数相同唯一解 target=8
    assert sol.fourSum([2,2,2,2,2], 8) == [[2,2,2,2]]
    # 测试用例3：空数组，无解
    assert sol.fourSum([], 0) == []
    # 测试用例4：数组长度不足4，无解
    assert sol.fourSum([1,2,3], 6) == []
    # 测试用例5：明显无法凑出目标值，无解
    assert sol.fourSum([0,1,1,2], 10) == []
    print("所有测试通过！")