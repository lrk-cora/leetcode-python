"""
LeetCode: 844 比较含退格的字符串
难度: Easy
链接: https://leetcode.cn/problems/backspace-string-compare/
标签: 字符串, 栈
掌握程度: ✅
解题思路: 使用栈结构遍历字符串
关联题目: 1047 删除字符串所有相邻重复项
易错点: 
- #是指令符号，绝对不能存入栈中，不要把#当成普通字符添加
- 遍历完成后，通过join将两个栈转为最终成型的字符串，对比两个结果是否完全一致
PS:
- 可用指针优化算法，之后练习
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []
        for i in s:
            if i == '#':
                if stack_s:
                    stack_s.pop()
            else:
                stack_s.append(i)
        for j in t:
            if j == '#':
                if stack_t:
                    stack_t.pop()
            else:
                stack_t.append(j)
        res_s = ''.join(stack_s)
        res_t = ''.join(stack_t)
        return res_s == res_t
    
if __name__ == "__main__":
    sol = Solution()
    # 测试用例1：题目示例1，处理后均为ac
    assert sol.backspaceCompare("ab#c", "ad#c") == True
    # 测试用例2：题目示例2，两个字符串全部退格后均为空串
    assert sol.backspaceCompare("ab##", "c#d#") == True
    # 测试用例3：题目示例3，处理结果不同
    assert sol.backspaceCompare("a#c", "b") == False
    # 测试用例4：开头连续退格，空文本输入#无效果
    assert sol.backspaceCompare("###abc", "#abc") == True
    # 测试用例5：末尾退格、长度不一致的场景
    assert sol.backspaceCompare("a##b", "b") == True
    # 测试用例6：完全全退格清空
    assert sol.backspaceCompare("####", "") == True
    print("所有测试通过！")