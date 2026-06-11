"""
LeetCode: 1544 整理字符串
难度: Easy
链接: https://leetcode.cn/problems/make-the-string-great/
标签: 字符串, 栈
掌握程度: ✅
解题思路: 利用栈遍历字符串，若当前字符与栈顶字符互为大小写，则弹出栈顶字符；否则将当前字符压入栈中，最后拼接栈内字符得到结果。
关联题目: 1047 删除字符串所有相邻重复项
易错点: 
- 判断相邻字符是否为同一字母的大小写形式
- 需先判断栈非空再访问栈顶元素，避免报错
"""

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in s:
            if stack and i == stack[-1].swapcase():
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)
    
if __name__ == "__main__":
    # 实例化解题对象
    sol = Solution()

    # 基础相邻大小写组合
    assert sol.makeGood("leEe") == "le"
    # 连续多组大小写
    assert sol.makeGood("abBAcC") == ""
    # 无需要整理的字符
    assert sol.makeGood("s") == "s"
    assert sol.makeGood("Pp") == ""

    print("所有测试通过!")