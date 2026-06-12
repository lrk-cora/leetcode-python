"""
LeetCode: 1281 整数的各位积和之差
难度: Easy
链接: https://leetcode.cn/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
标签: 数学, 字符串转换
掌握程度: ✅
解题思路: 将整数转为字符串遍历每一位数字，分别计算各位数字的乘积与总和，最后求两者差值。
关联题目: 无
易错点: 
- 遍历字符时记得转回整型计算
"""

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        pro1 = 1
        sum2 = 0
        for item in str(n):
            pro1 *= int(item)
            sum2 += int(item)

        return pro1 - sum2
    
if __name__ == "__main__":
    sol = Solution()
    assert sol.subtractProductAndSum(234) == 15
    assert sol.subtractProductAndSum(4421) == 21
    assert sol.subtractProductAndSum(1) == 0
    print("所有测试通过!")