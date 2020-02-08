
def Nostring(s:str)->int:
    length, j = 0,-1;
    for i, x in enumerate(s):
        if x in s[j+1:i]:
            print(x)
            print("i-j-1:{}".format(i-j-1))
            length = max(length,i-j-1)
            j=s[j+1:i].index(x)+j+1
            print("j:{}".format(j))
    return max(length,len(s)-1-j)

if __name__=="__main__":
    s='abcabcbb'
    print(Nostring(s))