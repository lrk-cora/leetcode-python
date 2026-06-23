"""
LeetCode: 345 反转字符串中的元音字母
难度: Easy
链接: https://leetcode.cn/problems/reverse-vowels-of-a-string/submissions/
标签: 字符串、双指针
掌握程度: ✅
解题思路: 全程仅一次遍历，时间复杂度 O(n)，字符串转为列表操作，空间复杂度 O(n)。
关联题目: 977 有序数组的平方
易错点: 
- 循环条件 l < r，指针相遇时无需交换，避免重复处理；
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        lst = list(s)
        l = 0
        r = len(lst) - 1
        while l < r:
            if lst[l] in 'aeiouAEIOU' and lst[r] not in 'aeiouAEIOU':
                r -= 1
            elif lst[l] not in 'aeiouAEIOU' and lst[r] in 'aeiouAEIOU':
                l += 1
            elif lst[l] not in 'aeiouAEIOU' and lst[r] not in 'aeiouAEIOU':
                r -= 1
                l += 1
            else:
                lst[l], lst[r] = lst[r], lst[l]
                r -= 1
                l += 1
        return ''.join(lst)
    
# 断言测试用例
if __name__ == "__main__":
    sol = Solution()
    assert sol.reverseVowels("IceCreAm") == "AceCreIm"
    assert sol.reverseVowels("leetcode") == "leotcede"
    assert sol.reverseVowels("bcdfgh") == "bcdfgh"
    assert sol.reverseVowels("u") == "u"
    # assert sol.reverseVowels("AEiou") == "uoiEA"
    # assert sol.reverseVowels("aabbEE") == "EEbbaa"

    print("所有测试用例全部通过！")




# 可改写成更强进的不易出错的while循环
class Solution:
    def reverseVowels(self, s: str) -> str:
        lst = list(s)
        l = 0
        r = len(lst) - 1
        vowels = 'aeiouAEIOU'
        while l < r:
            # 左指针找元音，不是就右移，保证l<r防止越界
            while l < r and lst[l] not in vowels:
                l += 1
            # 右指针找元音，不是就左移
            while l < r and lst[r] not in vowels:
                r -= 1
            # 左右都为元音，交换
            lst[l], lst[r] = lst[r], lst[l]
            l += 1
            r -= 1
        return ''.join(lst)

if __name__ == "__main__":
    sol = Solution()
    assert sol.reverseVowels("IceCreAm") == "AceCreIm"
    assert sol.reverseVowels("leetcode") == "leotcede"
    assert sol.reverseVowels("bcdfgh") == "bcdfgh"
    assert sol.reverseVowels("u") == "u"
    assert sol.reverseVowels("AEiou") == "uoiEA"
    assert sol.reverseVowels("aabbEE") == "EEbbaa"

    print("所有测试用例全部通过！")