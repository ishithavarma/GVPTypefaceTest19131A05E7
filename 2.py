def countlast(x, y) :
    ans = 0
    for i in range(len(x)) :
        if (x[i] == y):
            ans = ans + 1
    return ans
s1=input() 
s2=input()
y = s2[-1]
print(countlast(s1, y))