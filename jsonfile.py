import json
book = {}
book['me'] = {
    'name' : 'Pratik',
    "address" : 'Pune',
    "phone" : 232323232
}

book['me1'] = {
    'name' : 'Pratik1',
    "address" : 'Pune1',
    "phone" : 2323232322
}
print(book)

s = json.dumps(book)                    #convert dict to dump to string
print("type" , type(s) , s)

with open("D://code//book.txt",'w') as f:
    f.write(s)

f = open("D://code//book.txt",'r')
s = f.read()
book = json.loads(s)
print("type" , type(book) , book)