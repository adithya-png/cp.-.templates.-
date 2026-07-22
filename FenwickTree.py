BIT=[0]*(n+1)
def ind(i):
    return i+1
def add(i,x):
    i=ind(i)
    while(i<=len(BIT)-1):
        BIT[i]+=x
        i+=i&-i
def psum(i):
    i=ind(i)
    ans=0
    while(i>=1):
        ans+=BIT[i]
        i-=i&-i
    return ans
