"""
LeetCode: 9 回文数 
难度: Easy
链接: https://leetcode.cn/problems/palindrome-number/
标签: 数学, 双指针
掌握程度: ✅
解题思路: 将整数直接转为字符串，利用Python切片 `s[::-1]` 反转字符串
关联题目: 125 验证回文串
易错点: 
- 该方法会额外占用字符串的空间，空间复杂度为 O(n)
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        if s == s[::-1]:
            return True
        else:
            return False
        
# --- 测试代码 ---
if __name__ == "__main__":
    sol = Solution()

    # 测试用例1: 典型回文数
    assert sol.isPalindrome(121) == True
    # 测试用例2: 负数（天然非回文）
    assert sol.isPalindrome(-121) == False
    # 测试用例3: 末尾为0的非零数（非回文）
    assert sol.isPalindrome(10) == False
    # 测试用例4: 单个数字（一定是回文）
    assert sol.isPalindrome(0) == True
    # 测试用例5: 较大的回文数
    assert sol.isPalindrome(12321) == True
    # 测试用例6: 较大的非回文数
    assert sol.isPalindrome(12345) == False

    print("所有测试通过!")