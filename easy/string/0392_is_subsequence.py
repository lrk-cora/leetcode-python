"""
LeetCode: 392 判断子序列
难度: Easy
链接: https://leetcode.cn/problems/is-subsequence/
标签: 字符串, 双指针
掌握程度: ⚠️
解题思路: 先判断子串为空的特殊情况，遍历母串，逐个匹配子串字符。匹配成功则子串索引后移，索引走完代表全部匹配，提前返回结果。
关联题目: 792 匹配子序列的单词数
易错点: 
- 子串为空时直接返回 True
- 匹配完成后可提前终止循环，提升效率
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        idx = 0
        for i in t:
            if s[idx] == i:
                idx += 1
                if idx == len(s):
                    return True
        return False
    
if __name__ == "__main__":
    # 实例化解题对象
    sol = Solution()

    # 正常匹配子序列
    assert sol.isSubsequence("abc", "ahbgdc") == True
    # 无法构成子序列
    assert sol.isSubsequence("axc", "ahbgdc") == False
    # 子串为空字符串
    assert sol.isSubsequence("", "abc") == True
    # 子串与母串完全相同
    assert sol.isSubsequence("hello", "hello") == True
    # 子串长度大于母串
    assert sol.isSubsequence("abcd", "abc") == False

    print("所有测试通过!")