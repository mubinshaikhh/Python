#To read contents of a file in reverse order.

f = open('text.txt','r')
for line in f:
    f = line[::-1]
    print(f)
