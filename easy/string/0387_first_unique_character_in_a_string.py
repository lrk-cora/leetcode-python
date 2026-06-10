"""
LeetCode: 387 字符串第一个唯一字符
难度: Easy
链接: https://leetcode.cn/problems/first-unique-character-in-a-string/
标签: 字符串, 双指针
掌握程度: ✅
解题思路: 先用哈希表统计每个字符出现的次数，再从头遍历字符串，找到第一个出现次数为 1 的字符并返回其下标；若不存在唯一字符则返回 -1。
关联题目: 205 同构字符串、242 有效的字母异位词
易错点: 
- 所有字符均重复时，记得返回 -1
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1
        for keys, values in dic.items():
            if values == 1:
                return s.find(keys)
        return -1
    
if __name__ == "__main__":
    # 实例化解题对象
    sol = Solution()

    # 存在唯一字符
    assert sol.firstUniqChar("leetcode") == 0
    assert sol.firstUniqChar("loveleetcode") == 2
    # 所有字符均重复
    assert sol.firstUniqChar("aabb") == -1
    # 单字符
    assert sol.firstUniqChar("z") == 0

    print("所有测试通过!")