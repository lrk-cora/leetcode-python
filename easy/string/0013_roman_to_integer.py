"""
LeetCode: 13 罗马数字转整数
难度: Easy
链接: https://leetcode.cn/problems/roman-to-integer/
标签: 哈希表, 数学, 字符串
掌握程度: ✅
解题思路: 利用哈希表映射字符与数值，从后向前遍历字符串。当前字符值大于等于右侧则累加，小于则做减法。
关联题目: 12 整数转罗马数字
易错点: 
- 从倒数第一位开始初始化数值，遍历范围注意下标边界
- 严格区分左右字符大小关系，决定加减逻辑
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        val = roman[s[-1]]
        for i in range(len(s) - 2, -1, -1):
            item = s[i]
            right_item = s[i + 1]
            if roman[item] >= roman[right_item]:
                val += roman[item]
            else:
                val -= roman[item]
        return val
    
if __name__ == "__main__":
    # 实例化解题对象
    sol = Solution()

    # 常规累加用例：III -> 3
    assert sol.romanToInt("III") == 3
    # 左侧小于右侧特殊用例：IV -> 4
    assert sol.romanToInt("IV") == 4
    # 左侧小于右侧特殊用例：IX -> 9
    assert sol.romanToInt("IX") == 9
    # 混合常规与特殊组合：LVIII -> 58
    assert sol.romanToInt("LVIII") == 58
    # 复杂组合用例：MCMXCIV -> 1994
    assert sol.romanToInt("MCMXCIV") == 1994

    print("所有测试通过!")