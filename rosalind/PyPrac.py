'''k = 25
print(k)
j = 26
print(j)

klist = []
jlist = []

for i in range(1, 50):
    klist.append(i*k)

print(klist)

for m in range(1, 50):
    jlist.append(m*j)

print(jlist)

for n in range(1, 50) :
    klist[n-1] = klist[n-1]%26

print(klist)'''

'''k = 119

for i in range(2,119):
    j = k%i
    if j == 0 :
        print(i, j)
    else :
        continue'''


print(((25*7)+(25*13))%26)
print(((25*2)+(25*5))%26)