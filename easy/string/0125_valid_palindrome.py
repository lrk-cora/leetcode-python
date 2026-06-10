"""
LeetCode: 125 验证回文串
难度: Easy
链接: https://leetcode.cn/problems/valid-palindrome/
标签: 字符串, 双指针
掌握程度: ✅
解题思路: 先过滤掉非字母、数字字符并统一转为小写，再使用双指针分别从首尾向中间遍历，逐一比对字符是否相等。
关联题目: 9 回文数
易错点: 
- 需要忽略空格、标点等非字母数字字符
- 空字符串、仅含符号的字符串均判定为回文串
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = s.lower()
        res = ''
        for i in range(len(s)):
            if 'a' <= s_new[i] <= 'z' or '0' <= s_new[i] <= '9':
                res += s_new[i]
        slow = 0
        fast = len(res) - 1
        while slow < fast:
            if res[slow] != res[fast]:
                return False
            slow += 1
            fast -= 1
        return True
    
if __name__ == "__main__":
    # 实例化解题对象
    sol = Solution()

    # 含字母、数字、空格、标点的标准用例
    assert sol.isPalindrome("A man, a plan, a canal: Panama") == True
    # 非回文字符串用例
    assert sol.isPalindrome("race a car") == False
    # 空字符串用例
    assert sol.isPalindrome("") == True
    # 纯标点符号用例
    assert sol.isPalindrome(".,") == True
    # 纯数字回文用例
    assert sol.isPalindrome("12321") == True

    print("所有测试通过!")