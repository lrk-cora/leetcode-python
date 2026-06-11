"""
LeetCode: 1047 删除字符串所有相邻重复项
难度: Easy
链接: https://leetcode.cn/problems/remove-all-adjacent-duplicates-in-string/
标签: 字符串, 栈
掌握程度: ⚠️
解题思路: 借助栈结构遍历字符串，若当前字符与栈顶元素相同，则弹出栈顶（消除相邻重复）；否则将字符入栈，最终拼接栈内元素得到结果。
关联题目: 20 有效的括号
易错点: 
- 先判断栈是否为空，再取栈顶元素，避免下标报错
- 重复消除是持续迭代的，栈天然支持连环相邻重复删除
"""

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if stack and i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)
    
if __name__ == "__main__":
    # 实例化解题对象
    sol = Solution()

    # 基础相邻重复
    assert sol.removeDuplicates("abbaca") == "ca"
    # 全部两两重复
    assert sol.removeDuplicates("aabbcc") == ""
    # 无相邻重复
    assert sol.removeDuplicates("abcde") == "abcde"
    # 连环重复删除
    assert sol.removeDuplicates("aaaa") == ""

    print("所有测试通过!")