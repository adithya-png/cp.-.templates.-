import math
d=list(map(int,input().split()))
m=len(d)
st=[0]*(m)+d
for i in range(m-1,0,-1):
    st[i]=math.gcd(st[2*i],st[2*i+1])
def upd(i,x):
    i+=m
    st[i]=x
    i//=2
    while(i):
        st[i]=math.gcd(st[2*i],st[2*i+1])
        i//=2
def query(l,r):
    l+=m
    r+=m
    ans=0
    while(l<r):
        if l%2==1:
            ans=math.gcd(ans,st[l])
            l+=1
        if r%2==1:
            r-=1
            ans=math.gcd(ans,st[r])
        l//=2
        r//=2
    return ans
#l,r are 0-indexed, [l,r)






