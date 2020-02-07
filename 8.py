'''
回文数
'''
import re
def Palindrome_Number(num):
    if num<0:
        return False
    else:
        st = str(num)
        st = ''.join(re.findall('(.*)0*', st))
        st =list(st)
        st.reverse()
        res = int(''.join(st[0:len(st)]))
        if (res==num):
            return True
        else:
            return False
if __name__=='__main__':
    num =12
    if(Palindrome_Number(num)):
        print(num,'是回文数')
    else:print(num,'不是回文数')