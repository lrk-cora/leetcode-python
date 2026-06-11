"""
LeetCode: 1221 分割平衡字符串
难度: Easy
链接: https://leetcode.cn/problems/split-a-string-in-balanced-strings/
标签: 字符串, 计数
掌握程度: ✅
解题思路: 遍历字符串，分别统计字符 L 和 R 的数量，当两者计数相等时，说明分割出一个平衡字符串，结果计数加一并清空统计值，继续向后遍历。
关联题目: 1047 删除字符串所有相邻重复项
易错点: 
- 每次达成平衡后及时重置两个计数器
"""

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        countR = 0
        countL = 0
        res = 0
        for i in range(len(s)):
            if s[i] == 'R':
                countR += 1
            else:
                countL += 1
            if countL == countR:
                res += 1
                countL = 0
                countR = 0
        return res
    
if __name__ == "__main__":
    # 实例化解题对象
    sol = Solution()

    # 常规分割用例
    assert sol.balancedStringSplit("RLRRLLRLRL") == 4
    # 整体为一个平衡串
    assert sol.balancedStringSplit("RLLLLRRRLR") == 3
    # 两两交替
    assert sol.balancedStringSplit("LLLLRRRR") == 1
    # 最短平衡串
    assert sol.balancedStringSplit("RL") == 1

    print("所有测试通过!")