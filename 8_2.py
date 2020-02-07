'''
回文数解法2

'''
def isPlindrom(num):
    if num<0 or not num % 10 and num:
        return False
    r =0
    while r<num:
        num,rem = num//10,num%10
        r = r*10+rem
    return num==r or num ==r//10

if __name__=='__main__':
    num =121
    if(isPlindrom(num)):
        print(num,'是回文数')
    else:print(num,'不是回文数')

