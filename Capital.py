#To read a file and capitalize the first letter of everyword in a file.

f = open('text.txt','r')
for line in f:
    f = line.title()
    print(f)