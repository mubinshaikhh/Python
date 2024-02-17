#Read a text file & count the number of curtain letter appears in text file

f=open('a.txt','r')
r=f.read()
o=r.count(input('Enter letter: '))
print('Letter count:',o)