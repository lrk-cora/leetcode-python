"""
LeetCode: 709 转换成小写字母
难度: Easy
链接: https://leetcode.cn/problems/to-lower-case/
标签: 字符串, 字符编码
掌握程度: ✅
解题思路: 遍历字符串，判断字符是否为大写字母，利用 ASCII 码差值 +32 转为小写，其他字符直接拼接，最终返回结果。
关联题目: 344 反转字符串、541 反转字符串 II
易错点: 
- 牢记大小写字母 ASCII 码相差 32
"""

class Solution:
    def toLowerCase(self, s: str) -> str:
        res = ''
        for item in range(len(s)):
            if 'A' <= s[item] <= 'Z':
                res += chr(ord(s[item]) + 32)
            else:
                res += s[item]
        return res
    
if __name__ == "__main__":
    # 实例化解题对象
    sol = Solution()

    # 大小写混合
    assert sol.toLowerCase("Hello") == "hello"
    # 全大写
    assert sol.toLowerCase("LOVELY") == "lovely"
    # 字母+符号+数字混合
    assert sol.toLowerCase("al&phaBET") == "al&phabet"
    # 全小写
    assert sol.toLowerCase("python") == "python"

    print("所有测试通过!")