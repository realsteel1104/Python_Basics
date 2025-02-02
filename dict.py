d = {"tom" : 123 , "123":"tom"}
print(d)

for key in d:
    print("key" , key , "value" ,d[key])

for key,value in d.items():
    print("key" , key , "value" ,d[key])
