"""
LeetCode: 242 有效的字母异位词
难度: Easy
链接: https://leetcode.cn/problems/valid-anagram/
标签: 字符串, 哈希表
掌握程度: ⚠️
解题思路: 先判断两字符串长度，不等直接返回 false。用字典统计第一个字符串字符频次，再遍历第二个字符串抵消频次，最后检查所有频次是否归零。
关联题目: 217 存在重复元素
易错点: 
- 长度不同一定不是异位词，可提前剪枝
- 使用 dict.get 避免键不存在时报错
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        for j in t:
            dic[j] = dic.get(j, 0) - 1
        for v in dic.values():
            if v != 0:
                return False
        return True
    
if __name__ == "__main__":
    sol = Solution()
    assert sol.isAnagram("anagram", "nagaram") == True
    assert sol.isAnagram("rat", "car") == False
    assert sol.isAnagram("", "") == True
    assert sol.isAnagram("a", "aa") == False
    print("所有测试通过!")