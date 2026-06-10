"""
LeetCode: 205 同构字符串
难度: Easy
链接: https://leetcode.cn/problems/isomorphic-strings/
标签: 哈希表, 字符串
掌握程度: ⚠️
解题思路: 使用两个哈希表分别建立两个字符串字符间的双向映射，同步遍历字符。若出现映射冲突，则不是同构字符串，遍历完成则判定为同构。
关联题目: 290 单词规律
易错点: 
- 必须保证双向一一对应，单向映射会出现判断错误
- 两个字符串长度不一致时，可直接提前返回结果
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic_s = {}
        dic_t = {}
        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] not in dic_s:
                    if t[i] not in dic_t:
                        dic_s[s[i]] = t[i]
                        dic_t[t[i]] = s[i]
                    else:
                        return False
                else:
                    if t[i] != dic_s[s[i]]:
                        return False
            return True

if __name__ == "__main__":
    # 实例化解题对象
    sol = Solution()

    # 标准同构用例
    assert sol.isIsomorphic("egg", "add") == True
    # 字符映射冲突，非同构用例
    assert sol.isIsomorphic("foo", "bar") == False
    # 复杂字符同构用例
    assert sol.isIsomorphic("paper", "title") == True
    # 单向映射陷阱用例
    assert sol.isIsomorphic("ab", "aa") == False
    # 单字符用例
    assert sol.isIsomorphic("a", "b") == True

    print("所有测试通过!")