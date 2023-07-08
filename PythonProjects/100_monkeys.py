keys = []
for i in range(2,101):
    for j in range(2,101):
        if j%i == 0:
            keys.append(j)
y = []
for k in keys:
    x = []
    for j in keys:
        if j==k:
            x.append(k)
    if len(x)%2 == 0:
        for i in x:
            y.append(i)

y.append
a= set(y)
doors = sorted(a)
print(doors)
        
    

