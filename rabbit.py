n=int(input("토끼의 휴식시간 : "))
m=int(input("거북이의 휴식시간 : "))

def lcm(n,m):
    while(m!=0):
        temp=n%m
        n=m
        m=temp
    return n

def gcd(n,m):
    result = n*m/(lcm(n,m))
    print(result)

gcd(n,m)
