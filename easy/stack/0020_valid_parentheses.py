"""
LeetCode: 20 有效的括号
难度: Easy
链接: https://leetcode.cn/problems/valid-parentheses/
标签: 字符串, 栈
掌握程度: ✅
解题思路: 使用栈结构遍历字符串，遇到左括号入栈；遇到右括号则弹出栈顶元素比对，不匹配直接返回 false。遍历结束后栈为空则括号全部匹配。
关联题目: 1047 删除字符串所有相邻重复项
易错点: 
- 出现右括号时栈为空，直接判定无效
- 遍历完成后需检查栈是否还有剩余左括号
"""

class Solution:
    def isValid(self, s: str) -> bool:
        match = {')': '(', '}': '{', ']': '['}
        stack = []
        for i in s:
            if i in '([{':
                stack.append(i)
            else:
                if not stack:
                    return False
                elif match[i] != stack.pop():
                    return False
        if not stack:
            return True
        else:
            return False
        
if __name__ == "__main__":
    sol = Solution()
    assert sol.isValid("()") == True
    assert sol.isValid("()[]{}") == True
    assert sol.isValid("(]") == False
    assert sol.isValid("([)]") == False
    assert sol.isValid("{[]}") == True
    print("所有测试通过!")