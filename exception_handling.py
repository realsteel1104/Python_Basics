x = input("enter number 1 : ")
y = input("enter number 2 : ")

try:
    div = int(x) / int(y)
except Exception as e:
    print("Exception " , e)
    div = None
print(div)



