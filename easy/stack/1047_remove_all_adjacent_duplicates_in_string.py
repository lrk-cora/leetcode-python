"""
LeetCode: 1047 删除字符串所有相邻重复项
难度: Easy
链接: https://leetcode.cn/problems/remove-all-adjacent-duplicates-in-string/
标签: 字符串, 栈
掌握程度: ✅
解题思路: 遍历字符串，借助栈判断当前字符与栈顶是否相同；相同则弹出栈顶消除相邻重复，不同则将字符入栈，最终拼接栈内字符得到结果。
关联题目: 20 有效的括号、1544 整理字符串
易错点: 
- 取栈顶前先判断栈非空，避免索引报错
- 重复消除会连锁生效，栈可天然处理连环相邻重复
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
    sol = Solution()
    assert sol.removeDuplicates("abbaca") == "ca"
    assert sol.removeDuplicates("aabbcc") == ""
    assert sol.removeDuplicates("abc") == "abc"
    assert sol.removeDuplicates("aaaa") == ""
    print("所有测试通过!")