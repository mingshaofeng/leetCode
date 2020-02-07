# -*-coding:UTF-8 -*-
import re
class Solution:
    def reverse(self, x: int) -> int:
        #保留原数的正负号
        tag = 1 if x >=0 else -1
        #将数字转化为字符串
        st  = str(abs(x))
        #利用正则化将字符串的每一个数字切割出来
        st = ''.join(re.findall('(.*)0*',st))
        #将字符串列表化
        st = list(st)
        #列表反转
        st.reverse()
        #正数化，将前面的0去掉
        res = int(''.join(st[0:len(st)]))
        #溢出后返回0
        res = res if res >= -2147483648 and res <=2147483647 else 0
        return res*tag


if __name__=="__main__":
    s = Solution()
    res = s.reverse(12345670)
    print(res)