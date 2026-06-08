"""
LeetCode: 485 最大连续 1 的个数
难度: Easy
链接: https://leetcode.cn/problems/max-consecutive-ones/
标签: 数组, 遍历统计
掌握程度: ✅
解题思路: 遍历数组，用计数器记录当前连续1的长度，遇到1则计数器+1，遇到0则重置计数器，同时用变量保存过程中的最大值
关联题目: 无
易错点: 
- 数组末尾是1的情况，循环结束后也要更新最大值
"""

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur_count = 0
        max_count = 0
        for i in nums:
            if i == 1:
                cur_count += 1
                if max_count <= cur_count:
                    max_count = cur_count
            else:
                cur_count = 0
        return max_count
    
if __name__ == "__main__":
    sol = Solution()
    # 测试用例1：正常情况
    assert sol.findMaxConsecutiveOnes([1,1,0,1,1,1]) == 3
    # 测试用例2：全是1
    assert sol.findMaxConsecutiveOnes([1,1,1,1]) == 4
    # 测试用例3：全是0
    assert sol.findMaxConsecutiveOnes([0,0,0]) == 0
    # 测试用例4：开头/结尾是1
    assert sol.findMaxConsecutiveOnes([1,0,1,1,0]) == 2
    print("所有测试通过！")