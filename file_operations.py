#write process
f = open("D:\\code\\file_op.txt","w")
f.write("file_operations writing process")

#append process
f = open("D:\\code\\file_op.txt","a")
f.write("\nNext operation is append")

#read file line by line
f = open("D:\\code\\file_op.txt","r")
f_next = open("D:\\code\\file_next.txt","w")

for line in f:
    tokens = line.split(" ")                #split line using spaces in between to seperate them to words (output is array)
    print(tokens)
    f_next.write("wordcount"  + str(len( tokens)) + "  "+  line   )

f.close()
f_next.close()
