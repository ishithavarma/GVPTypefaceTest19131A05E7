n=int(input())
def baseThree(n):
    ans=""
    while n!=0:
        ans=str(n%3)+ans
        n=n//3
    return ans
print(baseThree(n))