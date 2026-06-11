"""
LeetCode: 67 二进制求和
难度: Easy
链接: https://leetcode.cn/problems/add-binary/
标签: 字符串, 双指针
掌握程度: ✅
解题思路: 利用Python内置函数将二进制字符串转为十进制整数，相加后再转回二进制字符串，截取掉前缀标识得到结果。
关联题目: 415 字符串相加
易错点: 
- bin() 转换结果会自带前缀 0b，需要切片截取有效部分
- 注意超长二进制字符串可能存在整数范围限制
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_pro = int(a, 2)
        b_pro = int(b, 2)
        pal = a_pro + b_pro
        res = bin(pal)
        return res[2:]

if __name__ == "__main__":
    # 实例化解题对象
    sol = Solution()

    # 基础相加用例
    assert sol.addBinary("11", "1") == "100"
    # 多位数二进制相加
    assert sol.addBinary("1010", "1011") == "10101"
    # 两个0相加
    assert sol.addBinary("0", "0") == "0"
    # 单二进制位相加
    assert sol.addBinary("1", "0") == "1"

    print("所有测试通过!")