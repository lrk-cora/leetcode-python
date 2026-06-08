"""
LeetCode: 66 加一
难度: Easy
链接: https://leetcode.cn/problems/plus-one/
标签: 数组, 数学模拟
掌握程度: ✅
解题思路 1: 先将数组转为字符串再转成整数加一，再将结果转为字符串，逐位拆分存入数组并反转得到结果
关联题目: 无
易错点: 
- 转换为整数时，若数组过长会存在溢出风险（Python对大数支持较好，但其他语言会报错）
- 结果数组需要反转，否则数字顺序会颠倒
- 空数组/0的特殊情况需要处理
"""

from typing import List

class Solution:
    def plusOne_convert(self, digits: List[int]) -> List[int]:
        s = ''.join(str(i) for i in digits)
        pro = int(s) + 1
        res = []
        while pro > 0:
            num = pro % 10
            last = pro // 10
            res.append(num)
            pro = last
        res.reverse()
        return res

if __name__ == "__main__":
    sol = Solution()
    # 测试用例1：正常加一
    assert sol.plusOne_convert([1,2,3]) == [1,2,4]
    # 测试用例2：末尾进位
    assert sol.plusOne_convert([4,3,2,1]) == [4,3,2,2]
    # 测试用例3：全9进位
    assert sol.plusOne_convert([9,9,9]) == [1,0,0,0]
    # 测试用例4：单元素非9
    assert sol.plusOne_convert([0]) == [1]
    # 测试用例5：单元素9
    assert sol.plusOne_convert([9]) == [1,0]
    print("所有测试通过！")

"""
LeetCode: 66 加一
难度: Easy
链接: https://leetcode.cn/problems/plus-one/
标签: 数组, 数学模拟
掌握程度: ✅
解题思路 2: 从数组末尾开始模拟加法进位，若当前位+1后为10则置0并继续进位；若所有位都进位完成，需在数组开头补1
关联题目: 0067 二进制求和（同数字字符串/数组模拟进位思路）
易错点:
- 进位处理：末尾为9时需要连续进位
- 全9的特殊情况：如[9,9,9]加一后变成[1,0,0,0]，数组长度会+1
- 不要直接把数组转成整数再运算，会有溢出风险
"""

class Solution:
    def plusOne_carry(self, digits: List[int]) -> List[int]:
        n = len(digits)
        # 从最后一位开始加
        for i in range(n - 1, -1, -1):
            digits[i] += 1
            if digits[i] < 10:
                return digits
            digits[i] = 0
        # 所有位都进位了，需要补1
        return [1] + digits

if __name__ == "__main__":
    sol = Solution()
    # 测试用例1：正常加一
    assert sol.plusOne_carry([1,2,3]) == [1,2,4]
    # 测试用例2：末尾进位
    assert sol.plusOne_carry([4,3,2,1]) == [4,3,2,2]
    # 测试用例3：全9进位
    assert sol.plusOne_carry([9,9,9]) == [1,0,0,0]
    # 测试用例4：单元素非9
    assert sol.plusOne_carry([0]) == [1]
    # 测试用例5：单元素9
    assert sol.plusOne_carry([9]) == [1,0]
    print("所有测试通过！")