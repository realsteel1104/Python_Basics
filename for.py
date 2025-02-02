exp = [2100 , 4356, 575, 667666]
total = 0
for item in exp:
    total = total + item

print(total)

for i in range(1,11):
    print(i)

for i in range(len(exp)):
    print("Month " , (i+1),"Expense",exp[i])
i=0
while i<len(exp) :
    print(exp[i])
    i = i + 1