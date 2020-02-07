# -*-coding:utf-8 -8-
def romtoint(s):
    line =list(s)
    sums=0
    nums={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    for i in range(len(s)-1):

        if (nums[s[i]]<nums[s[i+1]]):
            sums -= nums[line[i]]
        else:
            sums += nums[line[i]]
    sums+=nums[line[-1]]
    print (sums)

if __name__=='__main__':
    s='MCMXCIV'
    romtoint(s)