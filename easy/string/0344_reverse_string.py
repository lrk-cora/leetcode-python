"""
LeetCode: 344 反转字符串
难度: Easy
链接: https://leetcode.cn/problems/reverse-string/
标签: 字符串, 双指针
掌握程度: ✅
解题思路: 采用双指针法，左指针指向头部、右指针指向尾部，交换两指针位置字符，随后两指针向中间靠拢，直至相遇完成反转。题目要求原地修改输入数组。
关联题目: 9 回文数、125 验证回文串
易错点: 
- 必须在原数组上原地修改，不能新建数组返回
"""

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        slow = 0
        fast = len(s) - 1
        while slow < fast:
            s[slow], s[fast] = s[fast], s[slow]
            slow += 1
            fast -= 1

if __name__ == "__main__":
    # 实例化解题对象
    sol = Solution()

    # 常规字符数组
    s1 = ["h","e","l","l","o"]
    sol.reverseString(s1)
    assert s1 == ["o","l","l","e","h"]

    # 含大写字母数组
    s2 = ["H","a","n","n","a","h"]
    sol.reverseString(s2)
    assert s2 == ["h","a","n","n","a","H"]

    # 单字符数组
    s3 = ["A"]
    sol.reverseString(s3)
    assert s3 == ["A"]

    # 空数组
    s4 = []
    sol.reverseString(s4)
    assert s4 == []

    print("所有测试通过!")