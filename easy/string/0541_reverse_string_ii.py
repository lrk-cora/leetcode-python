"""
LeetCode: 541 反转字符串 II
难度: Easy
链接: https://leetcode.cn/problems/reverse-string-ii/
标签: 字符串, 切片
掌握程度: ⚠️
解题思路: 以 2k 个字符为一轮循环截取字符串，每一轮先反转前 k 个字符，再拼接后 k 个原字符，逐步拼接得到最终结果。
关联题目: 344 反转字符串
易错点: 
- 利用字符串切片自动处理末尾字符不足的边界，无需额外判断
- 循环步长固定为 2k，保证分段规则符合题目要求
"""

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = ''
        cur = 0
        while cur < len(s):
            front = s[cur: cur + k]
            res = res + front[::-1] + s[cur + k : 2 * k + cur]
            cur += 2 * k
        return res
    
if __name__ == "__main__":
    # 实例化解题对象
    sol = Solution()

    # 标准用例，完整分段
    assert sol.reverseStr("abcdefg", 2) == "bacdfeg"
    # 整体长度小于k，全部反转
    assert sol.reverseStr("hello", 10) == "olleh"
    # 长度等于k，整体反转
    assert sol.reverseStr("abcd", 4) == "dcba"
    # k=1，无需反转
    assert sol.reverseStr("leetcode", 1) == "leetcode"

    print("所有测试通过!")